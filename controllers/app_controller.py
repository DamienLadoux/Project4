from services.json_service import JsonService
from models.player import Player

from views.menu_view import MenuView
from views.player_view import PlayerView

from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


class AppController:

    def __init__(self):
        self.players = JsonService.load_players()
        self.tournaments = JsonService.load_tournaments()

        self.tournament_controller = TournamentController(
            self.tournaments,
            self.players
        )

        self.report_controller = ReportController(
            self.tournaments,
            self.players
        )

    def create_player(self):
        data = PlayerView.get_player_data()

        player = Player(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["chess_id"],
        )

        self.players.append(player)

        JsonService.save_players(self.players)

    def run(self):
        while True:
            MenuView.display_main_menu()
            choice = MenuView.get_choice()

            if choice == "1":
                self.create_player()

            elif choice == "2":
                PlayerView.display_players(self.players)

            elif choice == "3":
                self.tournament_controller.create_tournament()

            elif choice == "4":
                self.tournament_controller.list_tournaments()

            elif choice == "5":
                self.tournament_controller.start_round()

            elif choice == "6":
                self.report_controller.show_tournament_details()

            elif choice == "7":
                break
