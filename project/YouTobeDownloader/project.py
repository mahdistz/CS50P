from http.client import IncompleteRead
from pytube import YouTube
import re
import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] [%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('log.txt')
    ]
)

SAVE_PATH_VIDEOS = 'youtube_downloads/videos'
SAVE_PATH_AUDIOS = 'youtube_downloads/audios'


def get_youtube_video_available_resolutions(url):
    try:
        youtube = YouTube(url)
        streams = {stream.resolution for stream in youtube.streams.filter(type="video")}
        resolutions = sorted(streams, key=lambda x: int(x[:-1]))
        return resolutions
    except Exception as e:
        logging.error(e)
        return None


def get_youtube_video_size(video_url, resolution):
    try:
        youtube = YouTube(video_url)
        video_stream = youtube.streams.filter(res=resolution, file_extension='mp4').first()
        if not video_stream:
            raise ValueError
        video_size = video_stream.filesize
        return video_size
    except Exception as e:
        logging.error(e)
        return None


def get_size_format(num, suffix="B"):
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
        if abs(num) < 1024.0:
            num = float(num)
            return f"{num:.2f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.2f} Y{suffix}"


def download_youtube_video(youtube_url, path, resolution):
    """
    Downloads a YouTube video in the specified resolution

    :param youtube_url: The URL of the YouTube video to download.
    :param path: The path to the output MP4 file.
    :param resolution: The resolution of the video to download (e.g. "720p"),
    """
    try:
        youtube = YouTube(youtube_url)
        video = youtube.streams.filter(res=resolution, file_extension='mp4').first()
        if video is not None:
            f_name, extension = os.path.splitext(video.default_filename)
            file_name = f"{f_name}_{str(video.resolution)}{extension}"
            file_path = os.path.join(path, file_name)

            if os.path.exists(file_path):
                # Generate a new file name by appending a number to the existing file name
                file_name, extension = os.path.splitext(file_name)
                i = 1
                while os.path.exists(os.path.join(path, f"{file_name}_{i}{extension}")):
                    i += 1
                file_name = f"{file_name}_{i}{extension}"
            retries = 3
            while retries > 0:
                try:
                    video.download(path, filename=file_name)
                    return True
                except IncompleteRead as e:
                    logging.warning(f"IncompleteRead error: {str(e)}. Retrying...")
                    retries -= 1
            logging.error("Failed to download video after multiple retries")
    except Exception as e:
        logging.error(e)
        return None


def download_youtube_audio(youtube_url, path):
    """
       Downloads a YouTube audio

       :param youtube_url: The URL of the YouTube video to download.
       :param path: The path to the output MP4 file.
       """
    try:
        youtube = YouTube(youtube_url)
        audio = youtube.streams.filter(only_audio=True).first()
        file_name = audio.default_filename
        file_path = os.path.join(path, file_name)

        if os.path.exists(file_path):
            # Generate a new file name by appending a number to the existing file name
            file_name, extension = os.path.splitext(file_name)
            i = 1
            while os.path.exists(os.path.join(path, f"{file_name}_{i}{extension}")):
                i += 1
            file_name = f"{file_name}_{i}{extension}"

        file = audio.download(path, filename=file_name)
        new_file = os.path.splitext(file)[0] + '.mp3'
        os.rename(file, new_file)
        return True
    except Exception as e:
        logging.error(e)
        return None


def is_valid_youtube_url(url):
    pattern = (
        r'^https?://'  # http:// or https://
        r'(?:www\.)?'  # Optional www subdomain
        r'(?:youtu\.be/|youtube\.com/'  # YouTube domain and video ID separator
        r'(?:embed/|v/|watch\?v=|watch\?.+&v=))'  # Various URL formats
        r'([\w-]{11})'  # YouTube video ID
        r'(?:.+)?$'  # Optional video parameters
    )
    match = re.match(pattern, url)
    return bool(match)


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage:\npython project.py --video youtube_video_url \
        \nor\npython project.py --audio youtube_video_url")
    else:
        audio_or_video = sys.argv[1]
        video_url = sys.argv[2]

        if audio_or_video not in ['--video', '--audio']:
            sys.exit("Invalid arguments")

        if not is_valid_youtube_url(video_url):
            sys.exit("Invalid URL")

        resolutions = get_youtube_video_available_resolutions(video_url)

        if not resolutions:
            sys.exit("Failed to download video, please check your connection")

        if audio_or_video == '--video':
            print("Available resolutions for download:")
            while True:
                i = 1
                for resolution in resolutions:
                    # pytube does not support streams higher than 720p
                    if resolution in ['1080p', '1440p', '2160p']:
                        continue
                    size_format = get_size_format(get_youtube_video_size(video_url, resolution))
                    print(f'{i}. {resolution}, size = {size_format}')
                    i += 1
                try:
                    choice = int(input(f'\nChoose A Resolution Please [1-{i - 1}]: '))
                    if 1 <= choice < i:
                        resolution_to_download = resolutions[choice - 1]
                        print(f"You're now downloading the video with resolution {resolution_to_download}...")

                        if not os.path.exists(SAVE_PATH_VIDEOS):
                            os.makedirs(SAVE_PATH_VIDEOS)

                        downloaded_video = download_youtube_video(
                            video_url,
                            SAVE_PATH_VIDEOS,
                            resolution_to_download
                        )
                        if downloaded_video:
                            sys.exit(f"Video with resolution {resolution_to_download} downloaded successfully!")
                        else:
                            sys.exit(f"Video with resolution {resolution_to_download} not downloaded")
                except ValueError as e:
                    logging.error(e)
                    print("Invalid choice!!\n")

        elif audio_or_video == '--audio':
            print("You're now downloading the audio...")
            if not os.path.exists(SAVE_PATH_AUDIOS):
                os.makedirs(SAVE_PATH_AUDIOS)
            downloaded_audio = download_youtube_audio(video_url, SAVE_PATH_AUDIOS)
            if downloaded_audio:
                sys.exit("Audio downloaded successfully!")
            else:
                sys.exit("Audio not downloaded")


if __name__ == "__main__":
    main()
