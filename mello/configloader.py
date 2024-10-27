from typing import List
import tomli
import tomli_w

from mello.exceptions import (
    PrefixTooLong,
    PrefixNotFound,
    PrefixDeletionError,
    PrefixAlreadyExists,
)

_CFG_PATH = "./config.toml"


class _ConfigLoader:
    def __init__(self, filepath: str = _CFG_PATH) -> None:
        self._filepath = filepath

    @property
    def filepath(self) -> str:
        return self._filepath

    def _load(self) -> dict:
        with open(self._filepath, "rb") as f:
            return tomli.load(f)

    def _write(self, data: dict) -> None:
        with open(self._filepath, "wb") as f:
            tomli_w.dump(data, f)

    def get_prefix(self) -> List[str]:
        data = self._load()
        return data["prefix"]

    def add_prefix(self, prefix: str) -> None:
        data = self._load()
        if len(prefix) > 2:
            raise PrefixTooLong("A prefix cannot be more than 2 characters long.")

        elif prefix in data["prefix"]:
            raise PrefixAlreadyExists(
                "Cannot add an already existing prefix to the config."
            )

        else:
            data["prefix"].append(prefix)
            self._write(data)

    def delete_prefix(self, prefix: str) -> None:
        data = self._load()
        if prefix in data["prefix"] and len(data["prefix"]) == 1:
            raise PrefixDeletionError(
                "Cannot erase the only prefix available in config."
            )

        elif prefix not in data["prefix"]:
            raise PrefixNotFound("The requested prefix does not exist.")

        else:
            data["prefix"].remove(prefix)
            self._write(data)


config = _ConfigLoader()
