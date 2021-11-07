from django.db import models
# this is for images
from io import BytesIO
# from pillow installed we import image
from PIL import Image
# To easy the work of creating thumbnails
from django.core.files import File
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering =('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """This function helps to get the path of a given category easily"""
        return f'/{self.slug}/'
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=255, blank=True,null=True)
    price= models.DecimalField(max_digits=6,decimal_places=0)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_created = models.DateField(auto_now_add=True)
    
    
    class Meta:
            ordering =('-date_created',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # """This function helps to get the path of a given product based on the category easily"""
        return f'/{self.category.slug}/{self.slug}/'
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        return ''
    def get_thumbnail(self):
        if self.thumbnail:
             return 'http://127.0.0.1:8000'+self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save
                return 'http://127.0.0.1:8000'+self.thumbnail.url

            else:
                return ''
    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=70)
        thumbnail = File(thumb_io,name=image.name)
        return thumbnail


       