from app import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    alt = db.Column(db.String(255))
    text = db.Column(db.String(255))
    shop_url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __init__(
            self, id=None, title=None, alt=None, text=None,
            shop_url=None, image_url=None):
        self.id = id
        self.title = title
        self.alt = alt
        self.text = text
        self.shop_url = shop_url
        self.image_url = image_url
