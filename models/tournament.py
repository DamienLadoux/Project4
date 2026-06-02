import random
from typing import Optional

from models.player import Player
from models.match import Match
from models.round import Round


class Tournament:
    DEFAULT_ROUNDS = 4

    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        description: str = "",
        number_of_rounds: int = DEFAULT_ROUNDS,
        current_round: int = 0,
        players: Optional[list[Player]] = None,
        rounds: Optional[list[Round]] = None,
        player_scores: Optional[dict[str, float]] = None,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round

        self._players = players or []
        self._rounds = rounds or []

        self.player_scores = player_scores or {}

    @property
    def players(self) -> tuple[Player, ...]:
        return tuple(self._players)

    @property
    def rounds(self) -> tuple[Round, ...]:
        return tuple(self._rounds)

    def add_player(self, player: Player) -> None:
        if any(
            existing.chess_id == player.chess_id
            for existing in self._players
        ):
            raise ValueError("Joueur déjà inscrit")

        self._players.append(player)

    def has_enough_players(self) -> bool:
        return len(self._players) >= 2

    def has_even_number_of_players(self) -> bool:
        return len(self._players) % 2 == 0

    def remove_last_player(self) -> Optional[Player]:
        if not self._players:
            return None

        return self._players.pop()

    def is_finished(self) -> bool:
        return (
            self.current_round >= self.number_of_rounds
        )

    def get_played_pairs(self) -> set[tuple[str, str]]:
        played = set()

        for round_obj in self._rounds:
            for match in round_obj.matches:
                played.add(
                    match.players_pair()
                )

        return played

    def generate_pairings(self) -> list[Match]:
        if not self.has_enough_players():
            raise ValueError(
                "Le tournoi doit contenir au moins 2 joueurs"
            )

        if not self.has_even_number_of_players():
            raise ValueError(
                "Le tournoi doit contenir un nombre pair de joueurs"
            )

        if self.current_round == 0:
            ordered_players = self._players.copy()
            random.shuffle(
                ordered_players
            )
        else:
            ordered_players = sorted(
                self._players,
                key=lambda player: player.score,
                reverse=True,
            )

        played_pairs = self.get_played_pairs()

        matches = []

        remaining = ordered_players.copy()

        while remaining:
            player1 = remaining.pop(0)

            opponent_index = None

            for index, candidate in enumerate(
                remaining
            ):
                pair = tuple(
                    sorted(
                        [
                            player1.chess_id,
                            candidate.chess_id,
                        ]
                    )
                )

                if pair not in played_pairs:
                    opponent_index = index
                    break

            if opponent_index is None:
                opponent_index = 0

            player2 = remaining.pop(
                opponent_index
            )

            matches.append(
                Match(
                    player1,
                    player2,
                )
            )

        return matches

    def create_round(self) -> Round:
        if self.is_finished():
            raise ValueError(
                "Le tournoi est terminé"
            )

        round_obj = Round(
            name=f"Round {self.current_round + 1}"
        )

        round_obj.start_round()

        for match in self.generate_pairings():
            round_obj.add_match(match)

        self._rounds.append(round_obj)

        self.current_round += 1

        return round_obj

    def rankings(self) -> list[Player]:
        return sorted(
            self._players,
            key=lambda player: (
                -player.score,
                player.last_name,
            ),
        )

    def update_scores_snapshot(self) -> None:
        self.player_scores = {
            player.chess_id: player.score
            for player in self._players
        }

    def get_score(
        self,
        player: Player,
    ) -> float:
        return self.player_scores.get(
            player.chess_id,
            player.score,
        )

    def serialize(self) -> dict:
        self.update_scores_snapshot()

        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "player_scores": self.player_scores,
            "players": [
                player.serialize()
                for player in self._players
            ],
            "rounds": [
                round_obj.serialize()
                for round_obj in self._rounds
            ],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Tournament":
        players = [
            Player.from_dict(
                player_data
            )
            for player_data in data.get(
                "players",
                [],
            )
        ]

        players_index = {
            player.chess_id: player
            for player in players
        }

        rounds = [
            Round.from_dict(
                round_data,
                players_index,
            )
            for round_data in data.get(
                "rounds",
                [],
            )
        ]

        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data.get(
                "description",
                "",
            ),
            number_of_rounds=data.get(
                "number_of_rounds",
                cls.DEFAULT_ROUNDS,
            ),
            current_round=data.get(
                "current_round",
                0,
            ),
            players=players,
            rounds=rounds,
            player_scores=data.get(
                "player_scores",
                {},
            ),
        )
