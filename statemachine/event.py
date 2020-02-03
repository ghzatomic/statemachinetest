from random import randint
from time import sleep
from transitions import Machine


class Robo(object):
    
    def __init__(self):
        pass

    def parado(self):
        print("parado")

    def on_enter_login(self):
        print("login")
        self.next()

    def on_enter_extract_1(self):
        print("extract_1")
        self.next()

    def on_enter_extract_2(self):
        print("extract_2")
        self.next()

    def on_enter_finish(self):
        print("Fim !!")


class MaquinaEstado():
    def __init__(self):

        robo = Robo()

        states = ['parado' ,'login', 'extract_1', 'extract_2', 'finish']
        
        transitions = [
            { 'trigger': 'start', 'source': 'parado', 'dest': 'login'},
            { 'trigger': 'next', 'source':'login', 'dest': 'extract_1' },
            { 'trigger': 'next', 'source':'extract_1', 'dest': 'extract_2' },
            { 'trigger': 'next', 'source':['extract_2','extract_1'], 'dest': 'finish' },
        ]

        transitions2 = [
            { 'trigger': 'start', 'source': 'parado', 'dest': 'login'},
            { 'trigger': 'next', 'source':'login', 'dest': ['extract_1','extract_2'] },
            { 'trigger': 'next', 'source':['extract_2','extract_1'], 'dest': 'finish' },
        ]

        transitions3 = [
            { 'trigger': 'start', 'source': 'parado', 'dest': 'login'},
            { 'trigger': 'next', 'source':'login', 'dest': 'extract_1' },
            { 'trigger': 'next', 'source':'login', 'dest': 'extract_2' },
            #{ 'trigger': 'next', 'source':['extract_2','extract_1'], 'dest': 'finish' },
        ]

        self.machine = Machine(model=robo, states=states,
                                       transitions=transitions3, initial='parado',
                                       ignore_invalid_triggers=True)
        robo.start()
        print(robo.state)


        
if __name__ == "__main__":
    MaquinaEstado()