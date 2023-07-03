from flask import Flask
from src.fib import fib

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>This page is returning Fibonacci numbers!</p>'


@app.route('/num/<int:cnt>')
def get_fib(cnt):
    fib_gen = fib()
    res = [next(fib_gen) for _ in range(cnt)]
    return res