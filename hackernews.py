import requests

# Get the list of newest item IDs
url = "https://hacker-news.firebaseio.com/v0/newstories.json"
response = requests.get(url)
stories = response.json()

# Get the newest story
story_id = stories[0]

# Get the story details
url = "https://hacker-news.firebaseio.com/v0/item/" + str(story_id) + ".json"
response = requests.get(url)
story = response.json()

# Print the details
print("Title:", story["title"])
print("Author:", story["by"])
print("Link:", story["url"])