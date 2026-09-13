#!/usr/bin/env bash
# OmniDirector-H3: One-Click GitHub Publishing Script

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

echo "=================================================="
echo " OmniDirector-H3: GitHub Publishing Assistant"
echo " Working Directory: $REPO_DIR"
echo "=================================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository with default branch 'main'..."
    git init -b main
fi

# Set local git config if not set
if ! git config user.name > /dev/null 2>&1; then
    echo "Setting local git user.name..."
    git config user.name "OmniDirector-Team"
fi
if ! git config user.email > /dev/null 2>&1; then
    echo "Setting local git user.email..."
    git config user.email "omnidirector@users.noreply.github.com"
fi

# Stage and commit all files
echo "Staging files..."
git add .
if git diff --cached --quiet; then
    echo "No changes to commit."
else
    echo "Committing initial release..."
    git commit -m "feat: initial release of OmniDirector-H3 industrial production pipeline"
fi

echo ""
echo "--------------------------------------------------"
echo "Choose your GitHub publishing method:"
echo "--------------------------------------------------"
echo "Option A (Recommended if you have GitHub CLI):"
echo "  1. Run: gh auth login"
echo "  2. Run: gh repo create OmniDirector-H3 --public --source=. --remote=origin --push"
echo ""
echo "Option B (Using existing remote GitHub repository URL):"
echo "  1. Create a new empty repo on https://github.com/new named 'OmniDirector-H3'"
echo "  2. Run:"
echo "     git remote add origin https://github.com/egguy886/OmniDirector-H3.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo "=================================================="
