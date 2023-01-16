""""
created on Mon Jan 16 7:30:00 2023
@author:AbdallahGaber 
"""
"""
You want your own python program to use your gamil account and send emails
so you have the make this program has access to your gamil account and we
can do this through generating a passwrod in your gamil account and giving 
it the python program. will know to do this step by step. 
"""
"""
*** At first we have to go to gamil account and make some security processes 
    - we go to gmail and create 2 factor authentication
        $ go to Gmail Account $ select Security
        $ select 2-step verification and follow instructions to activate and trun it on
    - we create a new password
        $ then blew the 2-step verification you will find app passowrds 
        $ select app passwrod and at the end of box choose select app 
           (Note:the apps listed have access on your gamil and can send email through)
        $ select other(custom name) and give it a name called Python
        $ finally Click generate it will give you a password 
        $ these password our python email program will use to access your gamil account and send emails

*** secondly we bulid a program that sends the emails
    - we use email module(bulit-in module) to build our program
    - we use alot of functions from this module 
"""
#***********************************************************************************************#
                    #*** Statring of Prgoram Coding ***#
#***********************************************************************************************#

# We import some bulit-in packge and we explain how to use them
from email.message import EmailMessage     # this package is working the sender and reciever
import ssl                                 # this package add some encyrption to the email message
import smtplib                             # this package transfers the message thorugh the internet

# At first we spicify the element of the message
sender   ='aboodymoha123@gmail.com'        # the sender email (Yours)
password ='Your Own Paassword'             # the password we generate at google for this prgoram
receiver ='jedeso9023@unicsite.com'        # the email receiving the message

# then we write the subject and body of the email message
subject = "Give a Look,Please"
body = """ It would be an honour for us to give a simple
look at our program sir. thank you.
"""
# Now package the Message using the EmailMessage()
em_msg = EmailMessage()
em_msg['From'] = sender
em_msg['To']   = receiver
em_msg['subject'] = subject
em_msg.set_content(body)

#finally we add encryption through SSL Package and transfer the message thorough SMTP package
enc_context = ssl.create_default_context()  # this context is responsible for encryption process
with smtplib.SMTP_SSL('smtp.gmail.com', 465 ,context=enc_context)as smtp:  #465 is the port number
    # we login at our gmail account using our gamil and password generated from Google passwrods
    smtp.login(sender , password)
    # we send the message to the receiver as a string
    smtp.sendmail(sender, receiver, em_msg.as_string())
