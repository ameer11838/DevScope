import requests

# GitHub username to analyze
username = "ameer11838"

# GitHub API URL
url = f"https://api.github.com/users/{username}"

# Send GET request
response = requests.get(url)

# Convert JSON response into a dictionary
data = response.json()

# Print the whole JSON response
print(data)
