import smtplib
from email.message import EmailMessage
import os
import imghdr

sender = "senders email address"
password = os.getenv("save your password in the environment variables of your operating system")
receiver = "receivers email address"

# function to send the capture image with email

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, we just saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    host = smtplib.SMTP("smtp.gmail.com", 587)
    host.ehlo()
    host.starttls()
    host.login(sender, password)
    host.sendmail(sender, receiver, email_message.as_string())
    host.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
