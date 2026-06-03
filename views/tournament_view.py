class TournamentView:

    @staticmethod
    def get_tournament_data():
        print("\n=== Nouveau tournoi ===")

        name = input("Nom : ")
        location = input("Lieu : ")
        start_date = input("Date début : ")
        end_date = input("Date fin : ")
        description = input("Description : ")

        rounds_input = input(
            "Nombre de rounds (4 par défaut) : "
        ).strip()

        if rounds_input == "":
            number_of_rounds = 4
        else:
            number_of_rounds = int(rounds_input)

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "number_of_rounds": number_of_rounds,
        }

    @staticmethod
    def display_tournaments(tournaments):
        print("\n=== Tournois ===")

        for index, tournament in enumerate(
            tournaments,
            start=1,
        ):
            print(
                f"{index}. "
                f"{tournament.name} "
                f"({tournament.location})"
            )

    @staticmethod
    def select_tournament(tournaments):
        TournamentView.display_tournaments(
            tournaments
        )

        return (
            int(
                input(
                    "Choisir tournoi : "
                )
            )
            - 1
        )

    @staticmethod
    def display_matches(round_obj):
        print(f"\n=== {round_obj.name} ===")

        for index, match in enumerate(
            round_obj.matches,
            start=1,
        ):
            print(
                f"{index}. "
                f"{match.player1.full_name()} "
                f"vs "
                f"{match.player2.full_name()}"
            )

    @staticmethod
    def show_message(message):
        print(message)
