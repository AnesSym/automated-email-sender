import streamlit as st
from email_sender import email_sender
import pandas as pd
import info
from io import StringIO

st.title('Automated Email Sender')


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

if submit_button and not df.empty:
    df_selected_recipients = df.iloc[:num_recipients]
    rest_of_dataset = df.iloc[num_recipients:]
    buffer = StringIO()
    df_selected_recipients.to_csv(buffer, index=False)
    buffer.seek(0)
    email_sender(
      name = info.name,
      surname = info.surname,
      email_sender = info.email,
      email_password = info.generated_app_password,
      dataset = buffer,
      subject_text="emails/subject.txt",
      email_html_path="emails/html_email_1.html",
      email_text="emails/email_1.txt",
      sales_deck=None,
      signature_image_path="attachments/sample_image.png"
    )
    st.download_button(
        label="Download New dataset",
        data=rest_of_dataset.to_csv(index=False).encode('utf-8'),
        file_name=f"new_dataset_minus_{num_recipients}.csv",
        mime="text/csv",
    )

    st.success(f"Emails have been sent to the first {num_recipients} recipients successfully!")
