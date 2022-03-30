

class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.played = 0
        self.highscore = []
    
    def add_game(self, game, won_or_lost):
        self.played += 1
        self.highscore.append(game)
        if won_or_lost == True:
            self.wins += 1
        else:
            self.losses += 1

    def find_highscores(self):
        max_score = [float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
        for i in self.highscore:
            for j in range(0,5):
                if i.score < max_score[j]:
                    max_score[j] = i.score
                    break
            
        return [x for x in max_score if x != float('inf')]
