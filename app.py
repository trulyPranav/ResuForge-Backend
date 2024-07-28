from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_top_repos():

    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({'error': 'Username field is required'}), 400

    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from GitHub'}), response.status_code

    repos = response.json()
    repos = [repo for repo in repos if repo.get('name') != username]

    # Sort repositories by the number of stars (in descending order)
    sorted_repos = sorted(repos, key=lambda x: x.get('stargazers_count', 0), reverse=True)

    top_repos = sorted_repos[:3]

    result = []
    for repo in top_repos:
        repo_data = {
            'name': repo.get('name'),
            'description': repo.get('description', 'No description'),
            'stars': repo.get('stargazers_count', 0)
        }
        result.append(repo_data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
