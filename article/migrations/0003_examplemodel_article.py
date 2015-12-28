# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_examplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='article',
            field=models.ForeignKey(to='article.Article', null=True),
        ),
    ]
