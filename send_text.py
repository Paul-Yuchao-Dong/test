__author__ = 'Paul YC Dong'

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACdaa94ee7eb753ce16679a83ab4851e0b"
auth_token = "c72c454578762405d43bcf97198e2f8c"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(to="+85267941690", from_="+85258087558", body="test Huston")


# My sweet little valentine, I love you~