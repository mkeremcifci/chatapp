
from unittest.mock import patch
import requests
from request import getToken


@patch('requests.post')
def test_get_token_success(mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"access_token": "fake_token_value"}

    token = getToken()  

    assert token == "fake_token_value"  
    mock_post.assert_called_once_with(  
        "http://127.0.0.1:8000/token",
        json={"username": "kerem", "password": "password"}
    )


@patch('requests.post')
def test_get_token_failure(mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 400  
    mock_response.text = "Bad Request"

    token = getToken()  

    assert token is None  
    mock_post.assert_called_once_with(
        "http://127.0.0.1:8000/token",
        json={"username": "kerem", "password": "password"}
    )

