from django.db import models
from django.urls import reverse
# Create your models here.

class Mebel(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Введите название мебели',
                             verbose_name='Название мебели')
    type = models.ForeignKey('Type', on_delete=models.CASCADE,
                              help_text='Выберите вид мебели',
                              verbose_name='Вид мебели'
                              )
    izd = models.ForeignKey('Izdatel', on_delete=models.CASCADE,
                               help_text='Выберите издателя мебели',
                               verbose_name='Издатель мебели'
                               )
    summary = models.TextField(max_length=1000,
                               help_text='Введите краткое описание мебели',
                               verbose_name='Описание мебели'
                               )
    size = models.CharField(null=True,
                               help_text='Введите ширина*высота*глубина в сантиметрах')
    color = models.ForeignKey('Color', on_delete=models.CASCADE,
                              help_text='Выберите цвет мебели',
                              verbose_name='Цвет мебели',
                              null=True)
    price = models.DecimalField(
        max_digits=10,decimal_places=2,
        help_text='Введите цену в рублях',verbose_name='Цена',
        null=True,blank=True
    )
    image = models.URLField(
        max_length=500,
        help_text='Введите URL изображения',
        verbose_name='URL изображения',
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(
        default=0,
        help_text='Введите количество товара в наличии',
        verbose_name='Количество'
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('mebel-detail', args=[str(self.id)])

class Type(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите вид мебели',
                            verbose_name='Вид мебели')
    def __str__(self):
        return self.name

class Izdatel(models.Model):
    name = models.CharField(max_length=100,
                                  help_text='Введите название издателя',
                                  verbose_name='Название издателя')
    geo = models.CharField(max_length=120,
        help_text='Введите место регистрации издателя',
        verbose_name='Место регистрации издателя',
        null=True, blank=True
    )
    def __str__(self):
        return self.name

class Instance(models.Model):
    mebel = models.ForeignKey('Mebel', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text='Введите инвентарный номер мебели',
                               verbose_name='Инвентарный номер мебели')
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text='Изменить состояние экземпляра мебели')
    due_back = models.DateField(null=True, blank=True,
                                help_text='Введите конец срока статуса',
                                verbose_name='Дата окончания статуса')

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.status)

class Status(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите статус экземпляра мебели',
                            verbose_name='Статус экземпляра мебели')
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название цвет',
                            verbose_name='Название цвета')
    def __str__(self):
        return self.name

