import os

class Storage:
    def __init__(self, path_to_storage: str):
        self.path_to_storage = path_to_storage
        self.create_storage()
        
    def create_storage(self):
        clips_folder = os.path.join(self.path_to_storage, 'Clips')
        
        subfolders = ['Archived', 'Filtered', 'Unfiltered', 'Uploaded']
        filtered_subfolders = ['Product', 'Waiting Review', 'Waste']

        if not os.path.exists(clips_folder):
            os.makedirs(clips_folder)
        
        for folder in subfolders:
            folder_path = os.path.join(clips_folder, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
        filtered_folder = os.path.join(clips_folder, 'Filtered')
        for folder in filtered_subfolders:
            folder_path = os.path.join(filtered_folder, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

# path = "C:\\Users\\darre\\Desktop\\VCT-Clipper\\storage"
# storage = Storage(path)
