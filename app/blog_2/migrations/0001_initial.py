# Generated by Django 4.2.7 on 2023-11-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('full_name', models.CharField(max_length=81)),
                ('age', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Yazar',
                'verbose_name_plural': 'Yazarlar',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='blogs')),
                ('note', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(help_text='Bloqun yazarını seçin!', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog_2.author', verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Bloq',
                'verbose_name_plural': 'Bloqlar',
            },
        ),
    ]