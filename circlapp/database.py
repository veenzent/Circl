import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

load_dotenv()
file_content = os.getenv("SERVICE_ACC_KEY_JSON")

# Fetch the service account key JSON file contents
cred = credentials.Certificate(file_content)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com'
})


def get_db():
    # As an admin, the app has access to read and write all data, regardless of Security Rules
    # ref = db.reference('restricted_access/secret_document')
    ref = db.reference("/")
    # print(ref.get())
    try:
        yield ref
    finally:
        pass
