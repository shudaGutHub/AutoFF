import os

# Define the project structure
project_structure = {
    "eeg_summary_generator": {
        "app.py": "",
        "utils": {
            "__init__.py": "",
            "data_loader.py": "",
            "eeg_processor.py": "",
            "openai_interface.py": "",
            "perplexity_interface.py": "",
            "anthropic_interface.py": "",
            "observable_generator.py": "",
        },
        "models": {
            "__init__.py": "",
            "eeg_data.py": "",
            "summary_report.py": "",
        },
        "tests": {
            "__init__.py": "",
            "test_data_loader.py": "",
            "test_eeg_processor.py": "",
            "test_openai_interface.py": "",
            "test_perplexity_interface.py": "",
            "test_anthropic_interface.py": "",
        },
        "static": {
            "js": {
                "observable_embed.js": "",
            },
            "css": {
                "styles.css": "",
            },
        },
    },
    "README.md": "",
    "requirements.txt": "",
    ".env": "",
    ".gitignore": "",
}

# Required packages
required_packages = [
    "streamlit",
    "mne",
    "pydantic",
    "scikit-learn",
    "pandas",
    "numpy",
    "openai",
    "anthropic",
    "python-dotenv",
    "pytest",
    "pyedflib",
    "PyPDF2",
    "requests",  # For Perplexity AI API calls
]

def create_project_structure(base_path, structure):
    for item, sub_item in structure.items():
        path = os.path.join(base_path, item)
        if isinstance(sub_item, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, sub_item)
        else:
            with open(path, 'w') as f:
                f.write(sub_item)

# Create the project structure
create_project_structure(".", project_structure)

# Create requirements.txt
with open("requirements.txt", "w") as f:
    for package in required_packages:
        f.write(f"{package}\n")

# Create .gitignore
gitignore_content = """
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
*.env

# Streamlit
.streamlit/

# IDEs
.vscode/
.idea/

# Misc
.DS_Store
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content)

# Create .env template
env_template = """
OPENAI_API_KEY=your_openai_api_key_here
PERPLEXITY_API_KEY=your_perplexity_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
"""

with open(".env", "w") as f:
    f.write(env_template)

print("Project structure created successfully!")