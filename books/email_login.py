from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class EmailLogin(object):
    def authenticate(self,username=None,password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except ObjectDoesNotExist:
            return None