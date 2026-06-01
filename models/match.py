from models.player import Player

class Match:
    def __init__(
        self,
        player1: Player,
        player2: Player,
        player1_score: float = 0.0,
        player2_score: float = 0.0,
    ):
        if player1.chess_id == player2.chess_id:
            raise ValueError("Un joueur ne peut pas jouer contre lui-même")

        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def set_result(self, player1_score: float, player2_score: float):
        valid_scores = {0.0, 0.5, 1.0}
        if player1_score not in valid_scores or player2_score not in valid_scores:
            raise ValueError("Scores invalides")
        if player1_score + player2_score != 1.0:
            raise ValueError("Le total des scores doit être égal à 1")

        self.player1_score = player1_score
        self.player2_score = player2_score
        self.player1.add_score(player1_score)
        self.player2.add_score(player2_score)

    def players_pair(self) -> tuple[str, str]:
        return tuple(sorted([self.player1.chess_id, self.player2.chess_id]))

    def serialize(self) -> tuple:
        return (
            [self.player1.chess_id, self.player1_score],
            [self.player2.chess_id, self.player2_score],
        )

    @classmethod
    def from_dict(cls, data: tuple, players_index: dict[str, Player]) -> "Match":
        p1_id, p1_score = data[0]
        p2_id, p2_score = data[1]
        return cls(
            player1=players_index[p1_id],
            player2=players_index[p2_id],
            player1_score=p1_score,
            player2_score=p2_score,
        )
