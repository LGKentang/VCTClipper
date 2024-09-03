import os
from model.filterer import Filterer
from model.analyzed_cache import AnalyzedCache
from path import WAITING_REVIEW_FP
import shutil

def read_cache(folder_path, cache="analyzed_cache.txt"):
    file_path = os.path.join(folder_path, cache)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    else:
        return None


def funnel_clips(unfiltered_clips_path: str, filters: Filterer):
    cache_data = read_cache(unfiltered_clips_path)
    
    if cache_data:
        cache_data_objects = [AnalyzedCache.from_map(data) for data in cache_data]
        destination = os.path.join(WAITING_REVIEW_FP, os.path.basename(unfiltered_clips_path))
        
        os.makedirs(destination, exist_ok=True)
        
        filtered_data = filters.apply(cache_data_objects)
        
        for data in filtered_data:
            old_file_path = data.file_path
            file_name = os.path.basename(old_file_path)
            new_file_path = os.path.join(destination, file_name)
            
            
            if not os.path.exists(old_file_path):
                continue
            
            shutil.move(old_file_path, new_file_path)
