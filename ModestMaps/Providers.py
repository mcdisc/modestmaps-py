from Core import Coordinate
from Geo import LinearProjection, MercatorProjection, Transformation

ids = ('MICROSOFT_ROAD', 'MICROSOFT_AERIAL', 'MICROSOFT_HYBRID',
       'GOOGLE_ROAD',    'GOOGLE_AERIAL',    'GOOGLE_HYBRID',
       'YAHOO_ROAD',     'YAHOO_AERIAL',     'YAHOO_HYBRID',
       'BLUE_MARBLE',
       'OPEN_STREET_MAP')

class IMapProvider:
    def __init__(self):
        raise NotImplementedError("Abstract method not implemented by subclass.")
        
    def getTileUrl(self, coordinate):
        raise NotImplementedError("Abstract method not implemented by subclass.")

    def locationCoordinate(self, location):
        return self.projection.locationCoordinate(location)

    def coordinateLocation(self, location):
        return self.projection.coordinateLocation(location)

    def sourceCoordinate(self, coordinate):
        raise NotImplementedError("Abstract method not implemented by subclass.")