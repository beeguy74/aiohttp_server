from dataclasses import dataclass
import yaml
import typing

if typing.TYPE_CHECKING:
    from app.web.app import Application

@dataclass
class Config:
    db_name: str
    db_host: str

def setup_config(app: "Application"):
    with open("config/config.yml", "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        db_name=raw_config["credentials"]["db_name"],
        db_host=raw_config["credentials"]["db_host"],
    )
