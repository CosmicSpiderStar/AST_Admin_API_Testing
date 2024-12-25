import os

from dotenv import load_dotenv

load_dotenv()

valid_login = os.getenv('valid_login')
valid_password = os.getenv('valid_password')
wrong_id = os.getenv('wrong_id')
wrong_format = os.getenv('wrong_format')
wrong_picture_path = os.getenv('wrong_picture_path')
right_id = os.getenv('right_id')
right_id_2 = os.getenv('right_id_2')