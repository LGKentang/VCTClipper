from typing import List, Optional
from model.analyzed_cache import AnalyzedCache

class Filterer:
    def __init__(self, top_mode: bool, commentator_score: float, limit:Optional[int] = None) -> None:
        self.top_mode = top_mode
        self.commentator_score = commentator_score
        self.limit = limit
    
    def apply(self, datas : List[AnalyzedCache]) -> List[AnalyzedCache]:
        if self.top_mode:
            return self.get_filtered_and_sorted_data(datas,self.limit)
        else:
            return self.filter_data(datas)
        
    def filter_data(self, datas: List[AnalyzedCache]) -> List[AnalyzedCache]:
        filtered_data = []

        for data in datas:
            if not self.top_mode:
                if float(data.commentator_score) >= self.commentator_score:
                    filtered_data.append(data)

        return filtered_data

    def sort_data(self, datas: List[AnalyzedCache]) -> List[AnalyzedCache]:
        return sorted(datas, key=lambda x: float(x.commentator_score), reverse=True)

    def get_filtered_and_sorted_data(self, datas: List[AnalyzedCache], limit: Optional[int] = None) -> List[AnalyzedCache]:
        if self.top_mode:
            print(f'Limit = {limit}')
            sorted_data = self.sort_data(datas)
            if limit is not None:
                print(limit)
                return sorted_data[:limit]
            return sorted_data