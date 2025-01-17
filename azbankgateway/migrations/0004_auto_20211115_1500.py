# Generated by Django 3.2 on 2021-11-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("azbank", "0003_bank_bank_choose_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bank",
            name="bank_type",
            field=models.CharField(
                choices=[
                    ("BMI", "BMI"),
                    ("SEP", "SEP"),
                    ("ZARINPAL", "Zarinpal"),
                    ("IDPAY", "IDPay"),
                    ("ZIBAL", "Zibal"),
                    ("BAHAMTA", "Bahamta"),
                    ("MELLAT", "Mellat"),
                ],
                max_length=50,
                verbose_name="Bank",
            ),
        ),
    ]
