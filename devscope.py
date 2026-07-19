import requests
import pandas as pd
import sqlalchemy as db

username = "ameer11838"

url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()

# Convert the dictionary into a DataFrame
df = pd.DataFrame([data])

# Create the database
engine = db.create_engine("sqlite:///devscope.db")

# Store the data
df.to_sql("github_profile", con=engine, if_exists="replace", index=False)

# Read it back and print it
with engine.connect() as connection:
    result = connection.execute(db.text("SELECT * FROM github_profile"))
    print(pd.DataFrame(result))