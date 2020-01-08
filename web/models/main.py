from util.databae_conn import db

class Temperature(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    duration    = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.String(50), nullable=False)
    timestamp   = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Temperature %r>' % self.duration