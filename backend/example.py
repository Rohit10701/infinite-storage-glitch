import requests
import os
import json
# Set up the authorization headers
access_token = "ya29.a0Ael9sCNknYEIhhpR5Ur459WqED6dkz1BxmKQYmtuWJ7762BoaMyCkbDW-1Dj3fFGrV28fYQMifUp8o9lbZa3S5DYGB2Xi58f6V50y9pofEH3v1FqmLGs1Ga0BB1eCdBjTpFRHh-n8uBrC6o6qy0Wp7mJ5zGxaCgYKAcwSARMSFQF4udJhu9GLf_tDzUGTnfcGgF-nbQ0163"
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
video_path = "test.mp4"
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