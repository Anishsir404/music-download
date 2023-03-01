from pytube import YouTube
import os

# Open the file containing the YouTube links
with open('list.txt', 'r') as f:
    # Read the YouTube links from the file
    video_urls = f.read().splitlines()

# Download the audio from each YouTube link
for video_url in video_urls:
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(video_url)

        # Get the audio stream with the highest bitrate
        audio_stream = yt.streams.get_audio_only()

        # Download the audio stream to a file
        audio_file = audio_stream.download()

        # Rename the audio file to use the video title as the file name
        video_title = yt.title
        audio_extension = audio_file.split(".")[-1]
        new_audio_file_name = video_title + "." + audio_extension
        os.rename(audio_file, new_audio_file_name)

        print(f"Downloaded {new_audio_file_name} from {video_url}")
    except:
        print(f"Unable to download audio from {video_url}")
