def basic_auth(username="", password=""):
    from requests.auth import HTTPBasicAuth
    return HTTPBasicAuth(username=username, password=password)

