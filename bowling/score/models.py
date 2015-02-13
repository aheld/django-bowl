from django.db import models

# Create your models here.

class Game():
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        def isSpare(rolls):
            return rolls[0] + rolls[1] == 10

        def isStrike(rolls):
            return rolls[0] == 10

        def do_score(rolls, score, frame):
            if frame > 10:
                return score

            if isStrike(rolls):
                if len(rolls) < 3: return score
                score += rolls[0] 
                score += rolls[1] + rolls[2]
                return do_score(rolls[1:], score, frame+1)

            elif isSpare(rolls):
                score += rolls[0] + rolls[1]
                score += rolls[2]
                return do_score(rolls[2:], score, frame+1)

            else:
                score += rolls[0] + rolls[1]
                return do_score(rolls[2:], score, frame+1)

        return do_score(self.rolls, 0, 1)

    def score_old(self):
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
