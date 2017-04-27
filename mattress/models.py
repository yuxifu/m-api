from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from localflavor.us.models import PhoneNumberField
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField

import datetime


class OnlineRetailer(models.Model):
    """
    Model representing online retailer such as https://casper.com/
    """
    name = models.CharField(max_length=128,
                            help_text="Enter name of the retailer such as Casper")
    web = models.CharField(max_length=128,
                           help_text="Enter web address of the retailer such as casper.com")
    description = models.TextField(
        max_length=1024, help_text="Enter a brief description of the retailer")
    email = models.EmailField()
    phone = PhoneNumberField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class UsAddress(models.Model):
    """
    Model representing an US postal address
    """
    address_1 = models.CharField("Address", max_length=128)
    address_2 = models.CharField("Address Cont'd", max_length=128, blank=True)
    city = models.CharField("City", max_length=64)
    state = USStateField("State")
    zip_code = USZipCodeField("Zip Code", max_length=5)

    def __str__(self):
        """
        """
        return '%s %s, %s, %s %s' % (self.address_1, self.address_2,
                                     self.city, self.state, self.zip_code)


class Buyer(models.Model):
    """
    Model representing the buyer of the mattress
    """
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.ForeignKey(
        'UsAddress', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        """
        return self.full_name


class MattressSize:
    TWIN = 'TWIN'
    TWIN_XL = 'TWIN_XL'
    FULL = 'FULL'
    QUEEN = 'QUEEN'
    KING = 'KING'
    CAL_KING = 'CAL_KING'
    MATTRESS_SIZES = (
        (TWIN, 'Twin'),
        (TWIN_XL, 'Twin XL'),
        (FULL, 'Full'),
        (QUEEN, 'Queen'),
        (KING, 'King'),
        (CAL_KING, 'Cal King'),
    )


class RMA(models.Model):
    """
    Model representing a RMA from the retailer
    """
    retailer = models.ForeignKey(
        'OnlineRetailer', on_delete=models.CASCADE, null=False)
    rma_number = models.CharField('RMA#', max_length=128)
    order_number = models.CharField('Order#', max_length=128)
    invoice_number = models.CharField('Invoice#', max_length=128)
    order_date = models.DateField()
    return_authorized = models.BooleanField()
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    size = models.CharField(max_length=1, choices=MattressSize.MATTRESS_SIZES,
                            help_text='Mattress size')
    buyer = models.ForeignKey(
        'Buyer', on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        """
        Returns the url to access a particular RMA instance.
        """
        return reverse('rma-detail', args=[str(self.id)])

    def __str__(self):
        """
        """
        return '%s (%s)' % (self.retailer, self.rma_number)


class Return(models.Model):
    """
    Model representing a return initiated by the user
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    initiate_date = models.DateField(default=datetime.date.today)
    container_shipped = models.BooleanField(default=False)
    container_delivered = models.BooleanField(default=False)
    kit_shipped = models.BooleanField(default=False)
    kit_delivered = models.BooleanField(default=False)
    container_back_shipped = models.BooleanField(default=False)
    container_back_delivered = models.BooleanField(default=False)
    kit_back_shipped = models.BooleanField(default=False)
    kit_back_delivered = models.BooleanField(default=False)
    retailer = models.ForeignKey(
        'OnlineRetailer', on_delete=models.CASCADE, null=False)
    rma_number = models.CharField('RMA#', max_length=128)
    order_number = models.CharField('Order#', max_length=128)
    invoice_number = models.CharField('Invoice#', max_length=128)
    order_date = models.DateField()
    return_authorized = models.BooleanField()
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    size = models.CharField(max_length=1, choices=MattressSize.MATTRESS_SIZES,
                            help_text='Mattress size')
    buyer = models.ForeignKey(
        'Buyer', on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        """
        Returns the url to access a particular return instance.
        """
        return reverse('return-detail', args=[str(self.id)])

    def __str__(self):
        """
        """
        return '%s (%s)' % (self.user, self.id)
