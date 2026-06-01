class PlayerView:

    @staticmethod
    def get_player_data():
        print("\n=== Nouveau joueur ===")

        last_name = input("Nom : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (YYYY-MM-DD) : ")
        chess_id = input("ID échecs (AB12345) : ")

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "chess_id": chess_id,
        }

    @staticmethod
    def display_players(players):
        print("\n=== Liste des joueurs ===")

        for player in sorted(players, key=lambda p: p.last_name):
            print(
                f"{player.full_name()} "
                f"({player.chess_id}) "
                f"- Score: {player.score}"
            )

    @staticmethod
    def show_message(message):
        print(message)