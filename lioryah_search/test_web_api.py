

# from pathlib import Path
# import sys
# _me_parent = Path(__file__).absolute().parent.parent
# sys.path.append(_me_parent)



def test_read_main2():
    from fastapi.testclient import TestClient
    from fapi_server import app
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["msg"] == {"Hello": "World"}
