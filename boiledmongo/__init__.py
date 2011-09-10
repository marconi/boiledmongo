# -*- coding: utf-8 -*-

from paste.util.template import paste_script_template_renderer
from pyramid.scaffolds import PyramidTemplate


class BoiledMongoProjectTemplate(PyramidTemplate):
    _template_dir = 'boiled'
    summary = 'pyramid MongoDB project based on pyramid_starter'
    template_renderer = staticmethod(paste_script_template_renderer)
