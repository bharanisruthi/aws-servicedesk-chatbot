import json
import re
import boto3
from sdconf import  messages_config
from email.utils import parseaddr

print('Loading function')


def verify_email(sender, email, client):
    verifyRecepient = client.verify_email_address(EmailAddress=email)
    # verifyDomain = client.verify_domain_identity(Domain='gmail.com',)
    verifySender = client.verify_email_address(EmailAddress=sender)
    if verifyRecepient is not None:
        return "Unable to verify Recepient Email Address"
    else:
        return True


def validateEmail(email, text, ticketid,identifier):
    # email = event["currentIntent"]["slots"]["Email_Id"]
    #email = 'sruthi223@gmail.com'
    sender = "bharanisruthi17@gmail.com"
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        print('Bad Syntax')
    else:
        print(match)
        # awsregion = "us-west-2"
        client = boto3.client('ses')
        #verifyEmail = verify_email(sender, email, client)
        if True:
            subject = "Ticket Status Update for "+ str(ticketid)
            htmlbody = messages_config.emailMessage + "for the ticket id " +str(ticketid)
            textbody = None
            if identifier == "logIssue":
            # The email body for recipients with non-HTML email clients.
                textbody = "Ticket ID: "+ticketid +"has been logged for the issue, "+text
            elif identifier == "updateIssue" :
                textbody = "Ticket ID: "+ticketid +"has been updated with the information, "+text
            else:
                textbody = None
            # The character encoding for the email.
            charset = "UTF-8"

            # Try to send the email.
            try:
                # Provide the contents of the email.
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            email,
                        ],
                    },
                    Message={
                        'Body': {
                            'Html': {
                                'Charset': charset,
                                'Data': htmlbody,
                            },
                            'Text': {
                                'Charset': charset,
                                'Data': textbody,
                            },
                        },
                        'Subject': {
                            'Charset': charset,
                            'Data': subject,
                        },
                    },
                    Source=sender,
                )
            # Display an error if something goes wrong.
            except Exception as e:
                print("Error: ", e)
            else:
                print("Email sent!")
