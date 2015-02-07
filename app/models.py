from django.db import models

#User model represents user accounts
class User(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	username = models.CharField(max_length = 50)
	hashedPassword = models.CharField(max_length = 50)
	phoneNumber = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)

	#Represents User as a string when it is called
	def __str__(self):
		return "%s, %s, %s" % (self.firstName_text, self.lastName_text, self.username_text)

	#Orders the Users in the database by first name
	class Meta:
		ordering = ('firstName_text',)

