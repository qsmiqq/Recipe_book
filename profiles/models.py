from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    nickname = models.CharField(max_length=50, verbose_name='Nickname')
    email = models.EmailField(verbose_name='Mail', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')

    def __str__(self):
        return f'{self.pk} - {self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'