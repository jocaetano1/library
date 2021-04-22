from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='authors')

    def __str__(self):
        return self.user.get_full_name()
    
    def save(self, *args, **kwargs):
        if not self.id and self.nickname == None:
            self.nickname = self.generate_nickname()
        super().save(*args, **kwargs)

    def generate_nickname(self):
        first_name = getattr(self.user, 'first_name')
        last_name = getattr(self.user, 'last_name')
        if first_name and last_name:
            nickname = f'@{first_name}{last_name}'
        else:
            nickname = f'@{self.user.username}'
        return nickname