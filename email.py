"""
Using classes, methods, and functions; create an email simulator. 
"""

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False # Defaults to email as not been read

    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions.

def populate_inbox(email_address, subject_line, email_content):
    email = Email(email_address, subject_line, email_content)
    inbox.append(email)

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
      
inbox = []

populate_inbox("r.geller@friends.com", "Check this out", "Today was great!")
populate_inbox("r.green@friends.com", "Here we are", "What's happening today")
populate_inbox("j.tribbiani@friends.com", "How you doin?", "This happened today")

# Create function that loops the inbox and prints each email subject line 
# with corresponding index number using the enumerate function

def list_emails(inbox):
    print("\nThe subject lines of the inbox are:")
    for i, Email in enumerate(inbox):
       print(f"{i} {Email.subject_line}")
list_emails(inbox)

# Create function to display a selected email and contents then set to has_been_read

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

# Function to display all unread Email object subject lines.

def view_unread_emails():
    unread_email = [Email.subject_line for Email in inbox if not Email.has_been_read]
    if unread_email:
        for email_subject in unread_email:
            print(email_subject)       
    else:
        print("\nAll emails have been read.")

# --- Email Program --- #

# Add in user_choice options to output relevant information to user.

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
