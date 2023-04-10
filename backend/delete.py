import os
import json
import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
    url="http://localhost:3000"
    scopes = "https://www.googleapis.com/auth/youtube"
    flow = InstalledAppFlow.from_client_secrets_file("client.json", scopes)
    flow.redirect_uri=url
    flow.run_local_server(port=3000,prompt="consent")
    credentials=flow.credentials

    print(credentials.to_json())


    youtube = build("youtube", "v3",credentials=credentials)
    request = youtube.videos().delete(
        id='rwu1oeDIlZU'
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()