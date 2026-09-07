from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/restaurant_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE restaurant (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            address VARCHAR(200)
        )
    """))

    conn.execute(text("""
        INSERT INTO restaurant (name, address)
        VALUES ('Pizza Place', 'Rabat')
    """))

    conn.execute(text("""
        INSERT INTO restaurant (name, address)
        VALUES ('Burger House', 'Casablanca')
    """))

    conn.commit()