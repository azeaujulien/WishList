from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100, null=False)
    date = models.DateField(null=False)

    def __str__(self):
        return self.name + ' : ' + str(self.date.strftime("%d/%m/%Y"))
