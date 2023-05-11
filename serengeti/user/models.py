from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def _create_user(self, username, password, **kwargs):
        user = self.model(
            username = username,
            **kwargs
        )
        user.set_password(password) #암호화 하려면 이렇게 써야함
        user.save()
    def create_user(self, username, password, **kwargs):
        self._create_user(username, password, **kwargs)
    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    #Password는 이미 적용되어있음
    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )

    create_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser
    