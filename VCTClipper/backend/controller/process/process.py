from concurrent.futures import ThreadPoolExecutor, as_completed
from path import UNFILTERED_FP
from ..coverage.file_coverage import get_all_directory_in_path
from ..analyzer.analyze import analyze_and_cache

def analyze_and_cache_all_folders():
    all_dirs = get_all_directory_in_path(UNFILTERED_FP)
    num_threads = min(32, len(all_dirs)) 
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_dir = {executor.submit(analyze_and_cache, dir): dir for dir in all_dirs}
        
        for future in as_completed(future_to_dir):
            dir = future_to_dir[future]
            try:
                print(f"Successfully analyzed and cached: {dir}")
            except Exception as e:
                print(f"Error analyzing {dir}: {e}")

def filter_all_folders():
    all_dirs = get_all_directory_in_path(UNFILTERED_FP)
    
    