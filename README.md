# Automated Email Sender

This document provides step-by-step instructions to set up and use the Email Sender Project, a simple program to send emails to a list of recipients. No prior coding experience is required.

## Prerequisites

Before you begin, you will need to install Visual Studio Code and Python on your computer.

### Install Visual Studio Code

Visual Studio Code (VS Code) is a free code editor that you'll use to run the project.

1. Visit the [VS Code website](https://code.visualstudio.com/).
2. Download the version suitable for your operating system (Windows, macOS, or Linux).
3. Run the downloaded file and follow the installation instructions.

### Install Python

Python is the programming language used by this project.

1. Visit the [Python download page](https://www.python.org/downloads/).
2. Download the latest version for your operating system.
3. Run the downloaded file and follow the installation instructions.
   - Ensure you check the box that says “Add Python to PATH” during installation.

## Download and Set Up the Project

Follow these steps to download and set up the Email Sender Project on your computer.

1. **Download the Project**:
   - Go to the project's GitHub page.
   - Click on the "Code" button and select "Download ZIP".
   - Save the ZIP file to your computer and remember the location.

2. **Extract the Project**:
   - Navigate to the ZIP file in your file explorer.
   - Right-click on the ZIP file and select "Extract All...".
   - Choose where you want to extract the project files and extract them.

3. **Open the Project in VS Code**:
   - Open VS Code.
   - Go to `File` > `Open Folder...`.
   - Select the folder where you extracted the project and click "Open".

4. **Set Up the Project**:
   - With the project open in VS Code, open the integrated terminal:
     - You can open the terminal by selecting `Terminal` > `New Terminal` from the top menu.
   - In the terminal, install the required libraries by running:
     ```
     pip install -r requirements.txt
     ```

## Configuration Instructions

To configure the Email Sender Project, you'll need to fill out the `.env` file with your personal information. This file contains sensitive data, so make sure to keep it safe and secure.

Here's a step-by-step guide to setting up your `.env` file:

1. **Open the `.env` File**:
   - Locate the `.env` file in the root directory of the project.
   - Open it with a text editor of your choice, such as Notepad or Visual Studio Code.

2. **Fill Out Your Personal Information**:
   - You will see several fields in the file. Please replace the placeholder text with your actual information.
   - Here is an explanation of each field in the `.env` file:

     ```
     # Keep this information safe and secure

     # Your Name
     # Replace 'John' with your first name.
     name=John

     # Your Last Name
     # Replace 'Doe' with your surname.
     surname=Doe

     # Your Email Address
     # Replace 'example@gmail.com' with your email address.
     email=example@gmail.com

     # Your Generated App Password
     # Replace 'xxxx yyyy zzzz cccc' with the app password you generated.
     # Instructions for generating an app password can be found below.
     generated_app_password=xxxx yyyy zzzz cccc
     ```

3. **Generate and Enter Your App Password**:
   - Follow the instructions to generate an app password from your Google Account:
     - Go to your [Google Account settings](https://myaccount.google.com/).
      - Navigate to "Security" in the left-hand menu.
      - Under "Signing in to Google," select "App passwords" or "Third-party apps with account access."
      - You may be prompted to sign in. Use your Google account credentials.
      - Choose the app and the device you want to generate the App Password for. If you don't see your app listed, select "Other (Custom name)".
      - Click "Generate".
     - Replace `xxxx yyyy zzzz cccc` with the generated app password.
     - Please note that App Passwords are only available if you have **2-Step Verification** enabled on your Google account.

4. **Save the `.env` File**:
   - After filling in your details, save (ctrl + S) the `.env` file and close the text editor.

5. **Proceed With Using the Project**:
   - With the `.env` file set up, you can now proceed to use the project as instructed in the main README.

Remember not to share the `.env` file or its contents with anyone, and avoid uploading it to public repositories or websites to prevent unauthorized access to your personal information.


## Send Emails 

### Customizing the Email Sender Function

To use the Email Sender Project, you will need to place your custom files in the appropriate folders and specify their names in the `email_sender` function. This function is already configured to look in the right folders, so you just need to ensure your files are correctly named and placed.

### Step-by-Step Instructions:

1. **Prepare Your Files**:
   - Make sure you have the following files ready:
     - A CSV file with the list of email recipients.
     - A plain text file for the email subject.
     - A plain text file for the email body.
     - Any attachments you wish to include in the emails, such as PDFs or images.

2. **Place Files in Corresponding Folders**:
   - Put your CSV file in the project's root directory.
   - Place the subject and email body text files in the `emails` folder.
   - Place any attachments (PDFs, images) in the `attachments` folder.

3. **Update the `email_sender` Function**:
   - Open the `main.py` file in Visual Studio Code or your preferred text editor.
   - Locate the `email_sender` function.
   - Update the function arguments with the names of your files, as shown below:

     ```python
     email_sender(
         # Ensure the filenames below match the names of your actual files.
         dataset="name_of_dataset.csv",           # Your CSV file name.
         subject_text="subject.txt",              # Your email subject file name.
         email_text="email_body.txt",             # Your email body file name.
         sales_deck="sample_attachment.pdf",      # Your PDF attachment file name (if any).
         signature="signature_image.png"          # Your signature image file name (if any).
     )
     ```

   - Replace the placeholders (e.g., `name_of_dataset.csv`) with the actual names of your files.
   ### Optional Attachments:

   - **PDFs and Signatures**: If you don't want to include a PDF attachment or a signature image, you have two options:
     1. **Remove the Line**: Simply delete the line of code that references the attachment you do not wish to include.
     2. **Set to None**: Alternatively, you can set the value to `None`. This tells the program that no attachment is to be included.
   ### Example:

   ```python
   email_sender(
       # Other parameters (dataset, subject_text, email_text) remain unchanged.
       # ...
   
       # If you do not want to include a PDF, you can do one of the following:
       # Option 1: Remove the line entirely.
       # Option 2: Set to None.
       sales_deck=None,
   
       # The same applies for the signature image:
       # Option 1: Remove the line entirely.
       # Option 2: Set to None.
       signature=None
   )
4. **Run Your Project**:
   - After placing your files and updating the function, save the `main.py` file.
   - Run the script from the terminal in Visual Studio Code:
     ```bash
     python main.py
     ```
   - The script will send emails to the recipients listed in your CSV file using the content and attachments you provided.

**Note**: It is crucial that the file names in the `email_sender` function match exactly with the names of the files you placed in the folders. Any discrepancy will result in errors.

Please ensure the file paths and names match exactly, as errors here will prevent the emails from being sent correctly. Always double-check your work for accuracy.

## Email Sending Limit

When using this project to send emails through Gmail, it's important to be aware of Gmail's sending limits to avoid issues with your email account. Gmail typically allows sending a limited number of emails per day to prevent spamming. If you exceed this limit, Gmail may temporarily disable your account's ability to send more emails.

### Recommendations for Sending Emails:

- **Limit Your Email Batch**: Try to send between **50 to 100 emails** per batch. This is a general guideline to reduce the risk of reaching Gmail's sending limits.
  
- **Spread Out Your Emails**: If you need to send more than 100 emails, consider spreading them out over multiple days or sending them in smaller batches throughout the day.

- **Monitor Your Account**: After sending a large number of emails, keep an eye on your account for any notifications from Gmail about sending limits or account activity.

By following these recommendations, you can help ensure that your email account remains in good standing and avoid interruptions in your ability to send emails.

