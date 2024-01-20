from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=6)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.first_name}, {self.number_of_guests} guests on {self.reservation_date}'


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')
    inventory = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.name} : {str(self.price)}'
