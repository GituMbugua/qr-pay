from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid

# Create your models here.
class QR(models.Model):
    route = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    code = models.ImageField(upload_to='qr_codes', blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def save(self, *args, **kwargs):
            link =  'http://192.168.100.246:8000/payment/'+self.uuid.hex
            # link =  'http://192.168.100.246:8000/api/v1/online/lipa'
            # link = 'http://192.168.100.246:8000/api/v1/index'
            qrcode_img = qrcode.make(link)       
            canvas = Image.new('RGB', (450, 450), 'white')    
            canvas.paste(qrcode_img)
            fname = f'qr_code-'+str(self.uuid.hex)+'.png'
            # fname = f'qr_code-{self.item}.png'
            buffer = BytesIO() 
            canvas.save(buffer,'PNG')
            self.code.save(fname, File(buffer), save=False) 
            canvas.close()
            super().save(*args, **kwargs)