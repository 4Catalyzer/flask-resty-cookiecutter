from flask_resty.testing import assert_response

from . import mock_data as d

# -----------------------------------------------------------------------------


def test_list(client):
    response = client.get('widgets')
    assert_response(response, 200, [
        {'message': 'message 1'},
        {'message': 'message 2'},
        {'message': 'message 3'},
        {'message': 'message 4'},
    ])


def test_retrieve(client):
    id = d.WIDGETS[0]['id']

    response = client.get('widgets/{}'.format(id))
    assert_response(response, 200, {
        'id': id,
        'message': 'message 1',
    })
