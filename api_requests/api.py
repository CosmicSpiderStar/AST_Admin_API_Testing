import json
import requests


class AstApi:
    def __init__(self):
        self.base_url = 'https://ast-13team.onrender.com/api/v1'

    def get_audio(self):
        response = requests.get(f"{self.base_url}/audio/")
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text
        return response.status_code, result

    def get_books(self):
        response = requests.get(f"{self.base_url}/books/")
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text
        return response.status_code, result

    def get_books_picture(self):
        response = requests.get(f"{self.base_url}/books-picture/")
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text
        return response.status_code, result

    def get_reviews_picture(self):
        response = requests.get(f"{self.base_url}/reviews-picture/")
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text
        return response.status_code, result
    def get_reviews(self):
        response = requests.get(f"{self.base_url}/reviews/")
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text
        return response.status_code, result

