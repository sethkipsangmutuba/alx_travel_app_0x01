from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    guest_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.guest_name} booking for {self.listing.title}"
