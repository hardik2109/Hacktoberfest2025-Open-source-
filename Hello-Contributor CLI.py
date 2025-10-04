#!/usr/bin/env python3
# hello_contributor.py
import os
import sys
from pathlib import Path

def create_contributing(project_name: str):
    content = f"""# Contributing to {project_name}

Thanks for wanting to contribute!  
Steps:
1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes & tests
4. Create a PR describing your changes
"""
    Path("CONTRIBUTING.md").write_text(content)
    print("Created CONTRIBUTING.md")

def main():
    name = input("Your name: ").strip() or "Friend"
    project = input("Project name (for CONTRIBUTING.md): ").strip() or "MyProject"
    print(f"Hello, {name}! Welcome to {project} 👋")
    create_contributing(project)

if __name__ == "__main__":
    main()
