from django.db import models


class UserTelegram(models.Model):
    number = models.CharField("Номер", max_length=100)
    username = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.username


class Manga(models.Model):
    name = models.CharField("Название", max_length=250)
    description = models.TextField('Описание')
    date = models.DateField('Дата добавления')

    def __str__(self):
        return self.name


class ImagesManga(models.Model):
    image = models.ImageField("Изображение")
    manga = models.ForeignKey(Manga, verbose_name='Название манги', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manga.name} - {self.image}"


class Tags(models.Model):
    name = models.CharField("Тэг", max_length=100)

    def __str__(self):
        return self.name


class TagsManga(models.Model):
    tags = models.ForeignKey(Tags, verbose_name='Тэг', on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)


class Author(models.Model):
    username = models.CharField('Имя', max_length=100)

    def __str__(self):
        return self.username


class AuthorManga(models.Model):
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)


class PrimarySource(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name


class PrimarySourceManga(models.Model):
    primary_source = models.ForeignKey(PrimarySource, verbose_name="Первоисточник", on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)


class Like(models.Model):
    manga = models.ForeignKey(Manga, verbose_name='Манга', on_delete=models.CASCADE)
    user = models.ForeignKey(UserTelegram, verbose_name='Пользователь', on_delete=models.CASCADE)
    date = models.DateField('Дата')