# pytomlenv
Environment in TOML for Python.

### Install
```shell
pip install pytomlenv
```

### Usage
`.env.toml` 
```toml
[production]
DEBUG = false
DB_ENGINE = "django.db.backends.postgresql"
DB_NAME = "ragx"
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "10.10.0.100"
DB_PORT = 5432

[development]
DEBUG = true
DB_ENGINE = "django.db.backends.sqlite3"
DB_NAME = "ragx.db"
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = 0

[test]
DEBUG = true
DB_ENGINE = "django.db.backends.mysql"
DB_NAME = "ragx"
DB_USER = "root"
DB_PASSWORD = "123456"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
```

your python code:
```python
from toml_env import load_env

env = load_env(".env.toml")

# `os.environ.get()` also works, but it always return string

# you have better choice with the following methods：

project: str = env.get("PROJECT")
db_name: str = env.get_str("DB_NAME")
db_user: str = env.get_str("DB_USER", "root")
db_pass: str = env.get_str("DB_PASS", "password")
db_host: str = env.get_str("DB_HOST", "localhost")
db_port: int = env.get_int("DB_PORT", 3306)

debug: bool = env.get_bool("DEBUG", False)
sentry_dsn: str = env.get_str("SENTRY_DSN", None, nullable=True)

print(debug, db_name, db_user, db_pass, db_host, db_port, sentry_dsn)
```

run your python code:
```shell
$ export ENV=development
$ python your_code.py
```

### Methods

#### `load_env` function
> def load_env(path: str = ".env.toml", override: bool = False)
- `path`: the path to the `.env.toml` file;
- `override`: 
    - if `os.environ` does not have the environment variables, it will load the environment variables from the `.env.toml` file;
    - if `os.environ` already has the environment variables, and `override=True`, it will override the environment variables with the values in the `.env.toml` file;
    - if `os.environ` already has the environment variables, and `override=False`, it will not override the environment variables with the values in the `.env.toml` file;
    

#### `get` method
- `get(key: str, default=None, nullable=False) -> Any`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_str` method
- `get_str(key: str, default=None, nullable=False) -> str`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_int` method
- `get_int(key: str, default=None, nullable=False) -> int`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_float` method
- `get_float(key: str, default=None, nullable=False) -> float`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;

#### `get_bool` method
- `get_bool(key: str, default=None, nullable=False) -> bool`
- `key`: the key in the `.env.toml` file;
- `default`: the default value if the key is not found in the `.env.toml` file;
- `nullable`: if the key is not found in the `.env.toml` file, and the default value is `None`, you should set `nullable=True`, otherwise it will raise `TomlEnvError` exception;
