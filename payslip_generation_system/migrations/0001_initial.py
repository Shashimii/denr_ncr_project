# Generated by Django 4.2 on 2025-05-07 07:20

from django.db import migrations, models
import django.db.models.deletion
import payslip_generation_system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_no', models.CharField(default='Unknown', max_length=255)),
                ('fullname', models.CharField(default='Unknown', max_length=255)),
                ('date_hired', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('educational_attainment', models.CharField(blank=True, choices=[('High School', 'High School'), ('College', 'College'), ('Postgraduate', 'Postgraduate'), ('Others', 'Others')], max_length=50, null=True)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('fund_source', models.CharField(max_length=100)),
                ('tax_declaration', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('eligibility', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='EmployeeAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=payslip_generation_system.models.generate_filename)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='payslip_generation_system.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Adjustment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Income', 'Income'), ('Deduction', 'Deduction')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField()),
                ('computation', models.CharField(max_length=50)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20, null=True)),
                ('cutoff', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd')], max_length=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payslip_generation_system.employee')),
            ],
            options={
                'verbose_name': 'Adjustment',
                'verbose_name_plural': 'Adjustments',
            },
        ),
    ]
