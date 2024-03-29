# Generated by Django 5.0.1 on 2024-01-22 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='documents/')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('document_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentDocumentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.component')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.documenttype'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.location')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.locationtype')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location'),
        ),
        migrations.AddField(
            model_name='component',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.manufacturer'),
        ),
        migrations.AddField(
            model_name='component',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.package'),
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.component')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.component')),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_location', to='app.location')),
                ('source_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_location', to='app.location')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier'),
        ),
    ]
