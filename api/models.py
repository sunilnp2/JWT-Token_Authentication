from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

# create usermanager
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, password2 = None):
        """
        Creates and saves a User with the given  username, profile and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            # profile = profile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username, profile and password.
        """
        user = self.create_user(
            username = username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# create user 

class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    profile = models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin