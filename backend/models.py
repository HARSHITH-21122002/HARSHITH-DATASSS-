from app import db


class FRIEND(db.Model):
    id =  db.Column(db.integer,PRIMARY_KEY=True)
    name=db.column(db.string(100),nullable=False)
    role=db.column(db.string(100),nullable=False)
    gender=db.column(db.string(10),nullable=False)
    description=db.column(db.TEXT,nullable=True)

               