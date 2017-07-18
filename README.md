# aws-servicedesk-chatbot
Project for submission to the 2017 AWS Chatbot Competition

SDBot is designed to assist the enterprise service desks. This bot can be used to do tasks like log issue/ update issue done by SD teams with much ease and convenience. It can be used to increase the efficiency of Service Desk by delegating the simple tasks to the bot. 



We have assumed generic enterprise/firm for the test and development purposes. Our idea was to make it simple to be integrated. 



The bot can be used to do the following operations
log an issue
get ticket details
Update ticket details
Close ticket

Prerequisites:
Valid email id
Add the email id to slackbot
Add the email id as a valid user in dynamo db table, CustomerDetails


Technology Stack:

AWS Lambda
AWS Lex
AWS SES(Simple Email Service)
AWS DynamoDB

