
from github import Github


g = Github("")
repo = g.get_repo("Fadhilkhan04/web-analytics")

# Print repository details
print(f"Repository Name: {repo.name}")
print(f"Description: {repo.description}")
print(f"Stars: {repo.stargazers_count}")

# Get a list of contributors
for contributor in repo.get_contributors():
    print(f"{contributor.login} ({contributor.contributions} contributions)")

# Get the contents of the repository (all files and folders)
def list_files(path=""):
    contents = repo.get_contents(path)
    for content in contents:
        if content.type == "dir":
            print(f"Directory: {content.path}")
            # Recursively get files in subdirectories
            list_files(content.path)
        else:
            print(f"File: {content.path}")

# List all files and folders
list_files()
