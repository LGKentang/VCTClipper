import subprocess
import os
import threading
from datetime import datetime
import path

def download_video(youtube_url, folder_name, last_seconds=40, output_file_prefix='video'):
    """
    Download the last `last_seconds` of a YouTube video stream.

    Parameters:
    - youtube_url (str): The URL of the YouTube video.
    - last_seconds (int): Number of seconds of the video to download from the end.
    - output_file_prefix (str): Prefix for the output file name. A unique suffix will be added.
    """
    output_directory = os.path.join(path.UNFILTERED_FP, folder_name)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_file = f"{output_file_prefix}_{timestamp}.mp4"
    full_output_path = os.path.join(output_directory, output_file)

    try:
        cmd_get_url = ['youtube-dl', '-g', youtube_url]
        result = subprocess.run(cmd_get_url, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stream_url = result.stdout.strip()
        
        cmd_download = [
            'ffmpeg',
            '-i', stream_url,
            '-c', 'copy',
            '-t', str(last_seconds),
            '-f', 'mp4',
            full_output_path
        ]
        subprocess.run(cmd_download, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Downloaded the last {last_seconds} seconds of the video to {full_output_path}")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

