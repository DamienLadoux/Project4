from views.report_view import ReportView
from views.tournament_view import TournamentView


class ReportController:

    def __init__(self, tournaments, players):
        self.tournaments = tournaments
        self.players = players

    def show_players(self):
        ReportView.display_players(self.players)

    def show_tournament_details(self):
        if not self.tournaments:
            print("Aucun tournoi disponible.")
            return

        index = TournamentView.select_tournament(self.tournaments)
        tournament = self.tournaments[index]

        ReportView.display_tournament_details(tournament)
        ReportView.display_rounds(tournament)