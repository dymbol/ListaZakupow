# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name=b'Data utworzenia')),
                ('active', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BuyListElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=1)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='jednostka_miary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='element',
            name='typeof',
            field=models.ForeignKey(to='manager.ElementType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buylistelement',
            name='element',
            field=models.ForeignKey(to='manager.Element'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buylistelement',
            name='jednostka',
            field=models.ForeignKey(to='manager.jednostka_miary'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buylistelement',
            name='lista',
            field=models.ForeignKey(to='manager.BuyList'),
            preserve_default=True,
        ),
    ]
