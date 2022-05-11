import smtplib
from email.message import EmailMessage

print("Send email using your gmail account") 
print("(Please make sure to allow 3rd parties to send email from your account)")

USER_MAIL                   = input("Enter email-address: ")
PASSWORD                    = input("Enter your password: ")
RE_PASSWORD                 = input("Re-enter your password: ") 
if PASSWORD                 != RE_PASSWORD:
    print("Your password's do not match")
    quit()
RECEIVER_EMAIL              = input("Enter receiver email-address: ")
SUBJECT                     = input("Enter email subject: ")
MESSAGE                     = input("Enter email body content: ")

CONTENT                     = EmailMessage()
CONTENT["From"]             = USER_MAIL 
CONTENT["To"]               = RECEIVER_EMAIL
CONTENT["Subject"]          = SUBJECT

html = f"""
<html>
    <body>
        <h1>{SUBJECT}</h1>
        <p>{MESSAGE}</p>
    </body>
</html>
"""

CONTENT.add_alternative(html, subtype="html")

server                      = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(USER_MAIL, PASSWORD)
server.sendmail(USER_MAIL, RECEIVER_EMAIL, CONTENT.as_string())



