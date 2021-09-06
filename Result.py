

class Result:

    def __init__(self, winner, tourment, publication_date):
        self.winner = winner
        self.tourment = tourment
        self.publication_date = publication_date



class TennisResult(Result):
    def __init__(self, winner, tourment, publication_date, looser, number_of_sets):
        super().__init__(winner, tourment, publication_date)
        self.looser = looser
        self.number_of_sets =number_of_sets



class NBAResult(Result):
    def __init__(self, winner, tourment, publication_date, looser, game_number, mvp):
        super().__init__(winner, tourment, publication_date)
        self.looser = looser
        self.game_number = game_number
        self.mvp = mvp



class F1Result(Result):
    def __init__(self, winner, tourment, publication_date, seconds):
        super().__init__(winner, tourment, publication_date)
        self.seconds = seconds


