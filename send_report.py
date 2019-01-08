import smtplib
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

receiver_email_list = [
    "mxlor@yahoo.com",
    "charm.lor@outlook.com",
    "yangkchicago@gmail.com",
    "joshthor123@gmail.com",
    "klee2014@yahoo.com",
    "mambamama2@gmail.com",
    "maysivue@gmail.com",
    "shalomielore@hotmail.com",
    "sunnyovang@gmail.com",
    "luexionglx@gmail.com",
    "goodnewsusher@gmail.com"
]

today = str(date.today())
current_year = str(date.today().strftime("%Y"))

sender_email = "goodnewsusher@gmail.com"
tithe_report = "tithe_report_{}.xlsx".format(current_year)
        
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ",".join(receiver_email_list)
message["Subject"] = "Tithe Report for {}".format(today)
message.attach(MIMEText("Please see attached document below for tithe report...", "plain"))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
password = getpass.getpass("Please Enter Your Gmail Password for {}: ".format(sender_email)).strip()

try:
    with open(tithe_report, "rb") as report:
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload(report.read())
        encoders.encode_base64(payload)
        payload.add_header("Content-Disposition", "attachment", filename=tithe_report)
        message.attach(payload)

    attachment = message.as_string()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email_list, attachment)

    print("""
        -------------------------------------------------------------
       | Tithe report has been sent to the relevant Good News staff! |
        -------------------------------------------------------------
        """)

except Exception as e:
    print("Failed due to the following error: {}".format(e))
finally:
    server.quit()

input("Press any key to exit...")
