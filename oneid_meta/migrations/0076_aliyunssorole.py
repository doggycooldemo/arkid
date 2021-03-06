# Generated by Django 2.2.10 on 2020-07-24 07:37

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0075_auto_20200612_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliyunSSORole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('role', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='阿里云SSO角色分配')),
                ('session_duration', models.IntegerField(blank=True, default=900)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='aliyun_sso_role', to='oneid_meta.User', verbose_name='用户')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
