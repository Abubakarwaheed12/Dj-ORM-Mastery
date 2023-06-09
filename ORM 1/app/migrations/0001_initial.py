# Generated by Django 3.2.13 on 2023-04-27 09:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Techers',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(default=10, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)])),
                ('fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('url', models.SlugField()),
                ('books', models.CharField(choices=[('eng', 'eng'), ('URDU', 'URDU'), ('MATH', 'MATH'), ('PHY', 'PHY')], max_length=200)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
