"""from django.contrib import admin"""



# Register your models here.
from django.contrib import admin
from .models import Post # models.py da tanmladgmz Post modelini admin.py dosyamza buraya ekledik

admin.site.register(Post) # Modelimizi admin sayfasinda gorunur yapmak icin