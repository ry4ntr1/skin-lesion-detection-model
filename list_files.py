import os

def list_files(startpath, excluded_dirs=None):
    if excluded_dirs is None:
        excluded_dirs = []

    for root, dirs, files in os.walk(startpath, topdown=True):
        # Remove excluded directories from dirs list
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        dir_name = os.path.basename(root)
        if dir_name and root != startpath:  # Skip the root directory itself
            print(f"{indent}{'-' * level} {dir_name}/")  # Formatting for directories

        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{'-' * (level + 1)} {f}")  # Formatting for files

# Exclude certain directories from the output
excluded_dirs = ['__pycache__', '.git', '.git/', 'logs', 'lesionDetection.egg-info']


list_files(os.getcwd(), excluded_dirs)
