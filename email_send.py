import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    MY_ADDRESS = '22cs007@charusat.edu.in'  # Specify sender's email address here
    PASSWORD = 'Nand@2005'  # Specify sender's email password here
    RECIPIENT_EMAIL = '22cs092@charusat.edu.in'  # Specify recipient's email address here
    
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
 
    message = """
    Dear Recipient,

    This is the message content that you want to send. You can type your message here.

    Sincerely,
    Sender
    """

    msg = MIMEMultipart()  # create a message
    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'Your Subject Here'  # Specify email subject here
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # send the message via the server set up earlier.
    s.send_message(msg)
        
    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '_main_':
    main()