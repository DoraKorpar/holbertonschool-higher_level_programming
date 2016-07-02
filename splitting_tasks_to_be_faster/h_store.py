import time
import random
import threading

class Store:
    def __init__(self, item_number, person_capacity):
        self.item_number = item_number
        self.__semaphore = threading.Semaphore(person_capacity)

    def enter(self):
        self.__semaphore.acquire()
        
    def buy(self):
        time.sleep(random.uniform(5, 10))
        if (self.item_number) <= 0:
            self.__semaphore.release()
            return False

        self.item_number -= 1
        self.__semaphore.release()
        return True
