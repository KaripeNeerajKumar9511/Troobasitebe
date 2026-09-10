from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0002_blogpost"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsletterSubscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("subscribed", "Subscribed"),
                            ("unsubscribed", "Unsubscribed"),
                        ],
                        default="subscribed",
                        max_length=20,
                    ),
                ),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
                ("unsubscribed_at", models.DateTimeField(blank=True, null=True)),
                ("message_id", models.CharField(blank=True, max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-subscribed_at", "-id"],
            },
        ),
    ]
