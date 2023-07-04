# Unlimited-Storage-Giltch
**Infinite Storage Glitch Python**
This repository is inspired by the project Infinite Storage Glitch, which utilized a YouTube video database as a storage medium for storing different files.
While the original project was implemented in Rust, this version has been entirely developed in Python.

**Description**
The Infinite Storage Glitch Python project provides a way to store files by converting them into a binary representation of ones and zeros. The files are then
encoded into a series of images, which are subsequently combined to create a video file. This video file can be uploaded to YouTube, taking advantage of 
YouTube's storage capabilities.


https://github.com/Rohit10701/Unlimited-Storage-Giltch/assets/62689661/597406fa-d227-4ab6-ab32-e9757bbab38e


**The process involves the following steps:**

1. Convert a file into a binary string representation.
2. Encode the binary string into a series of images, where each image represents a portion of the binary string.
3. Combine the images to create a video file.
4. Upload the video file to YouTube (unlisted) using the provided APIs.
5. Download the video file using the YouTube Data API.

**Video Encoding Choices**

In the Infinite Storage Glitch Python project, specific choices were made regarding the video encoding parameters. The decision to use a resolution of 360p, a frame rate of 1fps, and a pixel representation of 3x3 for each binary pixel has several considerations.

**Efficiency and Compression**

YouTube applies significant compression to uploaded videos to optimize storage and streaming efficiency. By using a lower resolution of 360p, the video file size is reduced compared to higher resolutions such as 720p or 1080p. This choice helps minimize the impact of compression on the encoded data.

Similarly, setting a frame rate of 1fps reduces the number of frames in the video. Fewer frames mean less data that needs to be encoded and stored. This further aids in mitigating compression-induced data loss.

**Pixel Representation**

The choice of a 3x3 pixel representation for each binary pixel serves multiple purposes. By using a 3x3 grid, the encoded binary pixels can be visually discerned when viewing the resulting video. This ensures the integrity of the encoded data is preserved during the video conversion process.

Additionally, the 3x3 pixel representation provides redundancy, making it more resilient to compression artifacts. In the event of slight data loss during compression, the redundancy in the pixel representation helps in recovering the original binary pixel value.

**Balancing Trade-offs**

The selection of 360p resolution, 1fps frame rate, and a 3x3 pixel representation strikes a balance between video quality, storage efficiency, and data integrity. While higher resolutions and frame rates may offer better video quality, they would result in larger video files, potentially leading to more data loss during compression. On the other hand, excessively low resolutions or frame rates might make it difficult to recover the encoded data accurately.

By carefully considering these factors, the chosen encoding parameters provide a reasonable compromise to ensure efficient storage and reliable retrieval of the encoded files while minimizing the impact of compression-induced data loss.

Please note that the encoding parameters can be adjusted based on specific requirements or preferences.


**Requirements**

To run this project, you need to have the following dependencies installed:

Python 3.7
PIL (Python Imaging Library)
ffmpeg
You can install the necessary Python packages using pip:

Copy code
pip install Pillow
FFmpeg can be installed separately according to your operating system. For example, on Ubuntu, you can install FFmpeg using the following command:

sudo apt-get install ffmpeg
Usage
Clone the repository:

bash
Copy code
https://github.com/Rohit10701/Unlimited-Storage-Giltch.git
Navigate to the project directory:

bash
Copy code
cd <repository>
Place the file you want to store in the test directory.

Modify the file_path variable in the makeVideo function in the main.py file to point to your desired file:

python
Copy code
file_path = "test/<filename>"
Run the script:

python
Copy code
python main.py
This will convert the file to a binary representation, encode it into images, create a video file, and upload it to YouTube (unlisted). The script will also download the video file using the YouTube Data API.

Once the process is complete, you can find the downloaded video file in the project directory.

Note: You may need to set up YouTube Data API credentials and provide them in the appropriate section of the script for the upload and download functionalities to work correctly. Please refer to the YouTube Data API documentation for more information on obtaining and using API credentials.

**Acknowledgements**

This project is inspired by the original work done by DvorakDwarf in the Infinite-Storage-Glitch repository.
