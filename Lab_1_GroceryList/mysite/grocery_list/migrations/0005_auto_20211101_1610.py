# Generated by Django 3.2.9 on 2021-11-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0004_auto_20211101_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitems',
            name='Date_Purchased',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groceryitems',
            name='Item_Name',
            field=models.CharField(max_length=30),
        ),
    ]