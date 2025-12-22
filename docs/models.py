import random
from django.db import models

def gen_pin():
    return f"{random.randint(0, 999999):06d}"

class Document(models.Model):
    file = models.FileField(upload_to='docs/')
    pin = models.CharField(max_length=6, default=gen_pin, editable=False)
    qr = models.ImageField(upload_to='qr/', blank=True)
    pdf_image = models.ImageField(upload_to='pdf_preview/', blank=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doc #{self.id}"

