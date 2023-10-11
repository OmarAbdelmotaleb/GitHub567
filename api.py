import requests
import json


def getRepos(userID):
    r = requests.get(f"https://api.github.com/users/{userID}/repos")
    # Code 200 is successful
    if r.status_code == 200:
        repos_json = r.json()
        for repo in repos_json:
            commits = requests.get(f"https://api.github.com/repos/{userID}/{repo['name']}/commits")
            if commits.status_code == 200:
                print(f"Repo: {repo['name']} Number of commits: {len(commits.json())}")
            # Code 409 means no commits
            elif commits.status_code == 409: 
                print(f"Repo: {repo['name']} Number of commits: 0")
            else:
                print(f"ERROR: Failed to get commits for repo {repo['name']} with status code {commits.status_code}")
        return r.status_code
    else:
        print("ERROR: Status code ", r.status_code)
        return r.status_code

if __name__ == "__main__":
    userID = str(input("Please input a GitHub userID: "))
    getRepos(userID)