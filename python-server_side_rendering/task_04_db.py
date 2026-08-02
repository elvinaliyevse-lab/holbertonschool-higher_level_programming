#!/usr/bin/python3
"""
    Module containing a Flask application displaying product data
    read from a JSON file, a CSV file or a SQLite database
"""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read the list of products from products.json"""

    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_products():
    """Read the list of products from products.csv"""

    products = []
    with open('products.csv', 'r', encoding='utf-8', newline='') as file:
        for row in csv.DictReader(file):
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql_products():
    """Read the list of products from the products.db SQLite database"""

    conn = sqlite3.connect('products.db')
    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


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


@app.route('/products')
def products():
    """Render the products coming from the requested source"""

    source = request.args.get('source')
    product_id = request.args.get('id')

    readers = {
        'json': read_json_products,
        'csv': read_csv_products,
        'sql': read_sql_products
    }

    # Checking the requested source
    if source not in readers:
        return render_template('product_display.html', error="Wrong source")

    # Reading the data from the matching source
    try:
        data = readers[source]()

    # Exception handling
    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error="Database error: {}".format(e))
    except Exception as e:
        return render_template('product_display.html',
                               error="Error reading {} data: {}".format(
                                   source, e))

    # Filtering by id when one is provided
    if product_id is not None:
        try:
            wanted = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")

        data = [item for item in data if item.get('id') == wanted]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
