"""PCO Giving models.

Generated by pypco_generator tool. Manual changes not recommended.
"""

#pylint: disable=C0321,R0903,C0111

from .base_model import BaseModel

# The base Giving model
class GivingModel(BaseModel): pass

# Giving Models
class Batch(GivingModel): 
    """None"""
    ENDPOINT_NAME='batches'

class BatchGroup(GivingModel): 
    """None"""
    ENDPOINT_NAME='batch_groups'

class Designation(GivingModel): 
    """None"""
    ENDPOINT_NAME='donations'

class DesignationRefund(GivingModel): 
    """None"""
    ENDPOINT_NAME='donations'

class Donation(GivingModel): 
    """None"""
    ENDPOINT_NAME='donations'

class Fund(GivingModel): 
    """None"""
    ENDPOINT_NAME='funds'

class Label(GivingModel): 
    """None"""
    ENDPOINT_NAME='labels'

class PaymentMethod(GivingModel): 
    """None"""
    ENDPOINT_NAME='people'

class PaymentSource(GivingModel): 
    """None"""
    ENDPOINT_NAME='payment_sources'

class Person(GivingModel): 
    """None"""
    ENDPOINT_NAME='people'

class RecurringDonation(GivingModel): 
    """None"""
    ENDPOINT_NAME='recurring_donations'

class RecurringDonationDesignation(GivingModel): 
    """None"""
    ENDPOINT_NAME='recurring_donations'

class Refund(GivingModel): 
    """None"""
    ENDPOINT_NAME='donations'
