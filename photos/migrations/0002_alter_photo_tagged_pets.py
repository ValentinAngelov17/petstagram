# Generated by Django 4.2.2 on 2023-06-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet'),
        ),
    ]