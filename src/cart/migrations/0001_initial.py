# Generated by Django 3.2.5 on 2023-10-12 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=3, default='100', max_digits=5)),
                ('paid_status', models.BooleanField(default=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('product_status', models.BooleanField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivery')], default='process', max_length=50)),
            ],
            options={
                'verbose_name': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanlity', models.IntegerField(default=0)),
                ('invoices_no', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, default='100', max_digits=5)),
                ('image', models.CharField(max_length=200)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
            options={
                'verbose_name': 'Cart',
            },
        ),
    ]
