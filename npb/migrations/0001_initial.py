# Generated by Django 2.0.2 on 2018-02-09 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Paste UUID')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Removed paste')),
                ('removal_reason', models.CharField(blank=True, default='', max_length=512, verbose_name='Removal reason')),
                ('is_private', models.BooleanField(default=False, verbose_name='Private paste')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('edited_on', models.DateTimeField(auto_now=True, verbose_name='Edited on')),
                ('expire_on', models.DateTimeField(null=True, verbose_name='Expiration date')),
                ('author_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name="Author's IP address")),
                ('lexer', models.CharField(blank=True, max_length=128, verbose_name='Lexer')),
                ('title', models.CharField(blank=True, default='', max_length=256, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
