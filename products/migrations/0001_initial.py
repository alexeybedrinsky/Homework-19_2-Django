# Generated by Django 5.1 on 2024-09-03 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование",
                        max_length=50,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Краткое описание",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование",
                        max_length=50,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Краткое описание",
                        max_length=255,
                        null=True,
                        verbose_name="Краткое описание",
                    ),
                ),
                (
                    "image_preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение товара",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Превью товара",
                    ),
                ),
                (
                    "purchase_price",
                    models.CharField(
                        help_text="Цена за покупку",
                        max_length=50,
                        verbose_name="Стоимость",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Дата занесения в БД",
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Дата последнего изменения в БД",
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Категория товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="products.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category"],
            },
        ),
    ]
