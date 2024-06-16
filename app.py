import streamlit as st
import pickle
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Function to authenticate and download file from Google Drive
def download_file_from_google_drive(file_id, file_name):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None

    # Load the service account credentials
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    
    service = build('drive', 'v3', credentials=creds)
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}.")

# Set your Google Drive file ID here
file_id = 'YOUR_FILE_ID'
file_name = 'km.pkl'

# Download the file if not already present
if not os.path.exists(file_name):
    download_file_from_google_drive(file_id, file_name)

# Load the KMeans model
with open(file_name, "rb") as pickle_in:
    km = pickle.load(pickle_in)

def customer_segmentation(MonetaryValue, Frequency, Recency):
    MonetaryValue = int(MonetaryValue)
    Frequency = int(Frequency)
    Recency = int(Recency)

    prediction = km.predict([[MonetaryValue, Frequency, Recency]])
    return prediction[0]

def main():
    st.title("Customer Segmentation Analysis")
    html_temp = """
        <div style="background-color: lavender; padding: 10px">
        <h2 style="color: white; text-align: center;">Customer Segmentation Analysis</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    MonetaryValue = st.text_input("MonetaryValue", "type here")
    Frequency = st.text_input("Frequency", "type here")
    Recency = st.text_input("Recency", "type here")
    result = ""
    if st.button("Predict"):
        result = customer_segmentation(MonetaryValue, Frequency, Recency)
        if result == 0:
            result = "Churned customer"
        elif result == 1:
            result = "New customer"
        elif result == 2:
            result = "Customer at risk"
        else:
            result = "Churned customer"
    st.success("The output is {}".format(result))

if __name__ == '__main__':
    main()
