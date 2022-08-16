# Restricitons
## Use queue
## Methods
### Add music
### Play music
## Play music in the orden that it had been added (FIFO)

from random import randint
from node_base_queue import Queue
from time import sleep


class Track:
    def __init__(self, title: str = None) -> None:
        self.title = title
        self.lenght = randint(5,8)



class mediaPlayerQueue(Queue):
    def __init__(self) -> None:
        super(mediaPlayerQueue, self).self.__init__()

    
    def add_track(self, track):
        self.enqueue(track)

    
    def play(self):
        print(f'Number of musics: {self.count}')
        while self.count > 0 and self.head is not None:
            curren_track_node = self.dequeue()
            print(f'Current music playing: {curren_track_node.title}')

            sleep(curren_track_node.length)