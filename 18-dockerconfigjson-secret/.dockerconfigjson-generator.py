import base64
import json

encoding = 'utf-8'

username = "mock"
password = "mock"
email = "mock@example.com"
server = "https://index.docker.io/v1/"

auth_str = f"{username}:{password}"
auth_bytes = auth_str.encode(encoding)
auth_base64 = base64.b64encode(auth_bytes).decode(encoding)

dockerconfigjson_dict = {
    "auths": {
        server: {
            "auth": auth_base64,
            "email": email,
            "username": username,
            "password": password
        }
    }
}

dockercconfigjson_json = json.dumps(dockerconfigjson_dict)
# print(dockercfg_json)
dockercconfigjson_json_base64 = base64.b64encode(dockercconfigjson_json.encode(encoding)).decode(encoding)
print(dockercconfigjson_json_base64)