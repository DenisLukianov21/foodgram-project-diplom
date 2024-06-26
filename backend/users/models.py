from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from .validators import vaidate_subscribing


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    email = models.EmailField('Почта', max_length=254, unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(User, related_name='subscriber',
                             verbose_name="Подписчик",
                             validators=[vaidate_subscribing],
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='subscribing',
                               verbose_name="Автор",
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        constraints = (UniqueConstraint(fields=['user', 'author'],
                       name='unique_subscription'),)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Подписка {self.user} на {self.author}'
