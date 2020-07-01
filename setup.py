#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
        name='tweet_commune',
        version='1.2.1',
        description='Crowdsourced Twitter account',
        author='Jack Phallen',
        author_email='jackphallen@gmail.com',
        url='https://github.com/JackPhallen/TweetCommune',
        packages=find_packages(),
        scripts=['manage.py'],
    )
