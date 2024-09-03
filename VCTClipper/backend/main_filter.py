from controller.analyzer.funnel import funnel_clips
from controller.coverage.file_coverage import get_all_directory_in_path
from model.filterer import Filterer
from path import UNFILTERED_FP

def main():
    all_dirs = get_all_directory_in_path(UNFILTERED_FP)
    
    for dir in all_dirs:
        funnel_clips(dir, filters=Filterer(top_mode=True, commentator_score= 300, limit=5))


if __name__ == "__main__":
    main()