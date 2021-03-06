from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from app.models import *
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.mail import send_mail

def index(request):
	if ('user_id' in request.session):
		currentUser = User.objects.get(id = request.session['user_id'])
		context = {'currentUser': currentUser}
		return render(request, 'app/index.html', context)
	else:
		return render(request, 'app/index.html')

# View orders page
def viewOrders(request):
	if ('user_id' in request.session):
		currentUser = User.objects.get(id = request.session['user_id'])
		orderList = Order.objects.all()
		context = {'currentUser': currentUser, 'orderList': orderList}
		return render(request, 'app/orders.html', context)
	else:
		return render(request, 'app/logInPage.html')

#Create account page with form
def createAccount(request, blankErrorStatus):
	#Determines the error based on the URL string
	if blankErrorStatus == "True":
		context = {'error': False, 'blankErrorStatus': True}
	else:
		context = {'error': False, 'blankErrorStatus': False}
	return render(request, 'app/createAccount.html', context)

def sendRunnerMessage(runner, client, order):
	clientName = client.firstName
	clientNumber = client.phoneNumber
	runnerEmail = runner.email
	food = order.food
	restaurant = order.restaurant
	location = order.user_location
	body = "You are getting %s from %s for delivery to %s at %s. You can reach them at %s" % (food, restaurant, clientName, location, clientNumber)
	send_mail("CMYum Order", body, 'cmyumorders@gmail.com', [runnerEmail], fail_silently=False)

def sendClientMessage(runner, client, order):
	runnerName = runner.firstName
	runnerNumber = runner.phoneNumber
	clientEmail = client.email
	body = "%s is getting your order! You can reach them at %s" % (runnerName, runnerNumber)
	send_mail("CMYum Order", body, 'cmyumorders@gmail.com', [clientEmail], fail_silently=False)

def removePunctuation(s):
	result = ''
	for char in s:
		if char in '0123456789':
			result += char
	return result

#Adds a user account to the database
def addUser(request):
	firstName = request.POST['First_Name']
	lastName = request.POST['Last_Name']
	username = request.POST['username']
	phoneNumber = request.POST['phoneNumber']
	emailAddress = request.POST['email']
	password = request.POST['password']

	phoneNumber = removePunctuation(phoneNumber)

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
		if (firstName == "" or lastName == "" or username == "" or password == ""
			or phoneNumber == "" or emailAddress == ""):
			blankErrorStatus = True
			###Probably not the best idea to redirect here, use render with context instead
			return HttpResponseRedirect(reverse('app:createAccount', args=(blankErrorStatus,)))
		else:
			#If the username does not exist and all fields are filled, creates a
			#new User instance
			newUser = User(firstName = firstName, lastName = lastName,
				username = username, hashedPassword = encryptedPassword, phoneNumber = phoneNumber,
				email = emailAddress)
			newUser.save()
			return HttpResponseRedirect(reverse('app:index'))


# Creates order page with form
def createOrder(request, blankErrorStatus):
	#Determines the error based on the URL string
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		if blankErrorStatus == "True":
			context = {'user': user, 'error': False, 'blankErrorStatus': True}
		else:
			context = {'user': user, 'error': False, 'blankErrorStatus': False}
		return render(request, 'app/createOrder.html', context)
	else:
		return render(request, 'app/logInPage.html')

#Adds an order to the database
def addOrder(request):
	# Figure out how to get username (username not in form)
	# For now, enter username manually
	user = User.objects.get(id = request.session['user_id'])
	restaurant = request.POST['Restaurant']
	food = request.POST['Food']
	# Gets time from django.utils timezone
	time = timezone.now()
	user_location = request.POST['Location']
	runner = -1
	#createAccount page
	#If one or more fields are blank, raises an error
	if (restaurant == "" or food == "" or user_location == ""):
		blankErrorStatus = True
		###Probably not the best idea to redirect here, use render with context instead
		return HttpResponseRedirect(reverse('app:createOrder', args=(blankErrorStatus,)))
	else:
		#If the username does not exist and all fields are filled, creates a
		#new User instance
		newOrder = Order(user = user, restaurant = restaurant, food = food, time = time,
						 user_location = user_location, runner = runner)
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
		currentUser = User.objects.get(username = username)
		if (encryptedPassword == currentUser.hashedPassword):
			request.session['user_id'] = currentUser.id
			return HttpResponseRedirect(reverse('app:index'))
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

def claimOrder(request, id):
	currentOrder = Order.objects.get(id=id)
	runner = User.objects.get(id = request.session['user_id'])
	sendRunnerMessage(runner, currentOrder.user, currentOrder)
	sendClientMessage(runner, currentOrder.user, currentOrder)
	currentOrder.delete()
	return HttpResponseRedirect(reverse('app:viewOrders'))

#Allows users to log out of their session
def logout(request):
	#Deketes the cookie storing user info
	del request.session['user_id']
	return HttpResponseRedirect(reverse('app:index'))
