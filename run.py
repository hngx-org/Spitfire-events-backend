"""_summary_
"""
from Event import create_app
import os

app = create_app(
    database_uri=os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///test.db")
)

if __name__ == "__main__":
    app.run(debug=True)
