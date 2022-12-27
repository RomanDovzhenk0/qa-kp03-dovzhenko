def test_post_method(client):
    client.post('/directories?path=/logtextfilesfolder')
    response = client.post('/logtextfiles?path=/logtextfilesfolder/logtextfile1')
    assert response.status_code == 201


def test_post_method_file_path_error(client):
    response = client.post('/logtextfiles?path=/avava/logtextfile1')
    response.status_code = 400


def test_post_method_already_exist_error(client):
    response = client.post('/logtextfiles?path=/logtextfilesfolder/logtextfile1')
    response.status_code = 400


def test_put_method(client):
    response = client.put('/logtextfiles?path=/logtextfilesfolder/logtextfile1&content=content1')
    assert response.status_code == 200


def test_put_method_file_path_error(client):
    response = client.post('/logtextfiles?path=/avava/logtextfile1')
    response.status_code = 400


def test_put_method_permission_error(client):
    response = client.post('/logtextfiles?path=/avava')
    response.status_code = 400


def test_get_method(client):
    response = client.put('/logtextfiles?path=/logtextfilesfolder/logtextfile1&content=content2')
    assert response.status_code == 200
    response = client.get('/logtextfiles?path=/logtextfilesfolder/logtextfile1')
    assert response.status_code == 200
    assert b'content1' in response.data
    response = client.get('/logtextfiles?path=/logtextfilesfolder/logtextfile1')
    assert response.status_code == 200
    assert b'content2' in response.data


def test_get_method_file_path_error(client):
    response = client.get('/logtextfiles?path=/avava/logtextfile1')
    response.status_code = 400


def test_get_method_permission_error(client):
    response = client.get('/logtextfiles?path=/avava')
    response.status_code = 400


def test_delete_method(client):
    response = client.delete('/logtextfiles?path=/logtextfilesfolder/logtextfile1')
    assert response.status_code == 200


def test_delete_method_error(client):
    response = client.delete('/logtextfiles?path=/avava/logtextfile1')
    assert response.status_code == 400