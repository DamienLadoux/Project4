from models.player import Player
from models.tournament import Tournament
from services.json_service import JsonService
from views.tournament_view import TournamentView
import random


class TournamentController:
    def __init__(
        self,
        tournaments: list[Tournament],
        players: list[Player]
    ):
        self.tournaments = tournaments
        self.players = players

    def _generate_random_result(self, match) -> None:
        result = random.choice(
            [
                (1.0, 0.0),
                (0.0, 1.0),
                (0.5, 0.5),
            ]
        )

        match.set_result(result[0], result[1])

    def create_tournament(self) -> None:
        if len(self.players) < 2:
            TournamentView.show_message(
                "Il faut au moins 2 joueurs pour créer un tournoi."
            )
            return

        data = TournamentView.get_tournament_data()

        tournament = Tournament(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
        )

        players_to_register = self.players.copy()
        excluded_player = None

        if len(players_to_register) % 2 != 0:
            excluded_player = players_to_register.pop()

        for player in players_to_register:
            tournament.add_player(player)

        self.tournaments.append(tournament)
        JsonService.save_tournaments(self.tournaments)

        TournamentView.show_message("Tournoi créé.")

        if excluded_player:
            TournamentView.show_message(
                f"Attention : {excluded_player.full_name()} "
                f"n'a pas été inscrit car le nombre de participants était impair."
            )

    def list_tournaments(self) -> None:
        if not self.tournaments:
            TournamentView.show_message("Aucun tournoi disponible.")
            return

        TournamentView.display_tournaments(self.tournaments)

    def start_round(self) -> None:
        if not self.tournaments:
            TournamentView.show_message("Aucun tournoi disponible.")
            return

        index = TournamentView.select_tournament(self.tournaments)
        tournament = self.tournaments[index]

        if tournament.is_finished():
            TournamentView.show_message("Ce tournoi est terminé.")
            return

        if not tournament.has_enough_players():
            TournamentView.show_message(
                "Impossible de lancer un round : pas assez de joueurs."
            )
            return

        if not tournament.has_even_number_of_players():
            excluded_player = tournament.remove_last_player()

            TournamentView.show_message(
                f"Attention : {excluded_player.full_name()} "
                f"a été retiré du tournoi car le nombre de joueurs était impair."
            )

            JsonService.save_tournaments(self.tournaments)

        round_obj = tournament.create_round()

        TournamentView.display_matches(round_obj)

        for match in round_obj.matches:
            self._generate_random_result(match)

            print(
                f"{match.player1.full_name()} "
                f"{match.player1_score} - "
                f"{match.player2_score} "
                f"{match.player2.full_name()}"
            )

        round_obj.end_round()

        JsonService.save_tournaments(self.tournaments)

        TournamentView.show_message(
            "Résultats générés automatiquement."
        )

