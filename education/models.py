from django.db import models

from users.models import User

NULLABLE = {'blank': 'True', 'null': 'True'}


class Course(models.Model):
    title_course = models.CharField(max_length=50, verbose_name='название курса')
    image_course = models.ImageField(upload_to='course/', verbose_name='картинка курса', **NULLABLE)
    description_course = models.TextField(verbose_name='описание курса')

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title_course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=50, verbose_name='название урока')
    description_lesson = models.TextField(verbose_name='описание урока')
    image_lesson = models.ImageField(upload_to='lesson/', verbose_name='картинка урока', **NULLABLE)
    lesson = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='ссылка на курс', **NULLABLE)
    date_create = models.DateField(verbose_name='дата выхода урока', auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title_lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    course_subscription = models.ForeignKey(Course, verbose_name='курс в подписке', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.course_subscription}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
