# task - welcome mail, stats, think more

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
from fastapi import FastAPI, requests
import uvicorn

load_dotenv()

app = FastAPI()

def send_email(email, pdf_filepath):
    from_email: str = os.environ.get("EMAIL_USER")
    from_password: str = os.environ.get("EMAIL_PASS")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = email
    msg['Subject'] = "Your subject"

    body = "Please find your attachment."
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(pdf_filepath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= estimate.pdf")
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.post('/send_mail')
def send_mail_route():
    data = requests.Request() # ...
    email = data.get('email')
    pdf_filepath = data.get('pdfFilePath')

    if not email or not pdf_filepath:
        return {"error": "Email and pdfFilePath are required"}, 400

    if send_email(email, pdf_filepath):
        return {"message": "Email sent successfully"}, 200
    else:
        return {"error": "Failed to send email"}, 500

if __name__ == '__main__':
    uvicorn.run(app, port=8000)


def main():
    customer_email = "customer@example.com"
    pdf_path = "mail.pdf"  # Path to the PDF file

    if send_email(customer_email, pdf_path):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")

