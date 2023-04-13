# softwareAssesment3
The TicketData class is defined with several class variables including default_response, default_status, starting_number, total_ticket, open_tickets, and tickets. The __init__ method is defined to initialize instance variables for staffid, name_of_creater, email, description, response_to_ticket, status, and ticket_number. The show_highlevel_ticket_details is defined as a static method to display the total number of tickets created, resolved, and remaining tickets.

The main function is defined to execute the ticketing system's functionalities using a while loop that continually prompts the user to select an option from the menu. The options are 1-7, and the corresponding functionality is executed based on the user's input.

Option 1 allows the user to create a ticket by entering the staff ID, name of the creator, email, and description. A new instance of the TicketData class is created with the provided input, and the ticket number is generated.

Option 2 allows the user to reopen a closed ticket by entering the ticket number. If the ticket is found and marked as closed, the ticket is reopened, and the ticket statistics are updated.

Option 3 allows the user to respond to a ticket by entering the ticket number. If the ticket is found, the user can either enter a response or if the ticket's description is "Password Change," a new password is automatically generated, and the ticket is marked as resolved.

Option 4 displays all tickets' details, including the ticket number, creator name, staff ID, email, description, response, and status.

Option 5 displays the details of a specific ticket by entering the ticket number.

Option 6 displays ticket statistics, including the total number of tickets created, resolved, and remaining.

Option 7 terminates the program.
