from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import CustomUserCreationForm,CustomUserChangeForm


# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering=["email"]
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=User
    list_display=["pkid","id","email","username","first_name","last_name","is_staff","is_active"]
    list_display_links=["id","email"]
    list_filter=["email","username","first_name","last_name","is_staff","is_active"]
    fieldsets=(
        (
            _("login credentials"),
            {
                "fields":("email","password",)
            }
        ),
        (
            _("Personal Information"),
            {
                "fields":("username","first_name","last_name",)
            }
        ),
        (
            ("Permissions and Groups"),
            {
                "fields":("is_active","is_staff","is_super","groups","user_permissions")
            }
        ),
        (
            _("Important Dates"),
            {
                "fields":("last_login","date_joined",)
            }
        )
        
    )
    add_fieldsets=(
            (None,
             {
                 "classes":("wide",),
                 "fields":("email","password1","password2","is_staff","is_active"),
             })
        )
    search_fields=["email","first_name","last_name","username"]

admin.site.register(User,UserAdmin)
