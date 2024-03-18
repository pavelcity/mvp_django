from django.db import models

# Create your models here.


class Article(models.Model):
    rubric = models.CharField(max_length=255, verbose_name='Рубрика')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    cover_photo = models.ImageField(upload_to='photos/articles/')
    article_head_photo = models.ImageField(upload_to='photos/articles/')
    short = models.TextField(blank=True, verbose_name='Короткое описание')
    text = models.TextField(blank=True, verbose_name='Текст')
    sort = models.CharField(max_length=4, blank=True, verbose_name='Сортировка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    catarticle = models.ForeignKey('Categoryarticle', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']



class Categoryarticle(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория article')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статей'
        ordering = ['name']


