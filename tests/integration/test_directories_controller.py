def test_get_method(client):
    response = client.get('/directories')
    assert response.status_code == 200
    assert b'["avava", "binaryfilesfolder", "bufferfilesfolder"]' in response.data


def test_get_method_error(client):
    response = client.get('/directories?path=/asdas')
    response.status_code = 400


def test_post_method(client):
    response = client.post('/directories?path=/a/b')
    assert response.status_code == 201

    response = client.post('/directories?path=/c')
    assert response.status_code == 201

    response = client.get('/directories')
    assert response.status_code == 200
    assert b'"a", "avava", "binaryfilesfolder", "bufferfilesfolder", "c"' in response.data

    response = client.get('/directories?path=/a')
    assert response.status_code == 200
    assert b'"b"' in response.data


def test_post_method_error(client):
    response = client.post('/directories?path=/asdas/ababa')
    response.status_code = 400


def test_put_method(client):
    response = client.post('/directories?path=/a/b')
    assert response.status_code == 201

    response = client.post('/directories?path=/c')
    assert response.status_code == 201

    response = client.put('/directories?path=/a/b&newPath=/c')
    assert response.status_code == 200

    response = client.get('/directories?path=/a')
    assert response.status_code == 200
    assert b'' in response.data

    response = client.get('/directories?path=/c')
    assert response.status_code == 200
    assert b'"b"' in response.data


def test_put_method_error(client):
    response = client.put('/directories?path=/asdas/ababa&newPath=/c')
    response.status_code = 400


def test_delete_method(client):
    response = client.post('/directories?path=/a/b')
    assert response.status_code == 201

    response = client.post('/directories?path=/c')
    assert response.status_code == 201

    response = client.delete('/directories?path=/a')
    assert response.status_code == 200

    response = client.get('/directories')
    assert response.status_code == 200
    assert b'"c"' in response.data


def test_delete_method_error(client):
    response = client.delete('/directories?path=/asdas/abab')
    response.status_code = 400
