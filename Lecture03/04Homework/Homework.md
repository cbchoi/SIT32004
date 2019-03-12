# Homework03
During the lectures, we have overview the requirements of the Number Baseball Game(NBG). 
Complete the NBG game. 
```python
import random

class GameManager(object):
    def __init__(self):
        pass

    def play(self):
        #print("play function")
        # loop
        while True:
            self.create()
            x = input("Would you want to play more? (y/n)")
            if x == "n":
                break
        pass

    def create(self):
        #print("start function")
        rm = RuleManager()
        rm.start()
        pass


class RuleManager(object):
    def __init__(self):
        #print("RuleManager created")
        self.num = random.sample(range(0, 10), 3)
        print(self.num)
        pass

    def start(self):

        repeat = 1
        while True:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
        
            if self.evaluate(num1, num2, num3) == True:
                break
            else:
                repeat += 1
                print("Currently you tried " + str(repeat) + "times")
        
        pass
    
    def evaluate(self, num1, num2, num3):
        if num1 == self.num[0] and num2 == self.num[1] and num3 == self.num[2]:
            return True
        else:
            ball = 0
            out = 0
            strike = 0
            
            tp = (num1, num2, num3)
            ###########################################################
            # Fill in the blank and complete the baseball game
            #
            #
            #
            #
            ###########################################################
            return False
        pass

gm = GameManager()
gm.play()

```