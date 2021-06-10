from django.db import models

from Auth.models import Account


class Wish(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(Account, related_name='creator', null=False, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username + " : " + self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=False)
    wish = models.ForeignKey(Wish, null=False, on_delete=models.CASCADE)
    taker = models.ForeignKey(Account, related_name='taker', null=True, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        return ''
