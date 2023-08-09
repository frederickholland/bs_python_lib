from bs_profile import BSProfile
from bs_venue import BSVenue
from datetime import datetime


class BSOrder:
    def __init__(
        self,
        id: str,
        order_pid: str,
        reference: str,
        total: int,
        created_time: datetime,
        completed_time: datetime,
        profile: BSProfile,
        venue: BSVenue,
    ):
        self.id = id
        self.order_pid = order_pid
        self.reference = reference
        self.total = total
        self.created_time = created_time
        self.completed_time = completed_time
        self.profile = profile
        self.venue = venue

    @classmethod
    def from_data(cls, data: dict) -> "BSOrder":
        return cls(
            data["id"],
            data["order_pid"],
            data["reference"],
            data["total"],
            data["created_time"],
            data["completed_time"],
            BSProfile.from_data(data["profile"]),
            BSVenue.from_data(data["venue"]),
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "order_pid": self.order_pid,
            "reference": self.reference,
            "total": self.total,
            "created_time": self.created_time,
            "completed_time": self.completed_time,
            "profile": self.profile.to_data(),
            "venue": self.venue.to_data(),
        }
