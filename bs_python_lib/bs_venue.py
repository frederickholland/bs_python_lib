from datetime import datetime


class BSVenueGeopoint:
    def __init__(
        self,
        latitude: float,
        longitude: float,
    ):
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_data(cls, data: dict) -> "BSVenueGeopoint":
        return cls(
            data["latitude"],
            data["longitude"],
        )

    def to_data(self) -> dict:
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }


class BSVenueAddress:
    def __init__(
        self,
        street: str,
        suburb: str,
        state: str,
        postcode: int,
        coords: BSVenueGeopoint,
    ):
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.coords = coords

    @classmethod
    def from_data(cls, data: dict) -> "BSVenueAddress":
        return cls(
            data["street"],
            data["suburb"],
            data["state"],
            data["postcode"],
            BSVenueGeopoint.from_data(data["coords"]),
        )

    def to_data(self) -> dict:
        return {
            "street": self.street,
            "suburb": self.suburb,
            "state": self.state,
            "postcode": self.postcode,
            "coords": self.coords.to_data(),
        }


class BSVenueMedia:
    def __init__(
        self,
        primary: str,
        additional: list[str],
    ):
        self.primary = primary
        self.additional = additional

    @classmethod
    def from_data(cls, data: dict) -> "BSVenueMedia":
        return cls(
            data["primary"],
            data["additional"],
        )

    def to_data(self) -> dict:
        return {
            "primary": self.primary,
            "additional": self.additional,
        }


class BSVenue:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        online: bool,
        order_method: str,
        trending: bool,
        admin: str,
        pid: str,
        address: BSVenueAddress,
        media: BSVenueMedia,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.online = online
        self.order_method = order_method
        self.trending = trending
        self.admin = admin
        self.pid = pid
        self.address = address
        self.media = media

    @classmethod
    def from_data(cls, data: dict) -> "BSVenue":
        return cls(
            data["id"],
            data["name"],
            data["description"],
            data["online"],
            data["order_method"],
            data["trending"],
            data["admin"],
            data["pid"],
            BSVenueAddress.from_data(data["address"]),
            BSVenueMedia.from_data(data["media"]),
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "online": self.online,
            "order_method": self.order_method,
            "trending": self.trending,
            "admin": self.admin,
            "pid": self.pid,
            "address": self.address.to_data(),
            "media": self.media.to_data(),
        }
