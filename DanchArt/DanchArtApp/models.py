from django.db import models

# Create your models here.

class Foto(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/%Y/%m/%d')
    fecha = models.DateField()
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)

  
class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    telefono = models.IntegerField()
    instagram = models.CharField(max_length=15)
    x = models.CharField(max_length=15)
    facebook = models.CharField(max_length=15)

class Base(models.Model):
    nombre = models.CharField(max_length=30)
    base = models.ForeignKey(Foto, on_delete=models.CASCADE)

class Cuadro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cuadro = models.ForeignKey(Foto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    fisico = models.BooleanField()


class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    entrega = models.BooleanField()