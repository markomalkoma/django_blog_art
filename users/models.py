from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	image = models.ImageField(default='renaissance-fresco-painting.jpg', upload_to='profile_pics')

	def __str__(self):
		return "profile {}".format(self.user.username )

'''		
	
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		
		img = Image.open(self.image.path)
		
		if img.height>300 or img.width>300:
			output_size = (300, 300)
			img.thumbnail(output_size)

		
		if img.height>img.width:
			dim=img.width
			img=img.crop((0, 0, dim, dim))
			img.save(self.image.path)

		elif img.height<img.width:
			dim=img.height
			img=img.crop((0, 0, dim, dim))
			img.save(self.image.path)

		else:
			img.save(self.image.path)

'''