#
### GitHub Stars

github-stats-app/
    ├── api/
    │   └── github-stats.py     # Main API logic, compatible with Vercel
    ├── .env                    # Environment variables for local testing (e.g., GITHUB_TOKEN)
    ├── .gitignore              # Files and directories to ignore in Git
    ├── README.md               # Documentation for the project
    ├── vercel.json             # Vercel configuration file
    └── requirements.txt        # Python dependencies

This application provides an API to fetch GitHub user statistics, deployed using Vercel.

GITHUB_TOKEN=your_personal_access_token_here
GitHub Stats API

#
### Features:

Fetches user profile data from GitHub. Lists repositories sorted by stars. Displays recent public contributions.

#
### Requirements:

Python 3.8+ Flask Requests Vercel account

#
### Setup Instructions:

Clone the repository: git clone https://github.com/your-username/github-stats-app.git

Navigate to the project directory: cd github-stats-app

Install dependencies: pip install -r requirements.txt

Set up a .env file in the env/ directory with your GitHub token: GITHUB_TOKEN=your_github_personal_access_token

#
### Testing:

Run tests using pytest: pytest tests/

#
### Deployment:

Deploy the app on Vercel: vercel --prod

Access the API at: https://your-project.vercel.app/api/github-stats?username=<GitHub_username>

#
### API Endpoints:

GET /api/github-stats: Fetches GitHub user data. 
Query Parameters: username (required): GitHub username to fetch data for.

Response Format: JSON object with user profile, repositories, and contributions.