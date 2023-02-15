import requests
import json
from dotenv import load_dotenv
import os
from  modules.common import generate_data

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
# creating new repo method
    def create_repo(self, name, description):
        load_dotenv()
        url = "https://api.github.com/user/repos"
        payload = json.dumps({
        "name": name,
        "description": description,
        "homepage": "https://github.com",
        "private": False,
        "is_template": True
        })
        headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': 'Bearer ' + os.getenv('bearer_token'),
        'Content-Type': 'application/json'
        }
        r = requests.post(url, headers=headers, data=payload)
        body = r.json()
        os.environ['repo_name'] = name
        return body

# delete repo method
    def delete_repo(self, name):
        load_dotenv()
        url = f"https://api.github.com/repos/{os.getenv('owner')}/{name}"
        headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': 'Bearer ' + os.getenv('bearer_token'),
        'Content-Type': 'application/json'
        }
        r = requests.delete(url, headers=headers)
        print("Specified repo is deleted successfully, the success code is = ", r)

# get user's repo 
    def get_user_repo(self, name):
        load_dotenv()
        url = f"https://api.github.com/repos/{os.getenv('owner')}/{name}"
        headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': 'Bearer ' + os.getenv('bearer_token'),
        'Content-Type': 'application/json'
        }
        r = requests.get(url, headers=headers)
        body = r.json()
        return body
# get List repositories for the authenticated user 
    def get_user_repos(self):
        load_dotenv()
        url = f"https://api.github.com/user/repos"
        headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': 'Bearer ' + os.getenv('bearer_token'),
        'Content-Type': 'application/json'
        }
        r = requests.get(url, headers=headers)
        body = r.json()
        return body