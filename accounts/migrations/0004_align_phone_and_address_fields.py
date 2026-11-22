from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_address_options_remove_address_label_choice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.RenameField(
            model_name='address',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.RenameField(
            model_name='address',
            old_name='line_1',
            new_name='line1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='line_2',
            new_name='line2',
        ),
    ]
