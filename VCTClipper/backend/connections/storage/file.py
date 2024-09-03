import os
def get_all_directory_in_path(curr_path : str):
    all_directories = []
    for root, dirs, _ in os.walk(curr_path):
        for dir in dirs:
            all_directories.append(os.path.join(root, dir))
    return all_directories