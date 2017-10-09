from __future__ import unicode_literals
import requests
import json
import re
from datetime import datetime

from django.conf import settings

from . import models
from .log import logger


def get_raw_data(url, headers, payload):
    http_response = requests.post(url, headers=headers, data=json.dumps(payload))
    date_rgx = re.compile(r'"Date":new Date\(Date.UTC\((?P<date>\d{1,4},\d{1,2},\d{1,2})[\d,]+\)\)', re.MULTILINE)
    logger.info("Retrieving forecasts from: %s", url)
    response = http_response.text.replace(";/*", "")
    response = re.sub(date_rgx, '"Date": "\g<date>"', response)
    json_response = json.loads(response)
    logger.info("JSON formatted respons: %s", json.dumps(json_response))
    return json_response


def map_data(raw_data):
    forecasts_key_map = settings.APP['key_map']

    data = {}
    data['city_code'] = raw_data['City']
    data['city_name'] = raw_data['CityName']
    data['forecasts'] = []
    for forecast in raw_data['Forecasts']:
        mapped_field = {}
        for field_name, column_name in forecasts_key_map.items():
            if field_name == 'Date':
                mapped_field[column_name] = forecast['FormattedDate']
            else:
                mapped_field[column_name] = forecast[field_name]
        data['forecasts'].append(mapped_field)
    logger.info("Mapped forecasts data: %s", data)
    return data


def persist_data(data):
    city, _ = models.City.objects.get_or_create({
        'code': data['city_code'],
        'name': data['city_name']
    })

    forecast_data = data['forecasts']
    logger.info("Update forecast data for [%s]", data['city_name'])
    for forecast_datum in forecast_data:
        forecast_datum['city'] = city
        models.Forecast.objects.update_or_create(**forecast_datum)


def save_data(url, headers, payload):

    raw_data = get_raw_data(url, headers, payload)
    data = map_data(raw_data)
    persist_data(data)
