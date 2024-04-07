# Generated by Django 5.0.3 on 2024-03-24 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PollsQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('question_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('SC', 'Single Choice'), ('TX', 'Text')], max_length=2)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.polls')),
            ],
        ),
    ]
