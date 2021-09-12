import typing
from dataclasses import dataclass
import yaml

if typing.TYPE_CHECKING:
    from app.web.app import Application

@dataclass
class AdminConfig:
    email: str
    password: str

@dataclass
class SessionConfig:
    key: bytes

@dataclass
class Config:
    admin: AdminConfig
    session: SessionConfig
    username: str
    password: str
    db_name: str
    db_host: str

def setup_config(app: 'Application'):
    with open("config/config.yaml", "r") as f:
        raw_config = yaml.safe_load(f)
    app.config = Config(
        admin=AdminConfig(
            email=raw_config["admin"]["email"],
            password=raw_config["admin"]["password"],
        ),
        username = raw_config["credentials"]["username"],
        password = raw_config["credentials"]["password"],
        session = SessionConfig(
            key=raw_config["session"]["key"],
        ),
        db_name=raw_config["credentials"]["db_name"],
        db_host=raw_config["credentials"]["db_host"],
    )
