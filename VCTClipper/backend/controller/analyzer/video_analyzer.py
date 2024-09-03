import cv2
import pytesseract
from concurrent.futures import ThreadPoolExecutor, as_completed
from fuzzywuzzy import fuzz

def detect_replay_in_video(video_path):
    video_capture = cv2.VideoCapture(video_path)
    
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps)

    custom_config = r'--oem 3 --psm 6'
    target_text = "replay"
    
    frame_count = 0 
    
    def process_frame(frame):
        height, width = frame.shape[:2]

    
        x1 = width // 4
        x2 = 3 * width // 4
        y1 = height // 4
        y2 = 3 * height // 4 

        cropped_frame = frame[y1:y2, x1:x2]

        if cropped_frame.size == 0:
            return False, frame  

        resized_frame = cv2.resize(cropped_frame, (640, 360))
        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray, config=custom_config)
        print(text)
        
        similarity = fuzz.partial_ratio(text.lower(), target_text.lower())
        print(f"Similarity score: {similarity}")
        
        
        threshold = 82
        if similarity >= threshold:
            return True, cropped_frame
        return False, cropped_frame


    with ThreadPoolExecutor() as executor:
        futures = []

        while True:
            ret, frame = video_capture.read()

            if not ret:
                break
            
            if frame_count % frame_interval == 0:
                future = executor.submit(process_frame, frame)
                futures.append(future)
            
            for future in as_completed(futures):
                detected, _ = future.result()
                if detected:
                    video_capture.release()
                    return True  
            
            frame_count += 1

    video_capture.release()
    return False
