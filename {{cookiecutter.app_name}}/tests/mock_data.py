from uuid import uuid4

import {{cookiecutter.app_name}}.models as m

# -----------------------------------------------------------------------------


def _id():
    return str(uuid4())


def _row(columns, row):
    return dict(zip(columns, row))


def _table(columns, rows):
    # Convert header and tuple of tuples into tuple of dicts.
    return [_row(columns, row) for row in rows]


def _insert(session, db_table, data):
    for row in data:
        session.execute(db_table.insert().values(**row))
        session.commit()


# -----------------------------------------------------------------------------

WIDGETS = _table(('id', 'message', 'created_at'), (
    (_id(), 'message 1', '1990-01-01 00:00:00'),
    (_id(), 'message 2', '1990-01-02 00:00:00'),
    (_id(), 'message 3', '1990-01-03 00:00:00'),
    (_id(), 'message 4', '1990-01-04 00:00:00'),
))

# -----------------------------------------------------------------------------


def populate():
    session = m.db.session
    m.db.create_all()

    _insert(session, m.Widget.__table__, WIDGETS)


def clear():
    session = m.db.session
    for table in reversed(m.db.metadata.sorted_tables):
        session.execute(table.delete())

    session.commit()
