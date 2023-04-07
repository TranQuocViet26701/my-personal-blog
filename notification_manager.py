import smtplib
import os

SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


class NotificationManager:
    @staticmethod
    def send_email(name, email, phone, message):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=SMTP_EMAIL, password=SMTP_PASSWORD)
                connection.sendmail(
                    from_addr=SMTP_EMAIL,
                    to_addrs=SMTP_EMAIL,
                    msg=f"Subject:Viktor's Blog Contact\n\nName: {name}\n"
                        f"Email: {email}\nPhone: {phone}\nMessage: {message}".encode('utf-8').strip())
        except smtplib.SMTPException:
            print("Error: unable to send email")

