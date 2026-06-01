class ReportView:

    @staticmethod
    def display_players(players):
        print("\n=== Joueurs ===")

        for player in sorted(players, key=lambda p: p.last_name):
            print(
                f"{player.full_name()} "
                f"- {player.score}"
            )

    @staticmethod
    def display_tournament_details(tournament):
        print(f"\n{tournament.name}")
        print(tournament.start_date)
        print(tournament.end_date)

    @staticmethod
    def display_rounds(tournament):
        for round_obj in tournament.rounds:
            print(f"\n{round_obj.name}")

            for match in round_obj.matches:
                print(
                    f"{match.player1.full_name()} "
                    f"vs "
                    f"{match.player2.full_name()}"
                )