class TournamentView:

    @staticmethod
    def get_tournament_data():
        print("\n=== Nouveau tournoi ===")

        return {
            "name": input("Nom : "),
            "location": input("Lieu : "),
            "start_date": input("Date début : "),
            "end_date": input("Date fin : "),
            "description": input("Description : "),
        }

    @staticmethod
    def display_tournaments(tournaments):
        print("\n=== Tournois ===")

        for index, tournament in enumerate(tournaments):
            print(
                f"{index + 1}. "
                f"{tournament.name} "
                f"({tournament.location})"
            )

    @staticmethod
    def select_tournament(tournaments):
        TournamentView.display_tournaments(tournaments)

        while True:
            choice = input("Choisir tournoi : ")

            if not choice.isdigit():
                print("Veuillez entrer un nombre.")
                continue

            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                return index

                return index

            print("Choix invalide.")

    @staticmethod
    def display_matches(round_obj):
        print(f"\n=== {round_obj.name} ===")

        for index, match in enumerate(round_obj.matches):
            print(
                f"{index + 1}. "
                f"{match.player1.full_name()} "
                f"vs "
                f"{match.player2.full_name()}"
            )

    @staticmethod
    def get_match_result(match):
        print(
            f"\nRésultat : "
            f"{match.player1.full_name()} "
            f"vs "
            f"{match.player2.full_name()}"
        )

        print("1 = joueur 1 gagne")
        print("2 = joueur 2 gagne")
        print("3 = nul")

        return input("Choix : ")

    @staticmethod
    def show_message(message):
        print(message)