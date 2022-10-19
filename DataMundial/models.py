from distutils.command.upload import upload
from django.db import models
from django.db.models import Model, DateTimeField
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.conf import settings





# Create your models here.


class selecciones(models.Model):
    seleccion = models.CharField(max_length=20)
    jug_nombre = models.CharField(max_length=20)
    jug_apellido = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)

class grupo(models.Model):
    letra = models.CharField(max_length=1)
    seleccion = models.CharField(max_length=40)

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to= 'avatares', null = True, blank = True)

# class ConcursoBlog(models.Model):
#     comentario_blog = models.CharField(max_length=30)
#     autor = models.CharField(max_length=30) 
#     def __str__(self):
#         return f"Comentario:{self.comentario_blog} - Autor:{self.autor}"

# class BlogConcurso(models.Model):
#     comentario = models.CharField(max_length=200)
#     autor = models.CharField(max_length=200)


# class MyModel(models.Model):
#     fullname = models.TextField()
#     mobile_number = models.CharField(max_length = 200)

# class MyModelBlog(models.Model):
#     comentario = models.TextField(max_length = 400)
#     pais = models.CharField(max_length = 200)


class MyModelBlog(models.Model):
    comentario = models.TextField(max_length = 400)
    pais = models.CharField(max_length = 200)
    user= models.CharField(max_length = 200)
    # user= models.CharField(max_length = 400)
    # user= models.ForeignKey(User, on_delete = models.PROTECT)    
    # user= models.ForeignKey(User, on_delete = models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now(), blank=True)

class Details(models.Model):
    comentario = models.TextField(max_length = 400)
    pais = models.CharField(max_length = 200)
    user= models.CharField(max_length = 200)
    # user= models.CharField(max_length = 400)
    # user= models.ForeignKey(User, on_delete = models.PROTECT)   
    # user= models.ForeignKey(User, on_delete = models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now(), blank=True)


class Mensaje(models.Model):
    useror = models.CharField(max_length=30)
    userdest = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=400)
    def __str__(self):
        return f"Usuario_Origen:{self.useror} - Usuario_Destino:{self.userdest} - Mensaje:{self.mensaje}"


class Message(models.Model):
        author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
        content = models.TextField()
        timestamp = models.DateTimeField(default=timezone.now) #todo: timezone fix?
    
        def __str__(self):
            return self.author.username
    
        def last_10_messages(self):
            return Message.objects.order_by("-timestamp").all()[:10] # only load last 10 msgs from DB