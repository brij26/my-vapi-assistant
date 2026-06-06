import requests
import base64
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

USERNAME = os.getenv("GITHUB_USERNAME")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# =========================
# README
# =========================

def get_readme(repo_name):

    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/readme"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return "README not found."

    data = response.json()

    content = data["content"]

    decoded = base64.b64decode(content)

    return decoded.decode("utf-8")[:5000]

# =========================
# COMMITS
# =========================

def get_commits(repo_name):

    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/commits"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return "Commits not found."

    commits = response.json()[:5]

    result = []

    for commit in commits:

        msg = commit["commit"]["message"]

        result.append(msg)

    return "\n".join(result)

# =========================
# REPO DETAILS
# =========================

def get_repo_details(repo_name):

    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return "Repository not found."

    data = response.json()

    return f"""
Repository Name:
{data['name']}

Description:
{data['description']}

Primary Language:
{data['language']}

Stars:
{data['stargazers_count']}
"""