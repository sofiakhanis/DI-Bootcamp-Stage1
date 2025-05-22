import random

class Game():
    def __init__ (self):
        self.user_item = None
        self.computer_item = None
    
    def get_user_item(self):
        valid = ["rock", "paper", "scissors"]
        while True:
            choice = input("Select an item (rock/paper/scissors): ").lower()
            if choice in valid:
                self.user_item = choice
                break
            else:
                print ("Invalid input. Try again.")


    def get_computer_item(self):
        computer = ["rock", "paper", "scissors"]
        self.computer_item = random.choice(computer)
    
    def get_game_result(self):
        if self.user_item == "rock" and self.computer_item == "rock":
            return "draw"
        elif self.user_item == "rock" and self.computer_item == "paper":
            return "loss"
        elif self.user_item == "rock" and self.computer_item == "scissors":
            return "win"
        elif self.user_item == "paper" and self.computer_item == "rock":
            return "win"
        elif self.user_item == "paper" and self.computer_item == "paper":
            return "draw"
        elif self.user_item == "paper" and self.computer_item == "scissors":
            return "loss"
        elif self.user_item == "scissors" and self.computer_item == "rock":
            return "loss"
        elif self.user_item == "scissors" and self.computer_item == "scissors":
            return "draw"
        elif self.user_item == "scissors" and self.computer_item == "paper":
            return "win"
        
    def play(self):
        self.get_user_item()
        self.get_computer_item()
        result = self.get_game_result()
        print (f"Your choice: {self.user_item}.")
        print (f"Computer's choice: {self.computer_item}.")
        print (f"Result: {result}.")
        return result 
    

