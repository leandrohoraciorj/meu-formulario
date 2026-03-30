from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome'].upper()
    telefone = request.form['telefone']
    cidade = request.form['cidade'].upper()
    bairro = request.form['bairro'].upper()

    print(nome, telefone, cidade, bairro)  # depois vamos salvar no sheet

    return render_template('form.html', sucesso=True)

if __name__ == '__main__':
    app.run()