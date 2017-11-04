from mediacore.lib.base import BaseController
from mediacore.lib.decorators import (expose, observable)
from mediacore.plugin import events

import googlemaps
import logging
log = logging.getLogger(__name__)


class MapController(BaseController):
    """
        Map Controller
    """

    gmaps = googlemaps.Client(key='AIzaSyA3mWehI-WUOmQlTs7h5sV339EcL484DHQ')

    # Geocoding an address
    geocode_result = gmaps.geocode('Siera Leone & Liberia')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((7.493196470122287, -10.1953125))

    @expose('/map.html')
    @ observable(events.MapsController.mapping)
    def mapping(self, slug=None, **kwargs):
        pass
