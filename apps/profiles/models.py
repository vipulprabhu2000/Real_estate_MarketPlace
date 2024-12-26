from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampUUIDModel
from phonenumber_field.modelfields import PhoneNumberField


User=get_user_model()

# Create your models here.

class Gender(models.TextChoices):
    MEN="Male",_("Male")
    FEMALE="FEMALE",_("FEMALE")
    OTHER="OTHER",_("OTHER")



class Profile(TimeStampUUIDModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Profile")
    phone_number=PhoneNumberField(verbose_name=_("Phone Numer"),max_length=12,default="+914567894567")
    about_me=models.CharField(verbose_name=_("About me"),max_length=250,default="Add something in the about me")
    profile_photo=models.ImageField(default="/default.png",verbose_name=_("Profile Picture"))
    license=models.CharField(verbose_name=_("License details"),max_length=20,null=True,blank=True)
    gender=models.CharField(verbose_name=_("Gender"),max_length=20,default=Gender.OTHER,choices=Gender.choices)
    country=CountryField(verbose_name=_("Country"),default="India",blank=False,null=False)
    city=CountryField(verbose_name=_("City"),default="Mumbai",blank=False,null=False)
    is_buyer=models.BooleanField(verbose_name=_("Buyer"),help_text=_("Are you a Buyer?"),default=False)
    is_seller=models.BooleanField(verbose_name=_("Seller"),help_text=_("Are you a Seller"),default=False)
    top_agent=models.BooleanField(verbose_name=_("Agent"), help_text=_("Top Agent"),default=False)
    rating=models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    num_reviews=models.IntegerField(null=True,default=0,blank=True,verbose_name=_("Number Reviews"))

    def __str__(self):
        return f"{self.user.username}'s Profile"

    


