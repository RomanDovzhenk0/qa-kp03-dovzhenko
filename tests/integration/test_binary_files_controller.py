def test_post_method(client):
    client.post('/directories?path=/binaryfilesfolder')
    response = client.post('/binaryfiles?path=/binaryfilesfolder/binaryfile1&content=content1')
    assert response.status_code == 201


def test_post_method_file_path_error(client):
    response = client.post('/binaryfiles?path=/avava/binaryfile1&content=content1')
    response.status_code = 400


def test_post_method_already_exist_error(client):
    response = client.post('/binaryfiles?path=/binaryfilesfolder/binaryfile1&content=content1')
    response.status_code = 400


def test_get_method(client):
    response = client.get('/binaryfiles?path=/binaryfilesfolder/binaryfile1')
    assert response.status_code == 200
    assert b'content1' in response.data


def test_get_method_file_path_error(client):
    response = client.get('/binaryfiles?path=/avava/binaryfile1')
    response.status_code = 400


def test_get_method_permission_error(client):
    response = client.get('/binaryfiles?path=/avava')
    response.status_code = 400


def test_delete_method(client):
    response = client.delete('/binaryfiles?path=/binaryfilesfolder/binaryfile1')
    assert response.status_code == 200


def test_delete_method_error(client):
    response = client.delete('/binaryfiles?path=/avava/binaryfile1')
    assert response.status_code == 400