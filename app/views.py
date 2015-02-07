from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from app.models import *
from django.core.urlresolvers import reverse
from django.utils import timezone


def index(request):
	return render(request, 'app/index.html')

#Create account page with form
def createAccount(request, blankErrorStatus):
	#Determines the error based on the URL string
	if blankErrorStatus == "True":
		context = {'error': False, 'blankErrorStatus': True}
	else:
		context = {'error': False, 'blankErrorStatus': False}
	return render(request, 'app/createAccount.html', context)

#Adds a user account to the database
def addUser(request):
	firstName = request.POST['First_Name']
	lastName = request.POST['Last_Name']
	username = request.POST['username']
	password = request.POST['password']
	#Password is encrypted by hashing
	encryptedPassword = hashlib.sha1(password).hexdigest()
	#If username already exists in database, then raises an error in the
	#createAccount page
	try:
		User.objects.get(username = username)
		context = {'error': True, 'blankErrorStatus': False}
		return render(request, 'app/createAccount.html', context)
	except:
		#If one or more fields are blank, raises an error
		if (firstName == "" or lastName == "" or username == "" or password == ""):
			blankErrorStatus = True
			###Probably not the best idea to redirect here, use render with context instead
			return HttpResponseRedirect(reverse('app:createAccount', args=(blankErrorStatus,)))
		else:
			#If the username does not exist and all fields are filled, creates a
			#new User instance
			newUser = User(firstName = firstName, lastName = lastName,
				username = username, hashedPassword = encryptedPassword)
			newUser.save()
			return HttpResponseRedirect(reverse('app:index'))


# Creates order page with form
def createOrder(request, blankErrorStatus):
	#Determines the error based on the URL string
	if blankErrorStatus == "True":
		context = {'error': False, 'blankErrorStatus': True}
	else:
		context = {'error': False, 'blankErrorStatus': False}
	return render(request, 'app/createOrder.html', context)

#Adds an order to the database
def addOrder(request):
	# Figure out how to get username (username not in form)
	# For now, enter username manually
	username = request.POST['Username']
	restaurant = request.POST['Restaurant']
	food = request.POST['Food']
	# Gets time from django.utils timezone
	time = timezone.now()
	user_location = request.POST['Location']
	#createAccount page
	#If one or more fields are blank, raises an error
	if (username == "" or restaurant == "" or food == "" or user_location == ""):
		blankErrorStatus = True
		###Probably not the best idea to redirect here, use render with context instead
		return HttpResponseRedirect(reverse('app:createOrder', args=(blankErrorStatus,)))
	else:
		#If the username does not exist and all fields are filled, creates a
		#new User instance
		newOrder = Order(user = username, restaurant = restaurant, food = food, time = time,
						 user_location = user_location)
		newOrder.save()
		return HttpResponseRedirect(reverse('app:index'))

#Log In page with form
def logInPage(request):
	context = {'error': False}
	return render(request, 'app/logInPage.html', context)

#Verifies that the username and password entered are in the database
def logInAuthenticate(request):
	username = request.POST['username']
	password = request.POST['password']
	encryptedPassword = hashlib.sha1(password).hexdigest()
	try:
		#If username is in database and matches with password, go to
		#userProfile page
		currentUser = User.objects.get(username_text = username)
		if (encryptedPassword == currentUser.hashedPassword_text):
			request.session['user_id'] = currentUser.id
			return HttpResponseRedirect(reverse('app:userProfile'))
		#If username is in database but password is incorrect, raises an error
		#in the logInPage
		else:
			context = {'error': True, 'username': username}
			return render(request, 'app/logInPage.html', context) 
	except:
		#If username is not in database, raises an error in the
		##logInPage
		context = {'error': True}
		return render(request, 'app/logInPage.html', context) 

#Allows users to log out of their session
def logout(request):
	#Deketes the cookie storing user info
	del request.session['user_id']
	return HttpResponseRedirect(reverse('app:index'))
