"""PCO Webhooks models.

Generated by pypco_generator tool. Manual changes not recommended.
"""

#pylint: disable=C0321,R0903,C0111

from .base_model import BaseModel

# The base Webhooks model
class WebhooksModel(BaseModel): pass

# Webhooks Models
class AvailableEvent(WebhooksModel): 
    """An event supported by webhooks"""
    ENDPOINT_NAME='available_events'

class Delivery(WebhooksModel): 
    """None"""
    ENDPOINT_NAME='subscriptions'

class Event(WebhooksModel): 
    """None"""
    ENDPOINT_NAME='subscriptions'

class Subscription(WebhooksModel): 
    """None"""
    ENDPOINT_NAME='subscriptions'
