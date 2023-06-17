from flask import Flask, render_template, request, redirect
app = Flask(__name__)
produtos = []

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro_produto', methods=['GET', 'POST'])
def cadastro_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        marca = request.form['marca']
        preco = request.form['preco']
        produto = {'nome': nome, 'marca': marca, 'preco': preco}
        produtos.append(produto)
        return redirect('/produtos')
    return render_template('cadastro_produto.html')

@app.route('/ver_produto/<int:id>')
def ver_produto(id):
    produto = produtos[id] if id < len(produtos) else None
    return render_template('ver_produto.html', produto=produto)

@app.route('/editar_produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    if request.method == 'POST':
        nome = request.form['nome']
        marca = request.form['marca']
        preco = request.form['preco']
        produto = {'nome': nome, 'marca': marca, 'preco': preco}
        if id < len(produtos):
            produtos[id] = produto
        return redirect('/produtos')
    produto = produtos[id] if id < len(produtos) else None
    return render_template('editar_produto.html', produto=produto, id=id)

@app.route('/excluir_produto/<int:id>')
def excluir_produto(id):
    if id < len(produtos):
        del produtos[id]
    return redirect('/produtos')

@app.route('/produtos')
def listar_produtos():
    return render_template('listar_produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
