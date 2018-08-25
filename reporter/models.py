
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry



# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(srid=4326, spatial_index=False)
    

    def _unicode_(self):
        return self.name
    
class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(null=True)

    def _unicode_(self):
        return self.counties   
