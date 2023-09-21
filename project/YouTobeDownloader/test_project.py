import pytest
import os
from project import (
    get_youtube_video_available_resolutions,
    get_youtube_video_size,
    get_size_format,
    download_youtube_video,
    download_youtube_audio,
    is_valid_youtube_url
)


@pytest.fixture
def youtube_video_url():
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@pytest.fixture
def path(tmpdir):
    return str(tmpdir)


def test_get_youtube_video_available_resolutions(youtube_video_url):
    resolutions = get_youtube_video_available_resolutions(youtube_video_url)
    assert isinstance(resolutions, list), "Resolutions should be a list"
    assert all(isinstance(resolution, str) for resolution in resolutions)


def test_get_youtube_video_size(youtube_video_url):
    resolution = "360p"
    video_size = get_youtube_video_size(youtube_video_url, resolution)
    assert isinstance(video_size, int), "Video size should be an integer"


def test_get_size_format():
    assert get_size_format(1024) == "1.00 KB"
    assert get_size_format(1024 * 1024) == "1.00 MB"
    assert get_size_format(1024 * 1024 * 1024) == "1.00 GB"


def test_download_youtube_video(youtube_video_url, path):
    resolution = "360p"
    download_youtube_video(youtube_video_url, path, resolution)
    file_name = f"Never Gonna Give You Up_{resolution}.mp4"
    file_path = os.path.join(path, file_name)
    assert os.path.exists(file_path), "Video file does not exist"
    os.remove(file_path)


def test_download_youtube_audio(youtube_video_url, path):
    download_youtube_audio(youtube_video_url, path)
    file_name = "Never Gonna Give You Up.mp3"
    file_path = os.path.join(path, file_name)
    assert os.path.exists(file_path), "Audio file does not exist"
    os.remove(file_path)


def test_is_valid_youtube_url():
    valid_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.youtube.com/embed/dQw4w9WgXcQ"
    ]
    invalid_urls = [
        "https://www.google.com",
        "https://youtube.com",
        "https://www.youtube.com/watch"
    ]
    assert all(is_valid_youtube_url(url) for url in valid_urls)
    assert not any(is_valid_youtube_url(url) for url in invalid_urls)
