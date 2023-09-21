"""
summary
"""
from Event import db
from Event.errors.handlers import CustomError
from datetime import datetime



# db helpers


# get unique item from table based on filter
# args:table=model_class **kwargs=filters
def query_one_filtered(table, **kwargs):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """
    return db.session.execute(
        db.select(table).filter_by(**kwargs)
    ).scalar_one_or_none()


# get all items from table based on filter
# args:table=model_class **kwargs=filters
def query_all_filtered(table, **kwargs):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (
        db.session.execute(db.select(table).filter_by(**kwargs))
        .scalars()
        .all()
    )


# get first one item from table no filter
def query_one(table):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """
    return db.session.execute(db.select(table)).scalar_one_or_none()


# get all items on table no filter
def query_all(table):
    """_summary_

    Args:
        table (_type_): _description_

    Returns:
        _type_: _description_
    """
    return db.session.execute(db.select(table)).scalars().all()


# get all items from table no filter paginated
def query_paginated(table, page):
    """_summary_

    Args:
        table (_type_): _description_
        page (_type_): _description_

    Returns:
        _type_: _description_
    """
    return db.paginate(
        db.select(table).order_by(table.date_created.desc()),
        per_page=15,
        page=page,
        error_out=False,
    )


# get all items from table based on filtered paginated
def query_paginate_filtered(table, page, **kwargs):
    """_summary_

    Args:
        table (_type_): _description_
        page (_type_): _description_

    Returns:
        _type_: _description_
    """
    return db.paginate(
        db.select(table)
        .filter_by(**kwargs)
        .order_by(table.date_created.desc()),
        per_page=15,
        page=page,
        error_out=False,
    )


# session helpers


def is_logged_in(session):
    """
    Ensures a user is logged in or returns error

    Parameterss:
        session(dict):
            - flask session object

    returns
        id(str):
            - logged in users id
    """
    user = session.get("user")

    if not user:
        raise CustomError("Unauthorized", 401, "You are not logged in")

    return user.get("id")


def format_date(date):
    """Formats date to readable string"""
    return datetime.strptime(date, '%Y-%m-%d')


def format_time(time):
    """Formats date to readable string"""

    return datetime.strptime(time,'%H:%M')


