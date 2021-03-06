# Generated by Django 3.0.6 on 2020-05-24 14:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'a_city',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_status', models.SmallIntegerField(choices=[(1, 'active'), (0, 'inactive')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_shop.City')),
            ],
            options={
                'db_table': 'a_customer',
            },
        ),
        migrations.CreateModel(
            name='Mayor',
            fields=[
                ('mayor_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mayor_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'a_mayor',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_shop.Customer')),
            ],
            options={
                'db_table': 'a_order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customers', models.ManyToManyField(through='a_shop.Order', to='a_shop.Customer')),
            ],
            options={
                'db_table': 'a_product',
            },
        ),
        migrations.CreateModel(
            name='OrderAttachment',
            fields=[
                ('order_attachment_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('attachment', models.FileField(upload_to='order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_shop.Order')),
            ],
            options={
                'db_table': 'order_attachment',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_shop.Product'),
        ),
    ]
