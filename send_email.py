import smtplib
from email.message import EmailMessage
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


my_email = os.getenv("my_email")
password = os.getenv("password")


class SendEmail:
    def __init__(self, to_address, product_name, product_price, set_price):
        self.to_address = to_address
        self.product_name = product_name
        self.product_price = product_price
        self.set_price = set_price

    def send_email(self):
        msg = EmailMessage()
        msg.set_content(f"Dear user,\nThe price for {self.product_name} has droped under {self.set_price},"
                        f"it now costs {self.product_price}")
        msg['Subject'] = "Price Drop"
        msg['From'] = my_email
        msg['To'] = self.to_address
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.send_message(msg)
            print("email sent successfully")
        except Exception as e:
            print(
                f"An error has occured {e}"
            )