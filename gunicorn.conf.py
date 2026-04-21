import multiprocessing

# Bind to 0.0.0.0 for Docker/DigitalOcean App Platform
bind = "0.0.0.0:8000"

# Best practice workers count = 2 * CPU cores + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Timeouts
timeout = 30
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
