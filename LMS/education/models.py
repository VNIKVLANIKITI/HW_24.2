from django.db import models
class lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(max_length=255, verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson_previews/')
    link_video = models.URLField()

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField(max_length=255, verbose_name='Описание')
    lessons = models.ManyToManyField(lesson, related_name='courses')  # Связь ManyToMany с Уроком

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


