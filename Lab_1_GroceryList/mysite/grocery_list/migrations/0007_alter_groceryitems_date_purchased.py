# Generated by Django 3.2.9 on 2021-11-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0006_alter_groceryitems_date_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitems',
            name='Date_Purchased',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]