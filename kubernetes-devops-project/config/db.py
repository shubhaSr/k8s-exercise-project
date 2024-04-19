from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://admin:password@db:5432/storedb")

meta = MetaData()

conn = engine.connect()
