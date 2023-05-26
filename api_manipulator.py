import requests, base64

class SwaggerClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def make_request(self, method, path, data=None, params=None):
        headers = {
            "Content-Type": "application/json",
            "token": self.token
        }
        url = self.base_url + path
        print(url)
        try:
            response = requests.request(method, url, json=data, headers=headers, params=params, timeout=1.5)
            if response.status_code == 200:
                if "token" in response.headers:
                    token_value = response.headers['token']
                    try:
                        response_json = response.json()
                        # print(1)
                    except requests.exceptions.JSONDecodeError:
                        response_json = {}
                        # print(2)

                    if response_json:
                        response_json.update({"token": token_value})
                        # print(response_json)
                    else:
                        response_json = {"token": token_value}
                        # print(response_json)


                    return response_json
                else:
                    return response.json()
        except requests.Timeout:
            print("Timeout occurred")
            return False

    def updateUser(self, id, fullName, bio):
        data = {
            "id": id,
            "fullName": fullName,
            "bio": bio
        }
        return self.make_request("put", "api/auth/change/update", data)

    def updateRole(self, id, role):
        data = {
            "id": id,
            "role": role
        }
        print(data)
        return self.make_request("post", "api/auth/change/role", data)

    def simpleSignUp(self, email):
        data = {
            "email": email
        }
        return self.make_request("post", "api/auth/signUp/sendEmail", data)

    def signUp(self, fullName, email, bio, code, password):
        data = {
            "fullName": fullName,
            "email": email,
            "bio": bio,
            "code": code,
            "password": password
        }
        return self.make_request("post", "api/auth/signUp/full", data)

    def confirmEmail(self, email, code):
        data = {
            "email": email,
            "code": code
        }
        return self.make_request("post", "api/auth/signUp/confirmEmail", data)

    def signIn(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        return self.make_request("post", "api/auth/signIn", data)

    def changePassword(self, id, password):
        data = {
            "id": id,
            "password": password
        }
        return self.make_request("post", "api/auth/change/password", data)

    def getCurrent(self):
        return self.make_request("get", "api/auth/self")

    def getAllUsers(self):
        return self.make_request("get", "api/auth/all")

    def deleteUser(self, userId):
        params = {
            "userId": userId
        }
        return self.make_request("delete", "api/auth/deleteUser", params=params)
    def searchEmail(self, email):
        params = {
            "email": email
        }
        return self.make_request("post", "api/auth/search/email", params=params)
    def getUserbyID(self, id):
        params = {
            "id": id
        }
        return self.make_request("post", "api/auth/byId", params=params)
class analyticsClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, path, data=None, params=None):
        url = self.base_url + path
        print(url)
        try:
            response = requests.request(method, url, json=data, params=params, timeout=1.5)
            # print(response.status_code)
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    return response_json
                except requests.exceptions.JSONDecodeError:
                    return False
            else:
                return False
        except requests.Timeout:
            print("Timeout occurred")
            return False

    def getAllUsers(self):
        return self.make_request("get", "api/get")