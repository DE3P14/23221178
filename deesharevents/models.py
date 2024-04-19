from django.db import models

# Create your models here.
class deesharevents(models.Model):
    VENUE_CHOICES = [
        ('Dublin 08', 'Dublin 08'),
        ('Dublin 10', 'Dublin 10'),
        # Add more venue choices as needed
    ]

    venue = models.CharField(max_length=100, choices=VENUE_CHOICES)
    image = models.ImageField(upload_to='event_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alcoholic = models.BooleanField(default=False)
    select_date = models.DateField()
    expected_guests = models.IntegerField(default=0)