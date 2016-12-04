from django.db import models

# Create your models here.

class Publisher (models.Model) :
    """data for Publisher ."""
    name            = models.CharField  (max_length = 30)
    address         = models.CharField  (max_length = 50)
    city            = models.CharField  (max_length = 20)
    state_provice   = models.CharField  (max_length = 20)
    country         = models.CharField  (max_length = 20)
    website         = models.URLField   ()

    def __str__(self):
        "return String Object"
        return self.name

    class Meta:
        ordering = ['name']


class Author (models.Model) :
    """data for Author ."""
    first_name      = models.CharField  (max_length = 15)
    last_name       = models.CharField  (max_length = 15)
    email           = models.EmailField (blank      = True, verbose_name = 'e-mail')

    def __str__(self):
        "return String Object"
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta :
        ordering = ['first_name', 'last_name']



class Book (models.Model):
    """data for Book ."""
    title               = models.CharField  (max_length = 100)
    publication_date    = models.DateField  (blank= True, null=True)

    authors             = models.ManyToManyField    (Author)
    publisher           = models.ForeignKey         (Publisher)

    def __str__(self):
        "return String Object"
        return self.title

    class Meta :
        ordering = ['publication_date']
