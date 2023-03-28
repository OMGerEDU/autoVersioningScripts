import os
import requests
from github import Github

def main():
    gh_token = os.environ['ACCESS_TOKEN']
    github = Github(gh_token)

    search_query = 'topic:autoversioning-dependent'
    repositories = github.search_repositories(query=search_query)

    headers = {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Authorization': f'token {gh_token}'
    }

    for repo in repositories:
        print(f'Triggering update for {repo.full_name}')
        url = f'https://api.github.com/repos/{repo.full_name}/dispatches'
        payload = {'event_type': 'update-versioning-scripts'}
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 204:
            print(f'Successfully triggered update for {repo.full_name}')
        else:
            print(f'Error triggering update for {repo.full_name}. Status code: {response.status_code}')

if __name__ == "__main__":
    main()
