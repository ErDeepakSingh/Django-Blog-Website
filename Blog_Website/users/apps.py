from django.apps import AppConfig
from . import signals

class UsersConfig(AppConfig):
    name = 'users'

    # def ready(self):
    #     import users.signals