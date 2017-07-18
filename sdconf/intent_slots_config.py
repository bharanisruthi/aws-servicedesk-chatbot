#Intent Name

getTicketDetails = "GetOldTicketDetails"
logIssue = "LogIssue"
greeting= "Greeting"
hangUp = "HangUp"
closeTicket = "CloseTicket"
updateTicketDetails = "UpdateTicketDetails"
greetingSlots = {"greet":"Grret","greetBack":"GreetBack"}
getTicketDetailsSlots = {"emailId":"Email_ID","ticketId" :"Ticket_Id"}
updateTicketDetailsSlots = {"emailId":"Email_ID","ticketId" :"Ticket_Id","updateIssueDescription":"Updated_Description"}
closeTicketSlots = {"emailId":"Email_ID","ticketId" :"Ticket_Id"}
logIssueSlots = {"emailId":"Email_ID","issueDescription":"Issue_Description"}

#Slots
def getSlots(intentName):
    if intentName == getTicketDetails:
        return {
                    "Email_ID": None,
                    "Ticket_Id": None,
                }
    elif intentName == logIssue:
        return  {
                        "Email_ID": None,
                        "Issue_Description": None,
                }
    elif intentName == updateTicketDetails:
        return {
                    "Email_ID": None,
                    "Ticket_Id": None,
                    "Updated_Description":None,
                }

    elif intentName == greeting:
        return {
                    "Greet": None,
                    "Greetback":None,
                }
    elif intentName == closeTicket:
        return {
                    "Email_ID": None,
                    "Ticket_Id": None,
                }
    elif intentName == hangUp:
        return {}
    else:
        raise Exception("Intent not supported")
