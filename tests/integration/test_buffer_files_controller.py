def test_post_method(client):
    client.post('/directories?path=/bufferfilesfolder')
    response = client.post('/bufferfiles?path=/bufferfilesfolder/bufferfile1')
    assert response.status_code == 201


def test_post_method_file_path_error(client):
    response = client.post('/bufferfiles?path=/avava/bufferfile1')
    response.status_code = 400


def test_post_method_already_exist_error(client):
    response = client.post('/bufferfiles?path=/bufferfilesfolder/bufferfile1')
    response.status_code = 400


def test_put_method(client):
    response = client.put('/bufferfiles?path=/bufferfilesfolder/bufferfile1&content=content1')
    assert response.status_code == 200


def test_put_method_file_path_error(client):
    response = client.post('/bufferfiles?path=/avava/bufferfile1')
    response.status_code = 400


def test_put_method_permission_error(client):
    response = client.post('/bufferfiles?path=/avava')
    response.status_code = 400


def test_get_method(client):
    response = client.get('/bufferfiles?path=/bufferfilesfolder/bufferfile1')
    assert response.status_code == 200
    assert b'content1' in response.data


def test_get_method_file_path_error(client):
    response = client.get('/bufferfiles?path=/avava/bufferfile1')
    response.status_code = 400


def test_delete_method(client):
    response = client.delete('/bufferfiles?path=/bufferfilesfolder/bufferfile1')
    assert response.status_code == 200


def test_delete_method_error(client):
    response = client.delete('/bufferfiles?path=/avava/bufferfile1')
    assert response.status_code == 400