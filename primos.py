import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primo():

    co = 0
    for r in range(2, 548):
        c = 0
        for v in range(1, r+1):
            if r % v == 0:
                c += 1
        if c <= 2:
            print(r, end=' > ')
            co = co + 1
    return co
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

