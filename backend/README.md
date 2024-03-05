# me-gpt Backend
The backend includes shell scripts to automate commands. If your system doesn't have WSL, you'll need to install and activate it to run a script, or you can simply use a git bash terminal to run them.

## Initializing The Django Project
Run `sh init.sh` to initialize and run the backend in a dev environment.

`init.sh`: 
- creates the database if it doesn't already exist (MySQL)
- creates a venv if its doesn't already exist (pip)
- automatically installs all dependencies into the venv
- automatically migrates models to the database
- automatically runs the django server

## Dev Requirements
- MySQL Server running on `localhost:3306`
- Python
- a `.env` file with the following ENV vars:
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
- a `local_settings.py` file in `api/config`:

```
DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "OPTIONS": {"autocommit": True},
    }
}
```

## Installing Dependencies
From the api directory, run `sh pip_install.sh <package_name>` to install new packages. This guarantees it's intalled into the venv and automatically updates `requirements.txt`.
