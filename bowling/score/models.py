from django.db import models

# Create your models here.

class Game():
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        idx = 0
        frame_count=0
        score_sum=0
        while True:
            #check strike
            if (self.rolls[idx]) == 10:
                score_sum+=10 + self.rolls[idx+1] + self.rolls[idx+2] 
                idx += 1
            #check spare
            elif (self.rolls[idx] + self.rolls[idx+1]) == 10:
                score_sum+=10 + self.rolls[idx+2] 
                idx += 2
            #sum roll
            else:
                score_sum += self.rolls[idx]    
                score_sum += self.rolls[idx+1]    
                idx += 2

            frame_count += 1
            if frame_count == 10:
                break
        return score_sum
