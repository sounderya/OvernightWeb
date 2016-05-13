from django.db import models

# Create your models here.


class HotelInfo(models.Model):
    HotelID = models.TextField(db_column='hotelID', blank=True, primary_key=True)  # Field name made lowercase.
    Destination=models.TextField(db_column='destination', blank=True, null=True)  # Field name made lowercase.
    Area=models.TextField(db_column='area', blank=True, null=True)  # Field name made lowercase.
    HotelName=models.TextField(db_column='HotelName', blank=True, null=True)  # Field name made lowercase.
    HotelAddress=models.TextField(db_column='address', blank=True, null=True)  # Field name made lowercase.   HotelAmenities(JSON)
    HotelAmens= models.TextField(db_column='hotelAmenities', blank=True, null=True)  # Field name made lowercase.
    HotelServices=models.TextField(db_column='hotelServices', blank=True, null=True)  # Field name made lowercase.
    HotelRoomTypes=models.TextField(db_column='hotelRoomTypes', blank=True, null=True)  # Field name made lowercase.(JSON)
    PriceByDate=models.TextField(db_column='PriceByDate', blank=True, null=True)  # Field name made lowercase.(From)
    HotelPictures=models.TextField(db_column='HotelPictures', blank=True, null=True)  # Field name made lowercase.(HTML)

    class Meta:
        managed = True
        db_table = 'HotelInfo'
