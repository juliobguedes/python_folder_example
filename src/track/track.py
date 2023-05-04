from src.visualization.confusion_matrix import confusion
from abc import ABC, abstractmethod

class Track(ABC):
    def __init__(self, audio_file) -> None:
        super().__init__()
        self.audio_file = audio_file
    
    @abstractmethod
    def split(self, split_duration=10):
        pass


class TrackInda(Track):
    def __init__(self, audio_file) -> None:
        super().__init__(audio_file)
        
    def split(self, split_duration=10):
        pass


class TrackOpenMic(Track):
    def __init__(self, audio_file, relevance) -> None:
        super(Track, self).__init__(audio_file)
        self.relevance = relevance
        

track = TrackInda()
