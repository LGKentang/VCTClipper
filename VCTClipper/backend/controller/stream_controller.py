from googleapiclient.discovery import build
import time
from collections import deque
from .queue_controller import queue_job
from datetime import datetime, timedelta
from .stream.get_livedata import get_live_chat_id, get_live_chat_messages

last_work_time = datetime.min

def work(live_id : str, live_name : str, retries=0, max_retries=5):
    """
    Triggers the video download 
    
    Parameters:
    - live_id (str) : Live ID
    - live_name (str) : Live Name
    - retries (int): Current retry count.
    - max_retries (int): Maximum number of retry attempts.
    """
    global last_work_time
    queue_job(video_name=live_name, youtube_url="https://www.youtube.com/watch?v=" + live_id)
    last_work_time = datetime.now()


def run(live_id, live_name):
    live_chat_id = get_live_chat_id(live_id)
    next_page_token = None
    last_processed_comment_id = None
    total_comments = 0

    comment_counts = deque(maxlen=50)  
    running_sum = 0

    while True:
        response = get_live_chat_messages(live_chat_id, next_page_token)
        
        messages = response.get('items', [])
        # print(messages)
        
        new_comments_count = 0
        for message in messages:
            comment_id = message['id']
           
            if comment_id != last_processed_comment_id:
                new_comments_count += 1     
                last_processed_comment_id = comment_id
        

        total_comments += new_comments_count
        
        if len(comment_counts) == comment_counts.maxlen:
            oldest_count = comment_counts.popleft()
            running_sum -= oldest_count

        comment_counts.append(new_comments_count)
        running_sum += new_comments_count

        if len(comment_counts) > 1:
            mean_comments = running_sum / len(comment_counts)
        else:
            mean_comments = new_comments_count

        current_time = datetime.now()
        if new_comments_count > mean_comments * 1.5:
            time_since_last_work = current_time - last_work_time
            if time_since_last_work > timedelta(seconds=15):
                work(live_id,live_name)
            else:
                print("Blocked due to multiple calls")

        print(f"New comments in this batch: {new_comments_count}")
        print(f'Mean comments in this batch: {mean_comments}')
        print(f"Total comments so far: {total_comments}\n")

        next_page_token = response.get('nextPageToken')
        time.sleep(10)

