import requests
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
# Set up the authorization headers
# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"
# url="http://localhost:3000"
# scopes = ["https://www.googleapis.com/auth/youtube","https://www.googleapis.com/auth/youtube.force-ssl"]
# flow = InstalledAppFlow.from_client_secrets_file("client.json", scopes)
# flow.redirect_uri=url
# flow.run_local_server(port=3000,prompt="consent")
# credentials=flow.credentials
#
# print(credentials.to_json())
def uploadVideo():
    access_token = "ya29.a0Ael9sCPE5gHsUsA78dy9BVR1m8XENVKcudM0YZ3JXIfL4IPYKlsY2pnUZo2hy6zUVs5bV4kJ91rFvpCeQ8uAhtfNedq543aMur7lrjmVv30vZKSqNhXZTJnevYzzR_XJYlHYDMCgjknbmNLLiTCHj2a4meXJaCgYKAYYSARMSFQF4udJh0umM16NpZGXCN2HubrSayw0163"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "video/*"
    }
    # Get the upload URL for the resumable upload session
    url = "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable"
    response = requests.post(url, headers=headers)
    print(response)
    location_header = response.headers["Location"]
    print(location_header)

    # Upload the video in chunks using PUT requests
    video_path = "uploaded_file.txt.152.mp4"
    chunk_size = os.path.getsize(video_path)
    print(chunk_size)
    start_byte = 0
    end_byte = chunk_size - 1
    with open(video_path, "rb") as f:
        while start_byte < chunk_size:
            # Set the Content-Range header
            headers["Content-Range"] = f"bytes {start_byte}-{end_byte}/{chunk_size}"

            # Read the chunk of the video file and upload it
            chunk = f.read(chunk_size)
            response = requests.put(location_header, headers=headers, data=chunk)

            # Update the byte range for the next chunk
            start_byte = end_byte + 1
            end_byte = min(start_byte + chunk_size - 1, chunk_size - 1)

    # Print the response from the final PUT request
    print(response.json())
    return response.json()['id']