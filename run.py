"""_summary_
"""
from Event import create_app
import os

app = create_app(
    database_uri=os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///test.db")
)

# @app.before_request
# def is_logged_in(session):
#     """
#     Ensures a user is logged in returns error

#     Parameterss:
#         session(dict):
#             - flask session object

#     returns
#         id(str):
#             - logged in users id
#     """
#     user = session.get("user")

#     if not user:
#         raise CustomError("Unauthorized", 401, "You are not logged in")

#     return user.get("id")

if __name__ == "__main__":
    app.run(debug=True)
