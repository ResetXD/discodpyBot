class Client():
    def __init__(self,token) -> None:
        self.base_url = "https://api.myanimelist.net/v2"
        self.header={"Authorization":f"Bearer {token}"}