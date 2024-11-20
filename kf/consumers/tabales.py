from sqlalchemy import Column, String, Float, Integer, ForeignKey, JSON, create_engine, Table
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, relationship

connection_url = "postgresql://yossi:8520@localhost:5432/Suspicious_emails"
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()



class Hostage(Base):
    __tablename__ = 'hostage'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_name = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    words = Column(JSON)
    explos_id = Column(Integer, ForeignKey('exploss.id'))



class Explos(Base):
    __tablename__ = 'exploss'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_name = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    words = Column(JSON)


def insert_hostage(email):
    new_words = Hostage(
        email=email["email"],
        user_name=email["username"],
        ip_address=email["ip_address"],
        created_at=email["created_at"],
        words=email["sentences"],
    )
    db_session.add(new_words)
    db_session.commit()
    return new_words

def insert_exploie(email):
    new_words = Explos(
        email=email["email"],
        user_name=email["username"],
        ip_address=email["ip_address"],
        created_at=email["created_at"],
        words=email["sentences"],
    )
    db_session.add(new_words)
    db_session.commit()
    return new_words


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

