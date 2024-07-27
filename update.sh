#!/bin/bash

VENV_HOME=venv
BRANCH=$1

if [ -z "$BRANCH" ]; then
    echo "No branch specified. Usage: ./deploy.sh <branch>"
    exit 1
fi

echo "Activating virtual environment..."
if [ -d "$VENV_HOME" ]; then
    source $VENV_HOME/bin/activate
    if [ $? -ne 0 ]; then
        echo "Failed to activate virtual environment. Aborting deployment."
        exit 1
    fi
else
    echo "Virtual environment not found. Creating one..."
    python3 -m venv $VENV_HOME
    source $VENV_HOME/bin/activate
fi

echo "Pulling from branch $BRANCH..."
git pull origin $BRANCH
if [ $? -ne 0 ]; then
    echo "Git pull failed. Aborting deployment."
    deactivate
    exit 1
fi

echo "Installing requirements..."
pip install --upgrade -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install requirements. Aborting deployment."
    deactivate
    exit 1
fi

echo "Making migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Migrations failed. Aborting deployment."
    deactivate
    exit 1
fi

echo "Collecting static content..."
python manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "Failed to collect static content. Aborting deployment."
    deactivate
    exit 1
fi

echo "Deployment successful!"
deactivate
