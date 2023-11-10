from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, null=False, unique=False, blank=False)
    surname = models.CharField(max_length=50, null=False, unique=False, blank=False)
    gender = models.CharField(max_length=10, null=False, unique=False, blank=False)
    birthdate = models.DateField()
    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.gender} {self.birthdate}"

class Status(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True, blank=False, verbose_name="Название состояния")
    def __str__(self) -> str:
        return f'({self.id}){self.name}'
    class Meta:
        verbose_name_plural = 'Статусы товаров'

class Product(models.Model):
    name = models.CharField(max_length=300, null=False, unique=False, blank=False, verbose_name="Наименование товара", help_text="Картошка, помидор и т.п.")
    price = models.FloatField(verbose_name="Цена товара")
    quantity = models.FloatField(verbose_name="Количество товара")
    status = models.ForeignKey(Status, null=False, blank=False, on_delete=models.CASCADE,verbose_name="Состояние товара")
    photos = models.ManyToManyField("Photo", null=True, blank=True)
    comments = models.ManyToManyField("Comment", null=True, blank=True)
    def __str__(self) -> str:
        return f'({self.id}){self.name}-{self.price}, {self.quantity}, {self.status.name}'
    class Meta:
        verbose_name_plural = 'Продукты'

class Photo(models.Model):
    image = models.ImageField(upload_to='static/photos/', null=False, blank=False, verbose_name="Изображение товара")
    class Meta:
        verbose_name_plural = 'Фотографии продуктов'

class Comment(models.Model):
    content = models.TextField(verbose_name="Содержание комментария")
    def __str__(self) -> str:
        return f'({self.id}){self.content}'
    
    class Meta:
        verbose_name_plural = 'Комментарии'


# class Clothes(models.Model):
#     name = models.CharField(max_length=300, null=False, unique=False, blank=False, verbose_name="Наименование товара", help_text="Картошка, помидор и т.п.")
#     price = models.FloatField(verbose_name="Цена товара")
#     quantity = models.FloatField(verbose_name="Количество товара")
#     status = models.ForeignKey(Status, null=False, blank=False, on_delete=models.CASCADE,verbose_name="Состояние товара")
#     photos = models.ManyToManyField("Photo", null=True, blank=True)
#     comments = models.ManyToManyField("Comment", null=True, blank=True)
#     def __str__(self) -> str:
#         return f'({self.id}){self.name}-{self.price}, {self.quantity}, {self.status.name}'
#     class Meta:
#         verbose_name_plural = 'Одежда'