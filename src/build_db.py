import sqlalchemy as db
import persistence.model as mod

engine = db.create_engine('sqlite:///src/db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)
