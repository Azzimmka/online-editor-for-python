#!/bin/bash
set -e

# Run database migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Ensure admin user or seed tasks if necessary (optional)
# python manage.py seed_tasks

# Start the application using argument passed or default CMD
exec "$@"
