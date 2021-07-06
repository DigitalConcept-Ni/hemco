from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


class User(AbstractUser):
    documento = models.CharField(max_length=2,null=True, blank=True)

    # def toJSON(self):
    #     item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
    #     if self.last_login:
    #         item['last_login'] = self.last_login.strftime("%Y-%m-%d %H:%M:%S")
    #     item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
    #     return item

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.set_password(self.password)
    #     else:
    #         user = User.objects.get(pk=self.pk)
    #         if user.password != self.password:
    #             self.set_password(self.password)
    #     super().save(*args, **kwargs)