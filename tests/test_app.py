from flask_boilerplate import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'This is a flask-boilerplate project, not to be used in production.'

def test_hello(client):
    # if the url has no query parameter, it should show Hello World!
    # the get function doesn't error when the value wanted to be returned does not exist
    response = client.get('/hello')
    assert response.data == b'Hello World!'

    # if Jim is in the query parameter as name, it should return Hello Jim!
    response = client.get('/hello?name=Jim')
    assert response.data == b'Hello Jim!'

def test_number(client):
    response = client.get('/number/1')
    assert response.data == b'Number: 1'

    response = client.get('/number/2')
    assert response.data == b'Number: 2'

    response = client.get('/number/hi')
    assert response.status_code == 404