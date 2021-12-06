# Generated by Django 3.2.9 on 2021-12-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=30)),
                ('autoNumerotation', models.BooleanField(default=False)),
                ('nonReductibleCommand', models.BooleanField(default=False)),
                ('editionDomTom', models.BooleanField(default=False)),
                ('socialReason', models.CharField(max_length=255)),
                ('representedBy', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('adresseComplement', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phoneOrFax', models.CharField(max_length=255)),
                ('portable', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=255)),
                ('firstDeploy', models.DateField()),
                ('nbDeployOrdered', models.CharField(choices=[(3, 3), (6, 6), (9, 9), (12, 12)], max_length=255)),
                ('encart', models.CharField(max_length=255)),
                ('bdcLocality', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('priceHT', models.DecimalField(decimal_places=2, max_digits=19)),
                ('totalTTC', models.DecimalField(decimal_places=2, max_digits=19)),
                ('totalHT', models.DecimalField(decimal_places=2, max_digits=19)),
                ('commercialContact', models.CharField(max_length=255)),
                ('observations', models.TextField()),
            ],
        ),
    ]
