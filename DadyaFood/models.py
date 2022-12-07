from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='имя')
    card_number = models.IntegerField(verbose_name='номер карточки')

    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='имя')
    position = models.CharField(max_length=30, verbose_name='должность')

    class Meta:
        db_table = 'Worker'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, verbose_name='ингридиент')
    extra_price = models.IntegerField(verbose_name='надбавка')

    class Meta:
        db_table = 'Ingredient'
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингриденты'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20, verbose_name='наименование бдюда')
    start_price = models.IntegerField(verbose_name='цена')
    ingredient = models.ManyToManyField(Ingredient, related_name='mill', through='Order')

    class Meta:
        db_table = 'Food'
        verbose_name = 'хавчик'
        verbose_name_plural = 'хавчикс'

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='время заказа')

    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.food.name