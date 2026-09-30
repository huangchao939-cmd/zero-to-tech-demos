import json

site_name = "Zero to Tech"

def get_site_name():
    data = {
        "site_name": site_name,
        "message": "Welcome to Zero to Tech!"}
    return json.dumps(data)

print(get_site_name())