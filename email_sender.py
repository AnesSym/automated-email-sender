import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd


def email_sender(dataset: pd.DataFrame,
         name: str,
         surname: str,
         email_sender: str,
         email_password: str,
         subject_text: str,
         email_text: str, 
         sales_deck = None,
         signature = None):
    """
    Send personalized emails to recipients based on the data provided.

    Args:
        dataset (pd.DataFrame): A DataFrame containing recipient information.
        email_sender (str): The email address of the sender.
        email_password (str): The password for the sender's email account.
        subject_text (str): The path to a text file containing email subject content.
        email_text (str): The path to a text file containing email body content.

    Notes:
        - The `'dataset'` DataFrame should contain at least two columns: 'First Name' and 'Email'.
        - `'subject_text'` and `'email_text'` should be plain text files containing the subject and
          email body content, respectively. The content of these files will be personalized for
          each recipient.
        - Attachments (e.g., a PDF slide deck and a signature image) are included in the email.
          The 'sales_deck.pdf' attachment is added to the first email only.

    Example:
        To send emails to a list of recipients, you can call this function as follows:
        email_sender(`data`, `'your_email@gmail.com'`, `'generated_app_password'`, `'subject.txt'`, `'email_body.txt'`)
    
    Generated App Password:
        To authenticate using Google's third-party authentication (e.g., generating an "App Password" for Gmail), you'll need to follow these steps:

        1. Generate an App Password:

        - Go to your Google Account settings: https://myaccount.google.com/
        - Navigate to "Security" in the left-hand menu.
        - Under "Signing in to Google," select "App passwords" or "Third-party apps with account access."
        - Choose the app and the device you want to generate the App Password for. If you don't see your app listed, select "Other (Custom name)".
        - Click "Generate" and follow the instructions to enter the App Password on your device.

        2. Use the App Password in Your Code:
        Replace `'generated_app_password'` with the actual App Password you generated from your Google Account settings. 
        
        `Keep this password confidential and secure.`
    """
    df = pd.read_csv(dataset) 
    data = df[["First Name","Email"]]

    for index, row in data.iterrows():
        client_name = row["First Name"]
        email_receiver = row["Email"] 

        em = MIMEMultipart()

        # Open the subject.txt file for reading
        with open(f"emails/{subject_text}", 'r', encoding="utf-8") as file:
            subject_open= file.read()
        
        subject_content = f"{client_name}, {subject_open}"

        # Open the subject.txt file for reading
        with open(f"emails/{email_text}", 'r', encoding="utf-8") as file:
            email_open = file.read()

        email_content = f"Hi {client_name}, {email_open}"

        em['From'] = f"{name} {surname}"
        em['To'] = email_receiver
        em['Subject'] = subject_content
        
        email_body = MIMEText(email_content, 'plain')
        em.attach(email_body)
        
        if sales_deck is not None:
            with open(f"attachments/{sales_deck}", 'rb') as pdf_file:
                    slide_deck = MIMEApplication(pdf_file.read(), _subtype='pdf')
                    slide_deck.add_header('content-disposition', 'attachment', filename=f"{sales_deck}")
                    em.attach(slide_deck)
                #slide deck should be attached on the first email only.
        if signature is not None:
            with open(f"attachments/{signature}", 'rb') as image_file: #signature is attached here
                image = MIMEImage(image_file.read())
                image.add_header('Content-Disposition', 'attachment', filename=f"{signature}")
                em.attach(image)
        
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp: #sending the email
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        print(f"Email sent to {client_name} at {email_receiver}")