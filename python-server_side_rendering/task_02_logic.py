#!/usr/bin/python3
"""
    Module containing a Flask application rendering dynamic content
    with Jinja loops and conditions
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


def read_items():
    """Read the list of items from items.json"""

    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get('items', [])

    # Exception handling
    except Exception as e:
        print("An error occurred while reading items.json:", e)
        return []


@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the list of items read from items.json"""
    return render_template('items.html', items=read_items())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
