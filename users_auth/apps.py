"""
The module contains configuration class for app user_auth
"""
from django.apps import AppConfig


class UsersAuthConfig(AppConfig):
    """
    This is the configuration class for app user_auth
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_auth'
