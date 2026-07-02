from flask import Flask, render_template

app = Flask ("Lista de Livros")

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/livros')
def livros():
    return render_template('livros.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

app.run(debug=True)
