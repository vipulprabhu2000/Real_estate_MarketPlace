import logging
from django.db.models.signals import post_save
from RealEstate.settings.base import AUTH_USER_MODEL
from .models import Profile
from django.dispatch import receiver


logger=logging.getLogger(__name__)


@receiver(post_save,sender=AUTH_USER_MODEL)
def Create_User_Profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=AUTH_USER_MODEL)
def Save_User_Profile(sender,instance,**kwargs):
    instance.save()
    logger.info(f"{instance}'s Profile Created")
