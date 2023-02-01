import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
        
    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories',
        params = {"q": name})

        body = r.json()

        return body

    def search_user(self, name):
        r = requests.get('https://api.github.com/search/users',
        params = {"q": name})

        body = r.json()

        return body
'''
    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body

    def get_non_exist_user(self):
        r = requests.get('https://api.github.com/users/ksuhaluzhaska')
        body = r.json()

        return body
        '''