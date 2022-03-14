# Generated by Django 3.2 on 2022-03-14 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('number_of_tables', models.IntegerField(default=1)),
                ('font', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=2)),
                ('detail', models.TextField()),
                ('payment_intent', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('completed', 'Completed')], default='processing', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.place')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='core.category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.place')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='core.place'),
        ),
    ]
