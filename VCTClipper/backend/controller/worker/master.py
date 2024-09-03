import threading
from typing import List
from .worker import Worker

class Master:
    def __init__(self, workers: List[Worker]) -> None:
        self.workers = workers
    
    def run(self):
        threads = []
        for worker in self.workers:
            thread = threading.Thread(target=worker.run)
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
