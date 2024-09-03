import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from controller.stream_controller import run
from gui.app import runGuiApp
from controller.analyzer.analyze import analyze_and_cache
from path import UNFILTERED_FP
from controller.worker.worker import Worker
from controller.worker.master import Master
from controller.analyzer.funnel import funnel_clips
from model.filterer import Filterer
from controller.stream.get_livedata import get_channel_id_by_handle, get_active_livestream
from controller.stream_controller import work
from controller.process.process import analyze_and_cache_all_folders

def periodic_analysis():
    while True:
        analyze_and_cache_all_folders()
        time.sleep(60)

def main():
    channel_handle = "@ValorantEsports"
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

if __name__ == "__main__":
    main()
