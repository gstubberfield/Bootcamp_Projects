"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.

class Email:

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False # Defaults to email as not been read

    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.

# Create function that creates an email object 
# with email address, subject line and contents
# and stores in the inbox list

def populate_inbox(email_address, subject_line, email_content):
    email = Email(email_address, subject_line, email_content)
    inbox.append(email)

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
      
inbox = []

# Create three sample emails

populate_inbox("r.geller@friends.com", "Check this out", "Today was great!")
populate_inbox("r.green@friends.com", "Here we are", "What's happening today")
populate_inbox("j.tribbiani@friends.com", "How you doin?", "This happened today")

# Create function that loops the inbox and prints each email subject line 
# with corresponding index number.
# Use enumerate function

def list_emails(inbox):
    print("\nThe subject lines of the inbox are:")
    for i, Email in enumerate(inbox):
       print(f"{i} {Email.subject_line}")
list_emails(inbox)

# Create function to display a selected email and contents then set to has_been_read
# Allow user to input an index
# Add try/except in case of index error and user has inputted an invalid index

def read_email(index):
    try:
        number_emails = len(inbox)
        chosen_email = int(input(f"\nWhich number email, between 0 to {number_emails-1}, would you like to read? "))
        Email = inbox[chosen_email]
        Email.mark_as_read()
        print(f"\nFrom {Email.email_address} with subject line: {Email.subject_line} and the content is: {Email.email_content} marked as read.")
    except IndexError:
        print("\nYour selection isn't valid, please try again.")
read_email(inbox)

# Create a function that displays all unread Email object subject lines
# along with their corresponding index numbers.
# Loop through the inbox, select the unread emails, print the subject line and index

def view_unread_emails():
    unread_email = [Email.subject_line for Email in inbox if not Email.has_been_read]
    if unread_email:
        for email_subject in unread_email:
            print(email_subject)       
    else:
        print("\nAll emails have been read.")

# --- Email Program --- #

# Complete user_choice options below to output relevant information to user
# By calling the relevant functions created above 

while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        read_email(inbox)

    elif user_choice == 2:
        print("\nHere is a list of the subject lines of unread emails: ")
        view_unread_emails()

    elif user_choice == 3:
        print("\nYou have chosen to quit the application.")
        quit()

    else:
        print("\nOops - incorrect input. Please try again.")
