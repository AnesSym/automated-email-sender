import streamlit as st
from email_sender import email_sender
import pandas as pd

from io import StringIO
from dotenv import load_dotenv
import os
import time
def load_environment():
    st.sidebar.title("Configuration")
    env = st.sidebar.selectbox("Choose the environment:", ["Caze","Skylark"])

    if env == "Caze":
        load_dotenv(".env.caze")
    else:
        load_dotenv(".env.skylark")
def main():
    st.set_page_config(
        page_title="Automated Email Sender",
        page_icon=None,
        layout="centered",
        initial_sidebar_state="expanded",
    )
    load_environment()
    def load_files(directory):
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Sidebar options
    def get_file_path(selected_file, file_type):
        if selected_file == "None":
            return None
        else:
            return f"{file_type}/{selected_file}"
        
    subject_files = load_files('subjects')
    email_files = load_files('emails')
    signature_files = [None] + load_files('attachments') 
    sales_deck_files = [None] + load_files('attachments')
    

    subject = st.sidebar.selectbox("Choose the subject:", subject_files)
    emails_sidebar = st.sidebar.selectbox("Choose the Email:", email_files)
    signature = st.sidebar.selectbox("Choose the Signature:", [f if f is not None else "None" for f in signature_files])
    sales_deck_frontend = st.sidebar.selectbox("Choose the File:", [f if f is not None else "None" for f in sales_deck_files])

    dataset = st.file_uploader("Upload a dataset CSV", type=['csv'])
    df = pd.DataFrame()
    if dataset:
        df = pd.read_csv(dataset)
        st.write("Preview of dataset:")
        st.dataframe(df.head(10)) 

    if not df.empty:
        num_recipients = st.slider("Number of recipients", min_value=1, max_value=50, value=50)
    else:
        num_recipients = 1  

    with st.form(key='email_form'):
        submit_button = st.form_submit_button(label='Send Emails')

    def init_progress_bar():
        return st.progress(0)

    def update_progress(bar, progress):
        bar.progress(progress)

    if submit_button and not df.empty:
            bar = init_progress_bar()
            df_selected_recipients = df.iloc[:num_recipients]
            rest_of_dataset = df.iloc[num_recipients:]
            buffer = StringIO()
            df_selected_recipients.to_csv(buffer, index=False)
            buffer.seek(0)
            update_progress(bar,25)
            email_sender(
                name = os.getenv("name"),
                surname = os.getenv("surname"),
                email_sender = os.getenv("email"),
                email_password = os.getenv("generated_app_password"),
                dataset = buffer,
                subject_text=get_file_path(subject, "subjects"),
                email_html_path="html_email_1.html",
                email_text=get_file_path(emails_sidebar, "emails"),
                sales_deck=get_file_path(sales_deck_frontend, "attachments"),
                signature_image_path=get_file_path(signature, "attachments")
            )
            with st.empty():
                for i in range(76):
                    time.sleep(0.001)
                    update_progress(bar,25+i)
            st.success(f"Emails have been sent to the first {num_recipients} recipients successfully!")    
            
            st.sidebar.download_button(
                label="Download New dataset",
                data=rest_of_dataset.to_csv(index=False).encode('utf-8'),
                file_name=f"new_dataset_minus_{num_recipients}.csv",
                mime="text/csv",
            )
            

if __name__ == '__main__':
    main()

