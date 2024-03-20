from jwt import encode

def create_token(data: dict):
    token: str = encode(payload=data, key="my_secert_key", algorithm="HS256")
    return create_token
    