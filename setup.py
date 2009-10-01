#!/usr/bin/env python
from setuptools import setup, find_packages

import djangospot

setup(
    name='DjangoSpot',
    version=".".join(map(str, djangospot.__version__)),
    #packages=find_packages(),
    #include_package_data=True,
    author='David Cramer',
    author_email='dcramer@gmail.com',
    # zip_safe breaks non-python files
    zip_safe=False,
    install_requires=[
        'Jinja2>=2.2',
        'Django==1.1',
        'South>=0.6',
        'coffin>=0.3.1',
        'python-memcached==1.43',
        'django-ratings>=0.3.1',
        'django-sphinx>=2.0.2',
        'django-tagging>=0.3',
        'django-treebeard',
        'django-registration',
        'MySQL-python',
    ],
    description="",
)