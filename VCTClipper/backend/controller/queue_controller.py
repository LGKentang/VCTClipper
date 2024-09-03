from .file_controller import download_video
import threading
import time

def queue_job(video_name: str = "TEMP", youtube_url: str = ""):
    """
    Queue a job to download a video using a separate thread.

    Parameters:
    - video_name (str): Name for the folder and output file.
    - youtube_url (str): URL of the YouTube video to download.
    """
    print("Job queueing...")
    def job():
        time.sleep(20)
        download_video(youtube_url=youtube_url, folder_name=video_name, output_file_prefix=video_name)

    thread = threading.Thread(target=job)
    thread.start()
    return thread  

