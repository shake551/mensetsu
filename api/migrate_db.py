from sqlalchemy import create_engine

import sys
sys.path.append('..')

from models.user import Base as userBase
from models.interview import Base as interviewBase

DB_URL = "mysql+pymysql://root@db:3306/mensetsu?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    userBase.metadata.drop_all(bind=engine)
    userBase.metadata.create_all(bind=engine)

    interviewBase.metadata.drop_all(bind=engine)
    interviewBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
