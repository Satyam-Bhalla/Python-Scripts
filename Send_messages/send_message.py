from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "ACb0048d8170647e345609653d88e43596" # Your Account SID from www.twilio.com/console
auth_token  = "6485c9e2d025dc7fb3af38789fb26905"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="Testing",
        to="+917508018938",    # Replace with your phone number
        from_="+14152372003") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
