
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

        highscores = sorted([x.score for x in self.highscore])
        return highscores
