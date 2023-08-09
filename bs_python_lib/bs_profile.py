from datetime import datetime


class BSProfileName:
    def __init__(
        self,
        firstname: str,
        lastname: str,
    ):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_data(cls, data: dict) -> "BSProfileName":
        return cls(
            data["firstname"],
            data["lastname"],
        )

    def to_data(self) -> dict:
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
        }


class BSProfileLocation:
    def __init__(
        self,
        postcode: int,
    ):
        self.postcode = postcode

    @classmethod
    def from_data(cls, data: dict) -> "BSProfileLocation":
        return cls(
            data["postcode"],
        )

    def to_data(self) -> dict:
        return {
            "postcode": self.postcode,
        }


class BSProfile:
    def __init__(
        self,
        id: str,
        handle: str,
        email: str,
        dob: datetime,
        current: str,
        image: str,
        name: BSProfileName,
        location: BSProfileLocation,
    ):
        self.id = id
        self.handle = handle
        self.email = email
        self.dob = dob
        self.current = current
        self.image = image
        self.name = name
        self.location = location

    @classmethod
    def from_data(cls, data: dict) -> "BSProfile":
        return cls(
            data["id"],
            data["handle"],
            data["email"],
            data["dob"],
            data["current"],
            data["image"],
            BSProfileName.from_data(data["name"]),
            BSProfileLocation.from_data(data["location"]),
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "handle": self.handle,
            "email": self.email,
            "dob": self.dob,
            "current": self.current,
            "image": self.image,
            "name": self.name.to_data(),
            "location": self.location.to_data(),
        }
