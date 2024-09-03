import time
from celery import Celery
from controller.process.process import analyze_and_cache_all_folders
from controller.stream.get_livedata import get_active_livestream, get_channel_id_by_handle
import threading

from controller.stream_controller import run

app = Celery('tasks', broker='pyamqp://guest@localhost//')

def get_worker_stats():
    i = app.control.inspect()
    stats = i.stats()
    return

def periodic_analysis():
    while True:
        analyze_and_cache_all_folders()
        time.sleep(60)

def start_node(channel_handle):
    live_id, live_name = get_active_livestream(get_channel_id_by_handle(channel_handle))
    
    if live_id is None and live_name is None:
        print(f"No live stream found for channel {channel_handle}")
        return

    analysis_thread = threading.Thread(target=periodic_analysis, daemon=True)
    analysis_thread.start()

    try:
        run(live_id, live_name)
    except Exception as e:
        print(f"An error occurred while running the live stream: {e}")
    pass

@app.task
def analyzing_stream():
    while True:
        #analyze
        pass