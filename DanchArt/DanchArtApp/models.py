from django.db import models

# Create your models here.

class Foto(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/%Y/%m/%d')
    fecha = models.DateField()
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

  
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=15)
    pais = models.CharField(max_length=15)
    telefono = models.IntegerField( blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    x = models.CharField(max_length=30, blank=True, null=True)
    facebook = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre 

class Base(models.Model):
    nombre = models.CharField(max_length=30)
    base = models.ForeignKey(Foto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

class Cuadro(models.Model):
    nombre = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cuadro = models.ForeignKey(Foto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, blank=True, null=True)
    base = models.ForeignKey(Base, on_delete=models.PROTECT, blank=True, null=True)
    fisico = models.BooleanField()

    def __str__(self):
        return self.nombre 


class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    entrega = models.BooleanField()