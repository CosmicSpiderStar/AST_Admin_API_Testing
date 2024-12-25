from api_requests.api import AstApi

ast = AstApi()


def test_get_audio():
    status, result = ast.get_audio()
    assert status == 200, 'Ожидался статус 200, но сервер вернул другой код.'
    assert 'status' in result, "Ключ 'status' отсутствует в ответе."


def test_get_books():
    status, result = ast.get_books()
    assert status == 200, 'Ожидался статус 200, но сервер вернул другой код.'
    assert 'status' in result, "Ключ 'status' отсутствует в ответе."

def test_get_books_picture():
    status, result = ast.get_books_picture()
    assert status == 200, 'Ожидался статус 200, но сервер вернул другой код.'
    assert 'status' in result, "Ключ 'status' отсутствует в ответе."


def test_get_reviews_picture():
    status, result = ast.get_reviews_picture()
    assert status == 200, 'Ожидался статус 200, но сервер вернул другой код.'
    assert 'status' in result, "Ключ 'status' отсутствует в ответе."


def test_get_reviews():
    status, result = ast.get_reviews()
    assert status == 200, 'Ожидался статус 200, но сервер вернул другой код.'
    assert 'status' in result, "Ключ 'id' отсутствует в ответе."
