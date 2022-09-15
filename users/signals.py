from unicodedata import name
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
@receiver(post_save,sender=User)
def saved(sender,instance,created,**kwargs):
    if created or None:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name or user.username
        )
        name = user.first_name or user.username
        subject = 'welcome to my site'
        message = 'hallo {} selamat datang di website gw asw <3'.format(name)

        send_mail (
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )

@receiver(post_delete,sender=Profile)
def deleted(sender,instance,**kwargs):
    user = instance.user
    if user is not None:
        user.delete()
    else:
        None

        