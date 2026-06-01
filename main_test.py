from models.player import Player
from models.tournament import Tournament
from services.json_service import JsonService

players = [
    Player("Dupont", "Jean", "1990-01-01", "AB12345"),
    Player("Martin", "Luc", "1988-02-12", "CD23456"),
    Player("Bernard", "Emma", "1995-03-08", "EF34567"),
    Player("Petit", "Enrique", "1992-07-19", "GH45678"),
]

JsonService.save_players(players)

tournament = Tournament(
    "Tournoi Paris",
    "Paris",
    "2026-05-15",
    "2026-05-16",
    "Détails pour l'orga"
)

JsonService.save_tournaments([tournament])

for player in players:
    tournament.add_player(player)

round1 = tournament.create_round()

print("=== ROUND 1 ===")

for match in round1.matches:
    print(
        match.player1.full_name(),
        "vs",
        match.player2.full_name()
    )

round1.matches[0].set_result(1.0, 0.0)
round1.matches[1].set_result(0.5, 0.5)

round1.end_round()

print("\n=== CLASSEMENT ===")

for player in tournament.rankings():
    print(player.full_name(), "-", player.score)

JsonService.save_players(players)
JsonService.save_tournaments([tournament])
print("Sauvegarde OK")

round2 = tournament.create_round()

print("\n=== ROUND 2 ===")

for match in round2.matches:
    print(
        match.player1.full_name(),
        "vs",
        match.player2.full_name()
    )

loaded_players = JsonService.load_players()
loaded_tournaments = JsonService.load_tournaments()

print(loaded_players[0].full_name())
print(loaded_tournaments[0].name)