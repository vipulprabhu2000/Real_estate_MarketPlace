from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Invalid Email address'))
        
    def create_user(self,username,first_name,last_name,email,password,**extra_fields):

        if not username:
            raise ValueError(_('You have to enter your username'))
        if not first_name:
            raise ValueError(_('You have to enter your username'))
        if not last_name:
            raise ValueError(_('You have to enter your username'))
       
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError('BASE User Account : Email is needed')

        user=self.model(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,first_name,last_name,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if email:
            email=self.email_validator(email)
            self.email_validator(email)
        else:
            raise ValueError("Admin Account requires Email address")

        user=self.create_user(username,first_name,last_name,email,password,**extra_fields)
        user.save(using=self._db)
        return user