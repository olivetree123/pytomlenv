import os
import json

from pytomlenv import (
    load_env,
    TomlEnvError,
)


def test_load():
    os.environ["DB_ENGINE"] = "django.db.backends.test"

    env = load_env(path=".env.toml")

    DATABASES = {
        'default': {
            'ENGINE': env.get_str("DB_ENGINE"),
            'NAME': env.get_str("DB_NAME"),
            "USER": env.get_str("DB_USER"),
            "PASSWORD": env.get_str("DB_PASSWORD"),
            "HOST": env.get_str("DB_HOST"),
            "PORT": env.get_int("DB_PORT"),
            "HAHA": env.get_str("HAHA", default=None, nullable=True),
        }
    }

    print(json.dumps(DATABASES, indent=4))
