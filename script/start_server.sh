#!/bin/bash
cd /home/ec2-user/tourism_app
echo "Starting Flask tourism app..."
# Kill old process if running
pkill -f "python3 app.py"
# Start in background
nohup python3 app.py > app.log 2>&1 &
