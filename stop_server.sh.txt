#!/bin/bash
echo "Stopping existing tourism app..."
pkill -f "app.py" || true
