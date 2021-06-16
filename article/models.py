from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Kateqoriya")
    
    def __str__(self):
        return self.name

class About(models.Model):
    name = "About"
    content = RichTextField(verbose_name="Mətn")
    image = models.FileField(blank=True,null=True,verbose_name="Şəkil")

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ManyToManyField(Category,verbose_name="Kateqoriya",blank=True,null=True)
    title = models.CharField(max_length=50,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Mətn")
    image = models.FileField(blank=True,null=True,verbose_name="Şəkil")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_content = models.CharField(max_length = 1000,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_name = models.CharField(max_length=200,verbose_name="Ad",blank=True,null=True)
    
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
