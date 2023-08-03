from django.contrib import admin
from .models import Rental, BookRental, Book


class RentalsAdmin(admin.ModelAdmin):
    list_display = ('Name_of_rental', 'Type_of_rental', 'Total_no_of_units', 'Rent', 'Image_url', 'Name', 'Deposit',
                    'Location', 'Electricity', 'Water', 'Floors',
                    'Walls', 'Roof', 'Bathroom', 'Image_url1')


admin.site.register(Rental, RentalsAdmin),
admin.site.register(BookRental),
admin.site.register(Book),
