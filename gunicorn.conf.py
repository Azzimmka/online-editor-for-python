import multiprocessing

# Bind to 0.0.0.0 for Docker/DigitalOcean App Platform
bind = "0.0.0.0:8000"

# Best practice workers count for small containers
import os
workers = int(os.environ.get("WEB_CONCURRENCY", 2))

# Timeouts
timeout = 30
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
