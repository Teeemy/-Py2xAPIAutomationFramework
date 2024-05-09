# in the  utils we can create a class or functions.
# we can keep common headers or utilities here. such as json,xml,text etc

class Util(object):  # create using class
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_header_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth_value),
        }
        return headers

    def common_header_put_patch_delete_cookie(self,token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass  # creating using class '

    def read_database_file(self):
        pass


def common_headers_json():  # create using function
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers


def common_headers_put_patch_delete_basic_auth():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers


def common_header_put_patch_delete_cookie(token):
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + str(token),
    }
    return headers


def read_csv_file():
    pass


def read_env_file():
    pass


def read_database_file():
    pass
