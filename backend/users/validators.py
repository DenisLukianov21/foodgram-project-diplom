from django.core.exceptions import ValidationError


def vaidate_subscribing(user):
    if user == user:
        raise ValidationError('Нельзя подписываться на самого себя!')
