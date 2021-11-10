# Generated by Django 3.2.8 on 2021-11-10 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('dob', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('address', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('is_student', models.BooleanField(default=True)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to='profile_pics')),
            ],
        ),
    ]
