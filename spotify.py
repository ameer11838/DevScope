import requests

CLIENT_ID = "a03a817ed5984bfba3cd4c2b26e3f35b"
CLIENT_SECRET = "24304dd15be94aad86fdfb66bbc43fc8"

AUTH_URL = "https://accounts.spotify.com/api/token"

auth_response = requests.post(AUTH_URL, {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data["access_token"]

headers = {
    "Authorization": "Bearer {token}".format(token=access_token)
}

BASE_URL = "https://api.spotify.com/v1/"

track_id = input("Enter track id: ")

r = requests.get(
    BASE_URL + "audio-features/" + track_id,
    headers=headers
)

print(r.json())