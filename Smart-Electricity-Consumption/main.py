"""
main.py

Project Entry Point

This file launches the Streamlit web application.
"""

import subprocess
import os


def run_application():
    """
    Launch the Streamlit application.
    """

    project_directory = os.path.dirname(os.path.abspath(__file__))

    app_path = os.path.join(project_directory, "app", "app.py")

    subprocess.run(
        [
            "streamlit",
            "run",
            app_path
        ]
    )


if __name__ == "__main__":
    run_application()