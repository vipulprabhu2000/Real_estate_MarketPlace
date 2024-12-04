from .base import *


DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_NAME"),
        'USER':env("POSTGRES_USER"),
        'HOST':env("POSTGRES_HOST"),
        'PASSWORD':env("POSTGRES_PASSWORD"),
        'PORT':env("POSTGRES_PORT"),
    }
}
