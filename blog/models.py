from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300,verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')


    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
            
    def __str__(self):
        return self.title    



"""
Lógica de acceso a la base de datos.

"""
