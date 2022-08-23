# Generated by Django 4.0 on 2021-12-12 05:31

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('line_username', models.CharField(max_length=150, verbose_name='line_username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='メールアドレス')),
                ('sns_icon_url', models.URLField(blank=True, verbose_name='アイコン(SNS連携)')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_info_grade_number', models.IntegerField(choices=[(3, '3年'), (2, '2年'), (1, '1年')], default=True, verbose_name='学年')),
                ('user_info_class_number', models.PositiveSmallIntegerField(verbose_name='クラス番号')),
                ('user_info_student_number', models.PositiveSmallIntegerField(verbose_name='出席番号')),
                ('user_info_student_name', models.CharField(max_length=50, verbose_name='名前')),
                ('user_info_body_temperature', models.CharField(max_length=10, verbose_name='体温')),
                ('is_run_code', models.IntegerField(choices=[(1, '実行する'), (0, '停止する')], default=True, verbose_name='実行するか')),
                ('user_info_created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_info_updated_at', models.DateTimeField(auto_now_add=True)),
                ('user_info_last_run_at', models.DateTimeField(blank=True, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name_plural': 'ユーザー情報',
            },
        ),
    ]