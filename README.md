# AWS-ServiceDesk-Chatbot
Project for submission to the 2017 AWS Chatbot Competition https://www.youtube.com/watch?v=oQfebs3lfuc

SDBot is designed to assist the enterprise service desks. This bot can be used to do tasks like log issue/ update issue done by SD teams with much ease and convenience. It can be used to increase the efficiency of Service Desk by delegating the simple tasks to the bot. 



We have assumed generic enterprise/firm for the test and development purposes. Our idea was to make it simple to be integrated. 



The bot can be used to log an issue,get ticket details,Update ticket details and Close ticket

Prerequisites:
Valid email id,
Add the email id to slackbot,
Add the email id as a valid user in dynamo db table CustomerDetails and email id must be verified in AWS SES


Technology Stack:

AWS Lambda,
AWS Lex,
AWS SES(Simple Email Service),
AWS DynamoDB,
Slack API,
Boto3 API

