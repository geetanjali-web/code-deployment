#!/bin/bash
cd /home/ec2-user/tourism_app
echo "Installing Python dependencies..."

# Always upgrade pip first (avoids SSL / wheel issues)
python3 -m pip install --upgrade pip

# Install dependencies from requirements.txt
pip3 install -r requirements.txt
