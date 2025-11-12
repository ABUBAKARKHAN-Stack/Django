from django.db import models
from django.utils import timezone


class ChaiVerity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KI", "KIWI"),
        ("EL", "ELAICHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now())
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name
