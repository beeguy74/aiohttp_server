from app.store.crm.gino import db

class ConnectInfo(db.Model):
    __tablename__ = 'connect_info'

    id = db.Column(db.Integer(), primary_key=True)
    connect_dt = db.Column(db.DateTime(), server_default='now')