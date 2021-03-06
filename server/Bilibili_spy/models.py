from django.db import models


class Book(models.Model):
    qs_id = models.CharField(max_length=50)
    an_id = models.CharField(max_length=50)

    def __str__(self):
        return '%s: %s' % (self.qs_id, self.an_id)

    def toJSON(self):
        return {
            self.qs_id: self.an_id,
        }
