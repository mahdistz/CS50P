# YouTube Downloader

#### Description:

This Python script allows you to download videos and audios from YouTube using the `pytube` library. You can choose the resolution of the video you want to download or download only the audio. The script provides a convenient way to save YouTube content for offline viewing or personal use.

#### Prerequisites

- Python 3.7+
- [pytube](https://pypi.org/project/pytube/) : Python library for downloading YouTube videos
- [pytest](https://docs.pytest.org/en/stable/) : Testing framework


#### Setup

##### Method 1: Using Virtual Environment (recommended)
**NOTE: make sure you are in the root directory of the project**

Setting up a virtual environment for the YouTube downloader is recommended to isolate the project's dependencies from your system's global Python installation. Here's how you can set up and activate a virtual environment:

1. Create a virtual environment by running the following command in your terminal:

   ```shell
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   - On macOS and Linux, run the following command:

     ```shell
     source venv/bin/activate
     ```

   - On Windows, run the following command:

     ```shell
     .\venv\Scripts\activate
     ```


3. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

   This command installs all the necessary dependencies specified in the `requirements.txt` file.

##### Method 2: Without Virtual Environment

If you prefer not to use a virtual environment, you can install the required packages globally. Here's how:

1. Install the necessary packages by running the following command in your terminal:

   ```shell
   pip install pytube pytest
   ```

   This command installs the `pytube` library and the `pytest` testing framework globally.

### Usage

#### Downloading a Video

To download a video from YouTube, run the following command in your terminal:

```shell
python project.py --video youtube_video_url
```

Replace `youtube_video_url` with the URL of the YouTube video you want to download.

#### Downloading an Audio

If you prefer to download only the audio of a YouTube video, you can use the following command:

```shell
python project.py --audio youtube_video_url
```

Replace `youtube_video_url` with the URL of the YouTube video from which you want to extract the audio.

### Configuration

The YouTube downloader script allows you to configure the save paths for videos and audios. You can configure the save paths for videos and audios by modifying the following variables in the `project.py`:

```python
SAVE_PATH_VIDEOS = 'youtube_downloads/videos'
SAVE_PATH_AUDIOS = 'youtube_downloads/audios'
```

Ensure that the specified directory paths exist, or the script will create them for you when downloading videos or audios.

### Testing

The YouTube downloader script contains a set of tests to verify its functionality and ensure reliable operation. To run these tests, follow these steps:

1. Open your terminal and navigate to the root directory of the project.

2. Run the following command:

   ```shell
   pytest test_project.py
   ```

   This command executes the tests defined in the `test_project.py` file, which cover various aspects of the script.

3. Observe the test results displayed in the terminal. The tests will check different functionalities and report any errors or failures.

### Note

- This YouTube downloader project aims to provide a convenient and efficient way to download videos and audios from YouTube. However, it's important to respect the intellectual property rights of content creators and use the downloaded material responsibly and within legal boundaries.

- The script creates a log file named `log.txt` to store error logs and track potential issues during the downloading process. You can refer to this log file to diagnose any problems that may occur.

- If you encounter any errors while running the `project.py` script, make sure you have a stable internet connection and ensure the provided YouTube URL is valid. The script relies on internet connectivity to fetch video data and perform the downloading operations.

- Remember to comply with the terms and conditions of YouTube and adhere to any restrictions or regulations imposed by the platform.
