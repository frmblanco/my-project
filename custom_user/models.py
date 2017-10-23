
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name,):
        now = timezone.now()
        if not email:
            raise ValueError('The email is required to create this user')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, is_staff=True,
                          is_active=True, is_superuser=False, date_joined=now, last_login=now,)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name,):
        user = self.create_user(email, password, first_name, last_name,)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()