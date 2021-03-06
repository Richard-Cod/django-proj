# Generated by Django 3.2.9 on 2021-12-06 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bon',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bon',
            name='ownerName',
            field=models.CharField(default='default', max_length=255, verbose_name='ownerName'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bon',
            name='adresse',
            field=models.CharField(max_length=255, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='adresseComplement',
            field=models.CharField(max_length=255, verbose_name="Complément d'adresse"),
        ),
        migrations.AlterField(
            model_name='bon',
            name='autoNumerotation',
            field=models.BooleanField(default=False, verbose_name='Numérotation automatique'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='bdcLocality',
            field=models.CharField(max_length=255, verbose_name='Localité / Ville'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='commercialContact',
            field=models.CharField(max_length=255, verbose_name='Contact commercial'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='date',
            field=models.DateField(max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='bon',
            name='editionDomTom',
            field=models.BooleanField(default=False, verbose_name='Edition DOM/TOM '),
        ),
        migrations.AlterField(
            model_name='bon',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email (obligatoire)'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='encart',
            field=models.CharField(max_length=255, verbose_name='Encart'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='firstDeploy',
            field=models.DateField(verbose_name='Première mise en ligne programmée le'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='nbDeployOrdered',
            field=models.CharField(choices=[('3', 3), ('6', 6), ('9', 9), ('12', 12)], max_length=255, verbose_name='Nombre de mise en ligne commandées'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='nonReductibleCommand',
            field=models.BooleanField(default=False, verbose_name='Commande non reconductible '),
        ),
        migrations.AlterField(
            model_name='bon',
            name='observations',
            field=models.TextField(verbose_name='Observations'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='phoneOrFax',
            field=models.CharField(max_length=255, verbose_name='Téléphone / Fax'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='portable',
            field=models.CharField(max_length=255, verbose_name='Portable'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='postalCode',
            field=models.CharField(max_length=255, verbose_name='Code postal'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='priceHT',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Montant H.T. (par mise en ligne)'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='representedBy',
            field=models.CharField(max_length=255, verbose_name='Représentée par'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='sector',
            field=models.CharField(max_length=255, verbose_name="Secteur d'activité"),
        ),
        migrations.AlterField(
            model_name='bon',
            name='socialReason',
            field=models.CharField(max_length=255, verbose_name='Raison sociale'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='totalHT',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total H.T. (de la campagne)'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='totalTTC',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total T.T.C. (par mise en ligne)'),
        ),
        migrations.AlterField(
            model_name='bon',
            name='website',
            field=models.URLField(verbose_name='Site web'),
        ),
    ]
