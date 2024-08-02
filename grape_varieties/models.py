from django.db import models
from django.urls import reverse
from django.core.validators import (MinLengthValidator)
from django.utils.text import slugify


class AboutGrape(models.Model):
    name_rus = models.CharField(max_length=50)
    about_grape = models.TextField(validators=[MinLengthValidator(1)])

    def __str__(self):
        return f"{self.name_rus}"


class Grape(models.Model):
    name_eng = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    area = models.IntegerField(null=True)
    image = models.FileField(upload_to='grape_gallery', blank=True)
    about_grape = models.ForeignKey(AboutGrape, on_delete=models.PROTECT, null=True, related_name="info_about_grape")
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='colors')
    tags = models.ManyToManyField('TagGrape', blank=True, related_name='tags')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_eng)
        super(Grape, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("to_info_about_grapes", args=[self.slug])


    def __str__(self):
        return f"{self.name_eng} ({self.about_grape.name_rus})"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})


class TagGrape(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})

# ------------------------------------------------------------------------------------------

class History(models.Model):
    story_name = models.CharField(max_length=200)
    story = models.ForeignKey("AboutHistory", on_delete=models.PROTECT, related_name='once_history')
    tags = models.ManyToManyField('TagHistory', blank=True, related_name='tags')
    image = models.FileField(upload_to='grape_gallery', blank=True)
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)


class AboutHistory(models.Model):
    description = models.CharField(max_length=200)
    the_story = models.TextField(validators=[MinLengthValidator(1)])


class TagHistory(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_url(self):
        return reverse("history_tag", kwargs={"tag_slug": self.slug})

# ------------------------------------------------------------------------------------------





