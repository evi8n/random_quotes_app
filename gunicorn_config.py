# gunicorn_config.py
workers = 3
bind = "0.0.0.0:5000"
chdir = "random_quotes_app"