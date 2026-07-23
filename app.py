from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    username = request.form.get("username")
    target_field = request.form.get("target_field")

    profile = {
        "username": username,
        "name": "Test User",
        "bio": "Aspiring developer",
        "avatar_url": "https://github.com/github.png",
        "followers": 42,
        "public_repos": 15
    }

    repos = [
        {"name": "cool-project", "description": "A cool project", "language": "Python", "stars": 3}
    ]

    suggestions = {
        "fit_score": 7,
        "strengths": ["Consistent commit activity", "Strong Python fundamentals"],
        "gaps": ["No API-based projects", "READMEs lack documentation"],
        "suggested_actions": [
            "Build a project using a financial data API",
            "Add detailed READMEs to top repos"
        ]
    }

    return render_template("results.html", profile=profile, repos=repos, suggestions=suggestions, target_field=target_field)

if __name__ == "__main__":
    app.run(debug=True)