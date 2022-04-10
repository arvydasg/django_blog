from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog_post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    # content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=False)

    # Tell how you want the info to be sorted and named in
    # django-admin panel. No need to re-migrate
    class Meta:
        ordering = ['-created']
        # verbose_name = 'blet'
        # krc jeigu uncomment sita below me, kai meginu posta istrinti - gaunu error. zjbs.
        # verbose_name_plural = ['Blogo postai']

    # Tell django how you want the title of the Blog_post item to be
    # represented in django-admin panel. No need to re-migrate
    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    # content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images', default='static/images/placeholder.png')

    class Meta:
        ordering = ['title']
        # verbose_name = 'blet'
        # verbose_name_plural = ['Projektauskai']

    def __str__(self):
        return self.title
