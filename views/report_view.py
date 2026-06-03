class ReportView:

    @staticmethod
    def display_players(players):
        print("\n=== Joueurs ===")

        for player in sorted(
            players,
            key=lambda p: p.last_name
        ):
            print(
                f"{player.full_name()} "
                f"- {player.score} pts"
            )

    @staticmethod
    def display_tournament_details(tournament):
        print(f"\n=== {tournament.name} ===")
        print(f"Début : {tournament.start_date}")
        print(f"Fin   : {tournament.end_date}")

        print("\n=== Joueurs inscrits ===")

        for player in sorted(
                tournament.players,
                key=lambda p: p.last_name
        ):
            print(player.full_name())

        print("\n=== Classement ===")

        for player in tournament.rankings():
            print(
                f"{player.full_name()} "
                f"- {tournament.get_score(player)} pts"
            )

    @staticmethod
    def display_rounds(tournament):
        print("\n=== Rounds ===")

        for round_obj in tournament.rounds:
            print(f"\n{round_obj.name}")

            for match in round_obj.matches:
                print(
                    f"{match.player1.full_name()} "
                    f"vs "
                    f"{match.player2.full_name()}"
                )
