from app import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    alt = db.Column(db.String(255))
    text = db.Column(db.Text)
    shop_url = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __init__(
            self, id=None, title=None, alt=None, text=None,
            shop_url=None, image_url=None):
        self.id = id
        self.title = title
        self.alt = alt
        self.text = text
        self.shop_url = shop_url
        self.image_url = image_url


class NavLink(db.Model):
    __tablename__ = 'nav_links'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    left_num = db.Column(db.Integer)
    link_url = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __init__(
            self, id=None, title=None, left_num=None, link_url=None,
            image_url=None):
        self.id = id
        self.title = title
        self.left_num = left_num
        self.link_url = link_url
        self.image_url = image_url
