import pygame
# This is from my survival game project

class InputManager:
    def __init__(self, keyList:list[int]=[]):
        self.key_info_list = []
        self.key_state_list = []
        
        if keyList != []:
            self.addKeyList(keyList)

    def debug(self, keyNumber:int):
        for i in range(len(self.key_info_list)):
            key = self.key_info_list[i]
            
            if key == keyNumber:
                state = self.key_state_list[i]
                print(f"Key: {key} is {state}")
                return
        print(f"Error: No such key with the value of {keyNumber} is being monitored.")

    def addKeyList(self, keyList:list[int]):
        for num in keyList:
            self.addKey(num)
    
    def addKey(self, keyNumber:int):
        self.key_info_list.append(keyNumber)
        self.key_state_list.append(False)
    
    def getKeyState(self, keyNumber:int):
        for i, keyN in enumerate(self.key_info_list):
            if keyN == keyNumber:
                return self.key_state_list[i]
            
        print(f"Error: No such key with the value of {keyNumber} is being monitored.")

    def poll(self, event:pygame.event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for i, num in enumerate(self.key_info_list):
                if num == event.key:
                    self.key_state_list[i] = (event.type == pygame.KEYDOWN)