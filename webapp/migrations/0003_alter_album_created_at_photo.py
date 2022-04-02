# Generated by Django 4.0.3 on 2022-04-02 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_alter_album_options_alter_album_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_pics', verbose_name='Фотография')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')),
                ('isPrivate', models.BooleanField(default=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='webapp.album', verbose_name='Альбом')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'Photos',
            },
        ),
    ]