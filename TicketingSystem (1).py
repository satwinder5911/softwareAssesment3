class TicketData:    #ticket class
    #all static variables
    default_response = "Not Yet Provided" #default reponse
    default_status = "Open" #default status
    starting_number = 2000 #default number
    total_ticket = 0#number of total ticket
    open_tickets = 0 #number of all open ticket
    ticket_to_resolve = 0#ticket to resolve
    tickets=[]#total ticket list
    
    def __init__(self, staffid, name_of_creater, email, description):    #constructor   
        self.staffid = staffid
        self.name_of_creater = name_of_creater
        self.email = email
        self.description = description
        self.response_to_ticket = TicketData.default_response
        self.status = TicketData.default_status        
        self.ticket_number = TicketData.total_ticket + TicketData.starting_number
        TicketData.open_tickets += 1 #increment count to one
        TicketData.total_ticket += 1#increment count to one

    @staticmethod
    def show_highlevel_ticket_details(): #static method for show all information of ticket count.
        print("\nTotal Tickets Created: ", TicketData.total_ticket) 
        print("Total Tickets Resolved: ", TicketData.ticket_to_resolve)
        print("Total Tickets To Solve: ", TicketData.open_tickets)

        

def main():
    while True:
        #show menu to user
        print("\n+-+-+-+-+-+-+-+-+-+ Welcome To This System +-+-+-+-+-+-+-+-+-")
        print("Please choose an options below--\n1. Create a ticket\n2. Reopen a ticket\n3. Respond to a ticket")        
        print("4. Display all tickets")
        print("5. Display detail of one ticket using Ticket number")
        print("6. Display ticket statistics")
        print("7. Exit\nEnter your choice: ")
        input_data  = int(input());#ask user to input
        
        if input_data == 1:            
            staffid = input("Please Enter Staff_ID: ") #display message on console and ask input
            name = input("Please Enter Creator Name: ")#display message on console and ask input
            email = input("Please Enter Email: ")#display message on console and ask input
            description = input("Please Enter Description: ")#display message on console and ask input
            ticket = TicketData(staffid, name, email, description) #create object of ticket class
            print("Ticket Created Successfully with ticket_number ", ticket.ticket_number)#display message on console
            TicketData.tickets.append(ticket)#append all ticket to ticket list
        elif input_data == 2:
            ticket_number = int(input("\nPlease Enter Ticket Number: "))#display message on console and ask input
            for i in TicketData.tickets:
                if i.ticket_number == ticket_number and i.status == "Closed":   #check ticket is close and same as asked ticket                 
                    i.status ="Reopen" #change status to reopen
                    TicketData.open_tickets +=1#increment count to one
                    TicketData.ticket_to_resolve -=1#decrement count to one
                    print("Reopened Success!!")#display message on console
                    break
        elif input_data == 3:
            ticket_number = int(input("\nPlease Enter Ticket Number: "))#display message on console and ask input
            for i in TicketData.tickets:
                if i.ticket_number == ticket_number:
                    if i.description.lower() == "Password Change".lower():
                        i.response_to_ticket = "New Password : "+ i.staffid[:2]+i.name_of_creater[:3]
                        i.status = "Closed"
                        TicketData.open_tickets -= 1#decrement count to one
                        TicketData.ticket_to_resolve += 1#increment count to one
                        print("The ticket is resolved automatically because of new password request")
                        break
                    else:
                        response = input("Please enter response")
                        i.response_to_ticket = response
                        i.status = "Closed"
                        TicketData.open_tickets -= 1#decrement count to one
                        TicketData.ticket_to_resolve += 1#increment count to one
                        print("The ticket Has successfully added a response")
                        break
                    
        elif input_data == 4:
            for i in TicketData.tickets:
                print("\nTicket Number: ", i.ticket_number) #display message on console
                print("Ticket Creator: ", i.name_of_creater) #display message on console
                print("Staff ID: ", i.staffid) #display message on console
                print("Email Address: ", i.email) #display message on console
                print("Description: ", i.description) #display message on console
                print("Response: ", i.response_to_ticket) #display message on console
                print("Ticket Status: ", i.status)#display message on console
        elif input_data == 5:
            ticket_number = int(input("\nPlease Enter Ticket Number: "))#display message on console and ask input
            for i in TicketData.tickets:
                if i.ticket_number == ticket_number:
                    print("\nTicket Number: ", i.ticket_number)#display message on console
                    print("Ticket Creator: ", i.name_of_creater)#display message on console
                    print("Staff ID: ", i.staffid)#display message on console
                    print("Email Address: ", i.email)#display message on console
                    print("Description: ", i.description)#display message on console
                    print("Response: ", i.response_to_ticket)#display message on console
                    print("Ticket Status: ", i.status)#display message on console
                    break
        elif input_data ==6:
            TicketData.show_highlevel_ticket_details()
        elif input_data == 7:
            print("Thank you for using this system")#display message on console
            break 
        else:
            print("Invalid Choice. Please try again.") #display message on console


if __name__ == "__main__":
    main()
