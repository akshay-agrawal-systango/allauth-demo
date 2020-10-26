
from allauth.account.adapter import DefaultAccountAdapter 
from django.forms import ValidationError
from django.conf import settings

class UsernameMaxAdapter(DefaultAccountAdapter): 
    def clean_username(self, username): 
        if len(username) > settings.USERNAME_MAX_LENGTH: 
            raise ValidationError('Max username length is eight charactors') 

        # For other default validations. 
        return DefaultAccountAdapter.clean_username(self, username) 