from django.db import models
from ckeditor.fields import RichTextField
# from django.utils.html import strip_tags
# Create your models here.
class Post(models.Model):
    nom_poster = models.CharField(max_length = 64, default = "CyberCorpscm")
    titre = models.CharField(max_length = 255)
    sous_titre = models.CharField(max_length = 255)
    def __str__(self) -> str:
        return self.titre
    image_post = models.ImageField(upload_to='img/posts')
    date_post = models.DateField(auto_now_add=True)
    contenu_post = RichTextField(blank=True,null=True)
   

    
class Message(models.Model):
    nom = models.CharField(max_length = 70)
    def __str__(self) -> str:
        return self.nom
   
    telephone = models.IntegerField(unique = True,default='656565656')
    email = models.EmailField(max_length = 170,unique = True)
    contenu = models.CharField(max_length=255, default="tres interessant votre travaile Cybercoprs.cm continuer dans la meme lance")
    date = models.DateField(auto_now_add=True)