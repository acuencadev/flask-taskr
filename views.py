import sqlite3
from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config.from_object("_config")


# helper functions
def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


if __name__ == '__main__':
    app.run()
