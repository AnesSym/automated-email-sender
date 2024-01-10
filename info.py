from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("name")
surname = os.getenv("surname")
email = os.getenv("email")
generated_app_password = os.getenv("generated_app_password")
