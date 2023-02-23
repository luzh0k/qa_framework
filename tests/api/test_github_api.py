import pytest
import requests
from modules.api.clients.github import GitHub
from  modules.common import generate_data
from dotenv import load_dotenv
import os
import json
# check that we can find existing user
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

# Check that we can't find non-existing user
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('ksuhaluzhanska')
    assert r['message'] == 'Not Found'

# check we can find existing repo
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')

    assert r['total_count'] == 32
    assert 'become-qa-auto' in r['items'][0]['name']
 
# Check we can't find non-existing repo
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('ksuhaluzhanska_repo_non_exists')

    assert r['total_count'] == 0

# Check search works with one symbol, as a repo name
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')

    assert r['total_count'] != 0

# Positive case: we can create new repo with valid data and we can  select it after creating

@pytest.mark.api
def test_new_repo_can_be_creating(github_api):
    name = generate_data.generate_reponame()
    description = 'My test for autocreating repo'
    r = github_api.create_repo(name, description)
    os.environ["repo_name"] = name
    assert r['name'] == name
    assert r['owner']['login'] == os.getenv("owner")
    assert r['description'] == description
    r = github_api.get_user_repo(name)
    assert r['full_name'] == os.getenv("owner")+'/'+name


# Negative case: we can't create new repo with duplicated name
@pytest.mark.api
def test_impossible_create_two_repo_with_the_same_name(github_api):
    name = os.getenv("repo_name")
    description = 'My test for autocreating repo'
    r = github_api.create_repo(name, description)
    assert r['message'] == "Repository creation failed."
    assert r['errors'][0]['message'] == "name already exists on this account"

# Positive case: we can delete existing repo with and we can't  select it after deleting
@pytest.mark.api
def test_repo_can_be_deleted(github_api):
    name = os.getenv("repo_name")
    r = github_api.delete_repo(name)
    r = github_api.get_user_repo(name)
    assert r['message'] == 'Not Found'