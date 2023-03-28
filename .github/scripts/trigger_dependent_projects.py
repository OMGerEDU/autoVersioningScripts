import os
from github import Github

def main():
    gh_token = os.environ['GITHUB_TOKEN']
    github = Github(gh_token)

    search_query = 'topic:autoversioning-dependent'
    repositories = github.search_repositories(query=search_query)

    for repo in repositories:
        print(f'Triggering update for {repo.full_name}')
        repo.create_dispatch('update-versioning-scripts')

if __name__ == "__main__":
    main()
