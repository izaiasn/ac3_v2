import os
from flask import Flask, jsonify, request

app = Flask(_name_)


@app.route('/')
def func_primos():

    cont = 0
    num = 2
    lista = []
    while (cont <= 100):
        normal = False
        for i in range(2, num):
            if (num % i == 0):
                normal = True
                break
        if (not normal):
            cont += 1
            lista.append(num)

        num += 1

    return str(lista)


if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)