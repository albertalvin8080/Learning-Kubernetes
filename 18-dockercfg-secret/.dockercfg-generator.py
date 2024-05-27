import base64
import json

encoding = 'utf-8'

username = "mockuser"
password = "mockpassword"
email = "mockemail@example.com"
server = "https://index.docker.io/v1/"

auth_str = f"{username}:{password}"
auth_bytes = auth_str.encode(encoding)
auth_base64 = base64.b64encode(auth_bytes).decode(encoding)

dockercfg_dict = {
    "auths": {
        server: {
            "auth": auth_base64,
            "email": email
        }
    }
}

dockercfg_json = json.dumps(dockercfg_dict)
# print(dockercfg_json)
dockercfg_json_base64 = base64.b64encode(dockercfg_json.encode(encoding)).decode(encoding)
print(dockercfg_json_base64)