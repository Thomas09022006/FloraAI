"""
FloraAI - Deployment Module
Provides deployment guides, git instructions, and execution commands.
"""

def get_deployment_instructions() -> dict:
    """Returns deployment steps and code blocks."""
    return {
        "local_run": [
            "git clone https://github.com/Thomas09022006/FloraAI.git",
            "cd FloraAI",
            "pip install -r requirements.txt",
            "streamlit run app.py"
        ],
        "streamlit_cloud": [
            "1. Push repository to GitHub.",
            "2. Log in to share.streamlit.io",
            "3. Click 'New App' and select repository: FloraAI",
            "4. Main file path: app.py",
            "5. Click 'Deploy!'"
        ]
    }
