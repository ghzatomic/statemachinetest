from random import randint
from time import sleep
from event_bus import EventBus


class Robo(object):
    
    def __init__(self):
        self.bus = EventBus()
        self.bus.add_event(self.extract_1,"login_finish")
        self.bus.add_event(self.extract_2,"login_finish")
        self.bus.add_event(self.extract_3,"login_finish")
        pass

    def login(self):
        print("Iniciando login")
        sleep(1)
        self.bus.emit("login_finish")
        print("Fim login")

    def extract_1(self):
        print("Iniciando extract_1")
        sleep(2)
        print("Fim extract_1")

    def extract_2(self):
        print("Iniciando extract_2")
        sleep(2)
        print("Fim extract_2")

    def extract_3(self):
        print("Iniciando extract_3")
        sleep(2)
        print("Fim extract_3")
    
    def finish(self):
        print("Fim !!")

    def exec(self):
        self.login()

if __name__ == "__main__":
    Robo().exec()