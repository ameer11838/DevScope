import requests

username = "ameer11838"

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Username:", data["login"])
print("Public Repositories:", data["public_repos"])
print("Followers:", data["followers"])