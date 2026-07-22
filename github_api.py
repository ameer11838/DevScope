"""
DevScope - Day 1: GitHub API backend.

Fetches basic public profile info for a GitHub user via the GitHub API.
"""

import requests


def get_github_profile(username):
    """Look up a GitHub user and return their profile as a dictionary.

    On success the dict holds the profile fields. On failure it holds a
    single "error" key with a message explaining what went wrong.
    """

    # Don't bother hitting the API if there's nothing to look up.
    if not username or not username.strip():
        return {"error": "Please enter a GitHub username. It cannot be empty."}

    username = username.strip()
    url = f"https://api.github.com/users/{username}"

    # timeout keeps us from hanging forever if GitHub is slow or unreachable.
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to GitHub. Please check your internet connection."}
    except requests.exceptions.Timeout:
        return {"error": "The request to GitHub timed out. Please try again."}
    except requests.exceptions.RequestException:
        return {"error": "Something went wrong while contacting GitHub. Please try again."}

    # 200 means success, so pull out just the fields we care about.
    # Using .get() avoids a crash if GitHub leaves a field out.
    if response.status_code == 200:
        data = response.json()
        return {
            "username": data.get("login"),
            "name": data.get("name"),
            "bio": data.get("bio"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "profile_url": data.get("html_url"),
            "avatar_url": data.get("avatar_url"),
        }

    if response.status_code == 404:
        return {"error": f"GitHub user '{username}' was not found."}

    # 403 usually means we've hit GitHub's rate limit for unauthenticated requests.
    if response.status_code == 403:
        return {"error": "GitHub API rate limit reached. Please wait a while and try again."}

    return {"error": f"Unexpected response from GitHub (status code {response.status_code})."}


# Quick manual test: run this file directly to try a lookup from the terminal.
if __name__ == "__main__":
    print("=== DevScope: GitHub Profile Lookup ===")
    user_input = input("Enter a GitHub username: ")
    result = get_github_profile(user_input)

    print()
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("GitHub Profile Information")
        print("--------------------------")
        print("Username:    ", result["username"])
        print("Name:        ", result["name"])
        print("Bio:         ", result["bio"])
        print("Public Repos:", result["public_repos"])
        print("Followers:   ", result["followers"])
        print("Following:   ", result["following"])
        print("Profile URL: ", result["profile_url"])
        print("Avatar URL:  ", result["avatar_url"])
