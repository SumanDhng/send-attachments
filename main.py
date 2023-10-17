import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


load_dotenv("credentials.env")
display_name = os.getenv("DISPLAY_NAME") # Load Display Name from environment file
my_email = os.getenv("EMAIL") # Load Email Address from environment file
my_password = os.getenv("PASSWORD") # Load Password from environment file
bot_email = "" # Set bot's email here

# send email with an attachment
def send_email(batch_id, file_name, run_date, attachment):
    message = MIMEMultipart()
    message["From"] = f'{display_name} <{my_email}>'
    message["To"] = bot_email
    # Subject for the email containing batch_id and run_date i.e Xyz.pdf___B1___2023-04-10
    message["Subject"] =  file_name + "___B" + batch_id + "___" + run_date

    with open(attachment, "rb") as attachment_file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment_file.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_name}",
    )
    message.attach(part)
    print(f"\n\tSending : {message['Subject']}")
    server.send_message(message)

if __name__ == "__main__":
    # Get the current run date
    run_date = datetime.now().strftime('%Y-%m-%d')

     # Get the run batch ID and folder path
    batch_id = input("Enter the run batch ID: ")
    folder_path = input("Enter Folder Path: ")

    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print(f"\nLogging in as {display_name} <{my_email}>:")
    server.login(my_email, my_password)

    # Walk through the directory to find PDF files and send them via email
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith("pdf"):
                file_path = os.path.join(root, file)
                file_name =os.path.basename(file_path)

                send_email(batch_id, file_name, run_date, file_path)

    # Close the connection to the SMTP server
    server.quit()