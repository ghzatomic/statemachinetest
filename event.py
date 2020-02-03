from random import randint
from time import sleep


class Robo(object):
    
    def __init__(self):
        pass

    def login(self):
        print("Iniciando login")
        sleep(1)
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
        self.extract_1()
        self.extract_2()
        self.extract_3()
        self.finish()

if __name__ == "__main__":
    Robo().exec()