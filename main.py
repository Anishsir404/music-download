from pytube import YouTube
import os

while True:
    # Get the YouTube video URL from the user
    video_url = input("Enter a YouTube video URL (or 'stop' to quit): ")
    
    # Check if the user wants to stop the program
    if video_url.lower() == 'stop':
        break
    
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
