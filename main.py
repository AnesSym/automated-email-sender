from email_sender import email_sender
import info

if __name__ == "__main__":
     email_sender (
          #everything bellow this comment line is edited in the .env file.
          name = info.name,
          surname = info.surname,
          email_sender = info.email, 
          email_password = info.generated_app_password, 
          #everything bellow this comment line can be changed to your own custom files.
          dataset = "example_dataset.csv",
          subject_text="subject.txt", 
          email_text="email_1.txt",
          sales_deck="sample.pdf",
          signature="image.png"
          )









