from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,)
    name = models.SlugField(max_length=200, db_index=True)  # Наименование товара
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)  # Фото товара
    description = models.TextField(blank=True)  # Описание товара
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)  # Цена товара (кол-ва цифр всего, кол-во цифр после запятой)
    available = models.BooleanField(default=True)  # Наличие товара (есть/нет)
    created = models.DateTimeField(auto_now_add=True)  # Дата создания товара
    updates = models.DateTimeField(auto_now=True)  # Дата изменения товара

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
