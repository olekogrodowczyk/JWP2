from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite:///D:/Users/UL0243387/Downloads/census.sqlite', echo=True)
Base = declarative_base()

# with Session(engine) as session:
#     rows = session.execute(text("SELECT * FROM census")).unique()
#     for row in rows:
#         print(f'{row.state}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2000) as Sum FROM census WHERE state = 'Alaska'")).all()
    print(f'Alaska - Population 2000 - {rows[0].Sum}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2000) as Sum FROM census WHERE state = 'New York'")).all()
    print(f'New York - Population 2000 - {rows[0].Sum}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2008) as Sum FROM census WHERE state = 'Alaska'")).all()
    print(f'Alaska - Population 2008 - {rows[0].Sum}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2008) as Sum FROM census WHERE state = 'New York'")).all()
    print(f'New York - Population 2008 - {rows[0].Sum}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2008) as Sum FROM census WHERE state = 'New York' AND sex = 'F'")).all()
    print(f'New York - Women - Population 2008 - {rows[0].Sum}')

with Session(engine) as session:
    rows = session.execute(text("SELECT SUM(pop2008) as Sum FROM census WHERE state = 'New York' AND sex = 'M'")).all()
    print(f'New York - Men - Population 2008 - {rows[0].Sum}')
