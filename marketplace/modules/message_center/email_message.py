


# Import the email modules we'll need
from email.message import EmailMessage

txt = "C:/Users/hayesb3/Geany 1.38/Program Files/marketplace/the-grey-market/marketplace/message_center/email_message.txt"

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(txt, 'rb') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(str(fp.read()))

me = "brianhayes1998@yahoo.com"
you = "hayesb20@hanover.edu"
msg['Subject'] = 'The contents of %s' % "a txt file"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()