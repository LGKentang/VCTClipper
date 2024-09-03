class AnalyzedCache:
    def __init__(self, file_path,commentator_score):
        self.file_path = file_path
        # self.sentiment_score = sentiment_score
        self.commentator_score = commentator_score
        # self.is_replay = is_replay
        
    def aggregate(self):
        pass 
    
    def to_map(self):
        return f"{self.file_path}#{self.commentator_score}"
    
    @staticmethod
    def from_map(cache_data: str):
        datas = cache_data.split("#")
        if len(datas) != 2:
            raise ValueError("Invalid cache data format")
        return AnalyzedCache(datas[0], datas[1])