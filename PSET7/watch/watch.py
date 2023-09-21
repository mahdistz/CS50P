import re
import sys


def main():
    html_input = input('HTML: ')
    print(parse(html_input))


def parse(s):
    # Regular expression pattern to match YouTube URLs
    youtube_regex = r"https?://(?:www\.)?youtube\.com/embed/([0-9A-Za-z_-]{11})"

    # Find all iframe elements in the HTML string
    iframe_matches = re.findall(r"<iframe.*?</iframe>", s, re.DOTALL)

    for iframe_match in iframe_matches:
        # Extract the src attribute value from the iframe element
        src_match = re.search(r'src="([^"]+)"', iframe_match)
        if src_match:
            # Extract the YouTube video ID from the src URL
            url = src_match.group(1)
            youtube_match = re.search(youtube_regex, url)
            if youtube_match:
                video_id = youtube_match.group(1)
                # Return the youtu.be equivalent URL
                return f"https://youtu.be/{video_id}"

    # Return None if no YouTube URL is found
    return None


if __name__ == "__main__":
    main()