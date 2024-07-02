# Generated by Django 5.0.4 on 2024-06-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueprint', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blueprint',
            options={'ordering': ['changed_at']},
        ),
        migrations.RemoveField(
            model_name='blueprint',
            name='file',
        ),
        migrations.AddField(
            model_name='blueprint',
            name='file_b3d',
            field=models.FileField(blank=True, null=True, upload_to='blueprints/file'),
        ),
        migrations.AddField(
            model_name='blueprint',
            name='file_dwg',
            field=models.FileField(blank=True, null=True, upload_to='blueprints/file'),
        ),
        migrations.AddField(
            model_name='blueprint',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blueprint',
            name='file_pdf',
            field=models.FileField(blank=True, null=True, upload_to='blueprints/pdf'),
        ),
    ]