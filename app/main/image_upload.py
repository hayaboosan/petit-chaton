import cloudinary
import cloudinary.uploader
from pprint import pprint
from dotenv import load_dotenv
import os


def main(path, name):
    load_dotenv('.env')
    cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET')
    )

    res = cloudinary.uploader.upload(
        file=path,
        public_id=name
    )

    pprint(res['url'])
