# DevScope

DevScope is a **GitHub Profile Analyzer**. You give it a GitHub username, and it
uses the GitHub API to pull together that user's public profile and repositories.
The long-term goal is to add AI that reads this information and gives personalized
career recommendations.

This project is being built step by step as a learning exercise, starting with the
backend foundation.

## Current Features

Right now DevScope can:

- Look up a GitHub user's **profile** (name, bio, public repo count, followers, following, profile & avatar URLs).
- List all of the user's **public repositories** with language, star count, and forks.
- Fall back to a repo's **README** for a summary when it has no description.
- Print clear **logs** in the terminal so you can see each API call as it happens.
- Handle common problems gracefully: empty usernames, users that don't exist,
  GitHub rate limits, connection errors, and timeouts.

## Planned Features

- A Flask web page where you type a username and see the results in your browser.
- Saving results to a database.
- AI-powered career recommendations based on your languages and projects.

## Requirements

- Python 3
- The packages listed in `requirements.txt`

## Setup

It's best to install the packages inside a virtual environment so they stay
separate from the rest of your computer.

```bash
# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate it (Mac / Linux)
source venv/bin/activate

# 3. Install the required packages
pip install -r requirements.txt
```

> On Windows, activate the environment with `venv\Scripts\activate` instead.

## How to Run

With the virtual environment activated, run:

```bash
python github_api.py
```

The program will ask you to enter a GitHub username, then print the profile
information and repository list.

### Example

```
Enter a GitHub username: octocat

GitHub Profile Information
--------------------------
Username:     octocat
Name:         The Octocat
Public Repos: 8
Followers:    23369
...
```

## Notes

- DevScope currently uses the GitHub API **without a token**, which is limited to
  60 requests per hour. Since fetching a README counts as an extra request per
  repo, very active users can hit this limit. A GitHub token (added later) raises
  the limit to 5,000 requests per hour.
