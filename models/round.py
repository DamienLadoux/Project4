from datetime import datetime
from typing import Optional

from models.match import Match

class Round:
    def __init__(
        self,
        name: str,
        matches: Optional[list[Match]] = None,
        start_datetime: Optional[str] = None,
        end_datetime: Optional[str] = None,
    ):
        self.name = name
        self.matches = matches or []
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def start_round(self):
        self.start_datetime = datetime.now().isoformat()

    def end_round(self):
        self.end_datetime = datetime.now().isoformat()

    def add_match(self, match: Match):
        self.matches.append(match)

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "matches": [match.serialize() for match in self.matches],
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
        }

    @classmethod
    def from_dict(cls, data: dict, players_index: dict[str, Player]) -> "Round":
        matches = [
            Match.from_dict(match_data, players_index)
            for match_data in data.get("matches", [])
        ]
        return cls(
            name=data["name"],
            matches=matches,
            start_datetime=data.get("start_datetime"),
            end_datetime=data.get("end_datetime"),
        )

