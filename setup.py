#!/usr/bin/env python

import os
from setuptools import setup

base_root = os.path.dirname(os.path.realpath(__file__))
exts = []
for root, dirs, files in os.walk(base_root):
    if not '.git' in root:
        for f in files:
            _, ext = os.path.splitext(f)
            if not ext in exts and ext:
                p = root[len(base_root) + len('/boiledmongo/'):]
                exts.append(os.path.join(p, "*%s" % ext))


setup(name='boiled-mongo',
    version='0.1',
    description='A Pyramid project boiler plate that uses MongoDB as database.',
    author='Marconi Moreto',
    author_email='Marconi Moreto <caketoad@gmail.com>',
    packages=['boiledmongo'],
    include_package_data=True,
    package_data = {
        '': exts,
    },
    zip_safe=False,
    install_requires=['pyramid>=1.0', 'pymongo', 'mongoengine'],
    keywords="pyramid project template",
    entry_points="""
        [paste.paster_create_template]
        boiledmongo = boiledmongo:BoiledMongoProjectTemplate
        """
)
