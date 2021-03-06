import json
import requests

from .base import OAuthHandler

class GitHub(OAuthHandler):
    def __init__(self, client_id, client_secret):
        super().__init__(
        'GitHub',
        'https://github.com/login/oauth/authorize',
        'https://github.com/login/oauth/access_token',
        client_id,
        client_secret
        )

    def get_user_data(self, code):
        resp = requests.get(self.access_token_url, params={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": "",
            "state": self.state
        }, headers={
            "Accept": "application/json"
        })

        access_token = json.loads(resp.content)["access_token"]

        resp = requests.get("https://api.github.com/user", headers={
            "Authorization": f"token {access_token}"
        })

        user = json.loads(resp.content)
        email, github_id, avatar = user['email'], user['id'],user['avatar_url']

        # Some GitHub users don't want their email to be publicly available so we'll just create a fake email based on their GitHub ID
        if not email:
            email = f"f-gh-{github_id}@theangrydev.io"

        return (email, avatar)