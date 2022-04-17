from django.db import models


# Create your models here.
class Item(models.Model):
    """ Set up item model and put name and done items in database """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """ Return name as string """
        return self.name
