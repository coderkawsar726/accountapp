# Generated by Django 5.1.3 on 2024-12-17 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('ammount', models.IntegerField()),
                ('currency', models.CharField(choices=[('SAR', 'SAR'), ('BDT', 'BDT')], default='SAR', max_length=3)),
                ('remark', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('ammount', models.IntegerField()),
                ('currency', models.CharField(choices=[('SAR', 'SAR'), ('BDT', 'BDT')], default='SAR', max_length=3)),
                ('remark', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('note', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('', 'Select...'), ('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=12, max_length=15)),
                ('year', models.CharField(choices=[('', 'Select...'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030')], default=2024, max_length=15)),
                ('main_salary', models.IntegerField()),
                ('food_bill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(blank=True, max_length=50)),
                ('client_contact', models.CharField(max_length=26)),
                ('client_note', models.CharField(max_length=100)),
                ('client_NID', models.CharField(blank=True, max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_client', to='mainapp.borrow')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_amount', models.IntegerField()),
                ('remark', models.CharField(max_length=150)),
                ('return_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_return_client', to='mainapp.borrow')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ReturnLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_amount', models.IntegerField()),
                ('remark', models.CharField(max_length=150)),
                ('return_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_return_client', to='mainapp.loan')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
