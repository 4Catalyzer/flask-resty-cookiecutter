import flask_sqlalchemy as fsa
from sqlalchemy import Column, sql, Text, TypeDecorator
from sqlalchemy.dialects.postgresql import (
    TIMESTAMP as _TIMESTAMP, UUID as _UUID,
)

from . import app

# -----------------------------------------------------------------------------

db = fsa.SQLAlchemy(app)
db.metadata.schema = app.config['DB_SCHEMA']

# make sure to run
# CREATE EXTENSION IF NOT EXISTS pgcrypto
# CREATE SCHEMA IF NOT EXISTS {{cookiecutter.db_schema}}

NULL = sql.null()

# -----------------------------------------------------------------------------


class UUID(TypeDecorator):
    impl = _UUID(as_uuid=True)


class TIMESTAMP(TypeDecorator):
    impl = _TIMESTAMP(timezone=True)


# -----------------------------------------------------------------------------


class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(
        UUID, primary_key=True, server_default=sql.func.gen_random_uuid(),
    )

    message = Column(Text, nullable=False)
    created_at = Column(
        TIMESTAMP, nullable=False, server_default=sql.func.now(),
    )
