import requests

def test_hello_mike():
    page = requests.get('http://localhost:5000/hello/mike')
    true_content = '<h1>Hello mike</h1>'

    assert str(page.text) == true_content

def test_hello_sarah():
    page = requests.get('http://localhost:5000/hello/sarah')
    true_content = '<h1>Hello sarah</h1>'

    assert str(page.text) == true_content

def test_hello_crazy():
    page = requests.get('http://localhost:5000/hello/crazy')
    true_content = '<h1>Hello crazy</h1>'

    assert str(page.text) == true_content

def test_hello_asfdasdf():
    page = requests.get('http://localhost:5000/hello/asfdasdf')
    true_content = '<h1>Hello asfdasdf</h1>'

    assert str(page.text) == true_content