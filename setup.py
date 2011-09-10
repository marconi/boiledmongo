#!/usr/bin/env python
from setuptools import setup


setup(name='boiled-mongo',
    version='0.1',
    description='A Pyramid project boiler plate that uses MongoDB as database.',
    author='Marconi Moreto',
    author_email='Marconi Moreto <caketoad@gmail.com>',
    packages=['boiledmongo'],
    install_requires=['pyramid>=1.0', 'pymongo'],
    keywords="pyramid project template",
    entry_points="""
        [paste.paster_create_template]
        boiledmongo = boiledmongo:BoiledMongoProjectTemplate
        """
)
