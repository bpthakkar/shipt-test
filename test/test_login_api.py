import requests
import json
import urllib.parse
import pytest
import logging

testdata = [({"username": "bhargavhalani@yahoo.com", "password": "ShiptTest0419", "grant_type": "password"},
                {"response_code": 200, "message": ""}),
            ({"username": "bhargavhalani@yahoo.com", "password": "ShiptTest0418", "grant_type": "password"},
                {"response_code": 401, "message": "Invalid Username or Password"}),
            ({"username": "bhargav@yahoo.com", "password": "ShiptTest0418", "grant_type": "password"},
                {"response_code": 401, "message": "Invalid Username or Password"})
            ]


@pytest.mark.parametrize("payload, expected", testdata)
def test_login(payload, expected):

    url = "https://api.shipt.com/auth/v2/oauth/token?white_label_key=shipt"

    # pare header for post request
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "cache-control": "no-cache",
        "X-User-Type": "Customer"
    }

    logging.debug("Payload" + json.dumps(payload))
    logging.debug("Expected" + json.dumps(expected))

    response = requests.post(url, data=urllib.parse.urlencode(payload), headers=headers)

    print(response.text)

    # Assert response status code based on the test data
    assert str(response.status_code) == json.dumps(expected["response_code"])

    # verify the error message if the response is not OK
    if response.status_code != 200:
        assert json.dumps(expected["message"]) in response.text

