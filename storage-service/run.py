from app import app, db
from app import view


if __name__ == "__main__":
    app.run()
    db.cli.run()
