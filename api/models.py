from django.db import models

class Entrada(models.Model):
    tipo = models.CharField(max_length=10, choices=[
        ('Restaurant', 'Restaurant'),
        ('Pub', 'Pub'),
        ('Otro', 'Otro')
    ])
    detalle = models.TextField()
    mapa = models.CharField(max_length=350)
    foto1 = models.CharField(max_length=550,default="None")
    foto2 = models.CharField(max_length=550,default="None")
    foto3 = models.CharField(max_length=550,default="None")
    autor = models.CharField(max_length=50,default="None")
    calificacion = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ])
    class Meta:
        db_table = 'entrada'
