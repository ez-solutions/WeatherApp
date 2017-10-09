import os

from setuptools import setup, find_packages, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='mysite',
    version='0.0.1',
    description='Find out the weather in you ',
    long_description=read('README.md'),
    # author='Mandla Mbuli',
    # author_email='mail@mandla.me',
    # license='BSD',
    url='',
    packages=find_packages(),
    install_requires=[
        'Django'
    ],
    # cmdclass={'test': PyTest},
    include_package_data=True,
    classifiers=[
        # "Private :: Do Not Upload",
        "Programming Language :: Python",
        # "License :: OSI Approved :: BSD License",
        # "Development Status :: 1 - Alpha",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)

