import json
from pathlib import Path

from models.player import Player
from models.tournament import Tournament


class JsonService:
    PLAYERS_FILE = Path("data/players.json")
    TOURNAMENTS_FILE = Path("data/tournaments.json")

    @classmethod
    def load_players(cls):
        if not cls.PLAYERS_FILE.exists():
            return []

        with open(cls.PLAYERS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Player.from_dict(player_data)
            for player_data in data
        ]

    @classmethod
    def save_players(cls, players):
        serialized_players = [
            player.serialize()
            for player in players
        ]

        with open(cls.PLAYERS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                serialized_players,
                file,
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def load_tournaments(cls):
        if not cls.TOURNAMENTS_FILE.exists():
            return []

        with open(cls.TOURNAMENTS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Tournament.from_dict(tournament_data)
            for tournament_data in data
        ]

    @classmethod
    def save_tournaments(cls, tournaments):
        serialized_tournaments = [
            tournament.serialize()
            for tournament in tournaments
        ]

        with open(cls.TOURNAMENTS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                serialized_tournaments,
                file,
                indent=4,
                ensure_ascii=False
            )