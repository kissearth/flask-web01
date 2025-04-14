import datetime
from api.extensions import db

class CIType(db.Model):
    __tablename__ = "c_ci_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    alias = db.Column(db.String(32), nullable=False)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now())

    def __repr__(self):
        return f'<CIType {self.alias}>'


def list_all():
    types = CIType.query.all()
    # types2 = CIType.query.filter_by()
    return types
