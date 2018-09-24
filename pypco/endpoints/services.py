"""Endpoints for PCO services.

To add additional endpoints, simply add additional classes
subclassing the ServicesEndpoint class.
"""

#pylint: disable=C0304,R0903,C0111,C0321

from .base_endpoint import BaseEndpoint

# The the services endpoint
class ServicesEndpoint(BaseEndpoint): pass

# All objects on the services endpoint
class AttachmentTypes(ServicesEndpoint): pass
class EmailTemplates(ServicesEndpoint): pass
class Folders(ServicesEndpoint): pass
class Media(ServicesEndpoint): pass
class People(ServicesEndpoint): pass
class Series(ServicesEndpoint): pass
class ServiceTypes(ServicesEndpoint): pass
class Songs(ServicesEndpoint): pass
class TagGroups(ServicesEndpoint): pass
class Teams(ServicesEndpoint): pass
