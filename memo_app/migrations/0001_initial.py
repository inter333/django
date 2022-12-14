# Generated by Django 2.1.7 on 2021-03-06 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, unique=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='memo',
            field=models.ForeignKey(db_column='memo_content', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='memo_app.Memo', to_field='content'),
        ),
    ]
