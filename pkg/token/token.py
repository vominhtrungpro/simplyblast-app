class TokenManager:
    def __init__(self):
        self._access_token = None
        self._refresh_token = None

    def set_access_token(self, token):
        self._access_token = token

    def set_refresh_token(self, token):
        self._refresh_token = token

    def get_access_token(self):
        return self._access_token
    
    def get_refresh_token(self):
        return self._refresh_token