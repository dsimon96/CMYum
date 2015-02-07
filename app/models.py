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
		return "%s, %s, %s" % (self.firstName, self.lastName, self.username)

	#Orders the Users in the database by first name
	class Meta:
		ordering = ('firstName',)

# Order model for placed orders
class Order(models.Model):
	user = models.ForeignKey(User)
	restaurant = models.CharField(max_length = 50)
	food = models.CharField(max_length = 50)
	time = models.DateTimeField('time placed')
	user_location = models.CharField(max_length = 50)
	runner = models.IntegerField()
	



