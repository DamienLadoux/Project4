import re

class Player:
    CHESS_ID_PATTERN = re.compile(r"^[A-Z]{2}\d{5}$")

    def __init__(
        self,
        last_name: str,
        first_name: str,
        birth_date: str,
        chess_id: str,
        score: float =0.0,
    ):
        if not self.CHESS_ID_PATTERN.match(chess_id):
            raise ValueError("Identifiant national d'échecs invalide (format AB12345)")
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_score(self, points: float):
        self.score += points

    def reset_score(self):
        self.score = 0.0

    def serialize(self) -> dict:
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"],
            score=data.get("score", 0.0),
        )