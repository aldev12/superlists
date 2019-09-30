
from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    '''беспарольный серверный процессор аутентификации'''

    def authenticate(self, reauest, uid, *args, **kwargs):
        '''аутентифицировать'''
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except Token.DoesNotExist:
            return None
        except User.DoesNotExist:
            return User.objects.create(email=token.email)

    def get_user(self, email):
        '''получить пользователя'''
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
