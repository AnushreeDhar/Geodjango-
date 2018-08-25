
import os
import django.contrib.gis.utils import LayerMapping
from .models import Counties

counties_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(o.path.join(os.path.dirname(_file_),'data/counties.shp'))

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transorm=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)