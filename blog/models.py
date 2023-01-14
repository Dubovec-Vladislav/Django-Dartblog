from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Post')
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)  # Не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')  # По умолчанию ноль
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='get_category')
    # releated_name - Название связи постов с категориями (У category появиться свойство posts)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    # releated_name - У класса Post появится свойство Teg, а у класса Tag появится свойство Post

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты(ов)"
        ordering = ['-created_at']
