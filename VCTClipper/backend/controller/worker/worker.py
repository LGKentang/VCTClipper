import json,os
import uuid
def save_worker(name, channel_handle, media_type):
    worker_data = {
        'uuid' : str(uuid.uuid4()),
        'name': name,
        'channelHandle': channel_handle,
        'mediaType': media_type,
        'status' : "inactive"
    }
    print(worker_data)
    
    file_path = '../storage/Data/workers.json'
    
    # file_path = 'C:\\Users\\darre\\Desktop\\VCT-Clipper\\storage\\Data\\workers.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(worker_data)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def get_workers_backend():
    file_path = '../storage/Data/workers.json'
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Error: Could not decode JSON from file.")
                return []
    else:
        print("Error: File does not exist.")
        return []

    