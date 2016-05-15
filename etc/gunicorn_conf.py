bind = "0.0.0.0:80"
logfile = "/tmp/outbreak.gunicorn.log"
workers = 1
timeout = 120
accesslog = "/tmp/outbreak.access.log"
errorlog = "/tmp/outbreak.error.log"
