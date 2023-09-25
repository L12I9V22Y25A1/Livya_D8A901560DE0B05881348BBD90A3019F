class Player:
    def play(self):
        print("THE PLAYER IS PLAYING CRICKET")
class Batsman(Player):
    def play(self):
        print("THE BATSMAN IS BATTING")
class Bowler(Player):
    def play(self):
        print("THE BOWLER IS BOWLING")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()