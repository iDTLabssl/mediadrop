from pylons import request, response, tmpl_context as c
from pylons.controllers.util import abort
from sqlalchemy import orm

from mediacore.lib.base import BaseController
from mediacore.lib.decorators import (expose, observable)
from mediacore.plugin import events

import logging
log = logging.getLogger(__name__)


class MapController(BaseController):
    """
        Map Controller
    """

    @expose('/map.html')
    @ observable(events.MapsController.mapping)
    def mapping(self, slug=None, **kwargs):
        pass
