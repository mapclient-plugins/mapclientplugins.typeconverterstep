'''
MAP Client Plugin
'''

__version__ = '0.2.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Type Converter'
__location__ = 'https://github.com/mapclient-plugins/typeconverterstep/archive/master.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.typeconverterstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
