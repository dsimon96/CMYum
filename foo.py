from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc80ca9e0300eca6696d3ef736b07bfa6"
auth_token  = "add2bd12a41a84bb45fbcfa271464ae5"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I got the Twilio working",
    to="+14082163052",    # Replace with your phone number
    from_="+12673092588") # Replace with your Twilio number
print message.sid