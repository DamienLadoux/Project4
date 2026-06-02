class MenuView:

    @staticmethod
    def display_main_menu():
        print("\n=== GESTION TOURNOI ÉCHECS ===")
        print("1. Créer un joueur")
        print("2. Lister les joueurs")
        print("3. Créer un tournoi")
        print("4. Lister les tournois")
        print("5. Lancer un round")
        print("6. Rapports")
        print("7. Quitter")

    @staticmethod
    def get_choice():
        return input("Votre choix : ")
