import os
from .commentator_analyzer import calculate_excitedness
from .sentiment_analyzer import analyze_excitement
from model.analyzed_cache import AnalyzedCache

def analyze(file_path) -> AnalyzedCache:
    commentator_score = calculate_excitedness(file_path)
    return AnalyzedCache(file_path, commentator_score)

def read_cache(folder_path, cache="analyzed_cache.txt"):
    file_path = os.path.join(folder_path, cache)
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    else:
        with open(file_path, "w") as file:
            pass
        return None

def write_cache(folder_path, cache_data, cache="analyzed_cache.txt"):
    file_path = os.path.join(folder_path, cache)
    with open(file_path, "w") as file:
        for data in cache_data:
            file.write(data + "\n")

def analyze_and_cache(folder_path: str):
    allowed_formats = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv')
    
    cache_data = read_cache(folder_path)
    cached_paths = set()
    
    if cache_data is not None:
        for data in cache_data:
            file_path = data.split("#")[0]
            normalized_path = os.path.normpath(file_path)
            cached_paths.add(normalized_path)
    
    new_cache_data = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        normalized_path = os.path.normpath(file_path)
        if os.path.isfile(normalized_path) and normalized_path not in cached_paths:
            if normalized_path.lower().endswith(allowed_formats):
                analyzed_cache = analyze(normalized_path)
                analyzed_cache_string = analyzed_cache.to_map()
                new_cache_data.append(analyzed_cache_string)
    
    if new_cache_data:
        if cache_data is None:
            cache_data = []
        cache_data.extend(new_cache_data)
        write_cache(folder_path, cache_data)
