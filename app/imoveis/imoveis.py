from flask import Blueprint, render_template, request

bp_imoveis = Blueprint("Imoveis", __name__, template_folder='template', static_folder='static')

@bp_imoveis.route('/criar', methods=['GET', 'POST'])
def criar_imoveis():
    if request.method == 'GET':
        return render_template('criar_imovel.html')

    if request.method == 'POST':
        nome = request.form.get('nome')
        endereco = request.form.get('endereco')
        tipo = request.form.get('tipo')
        preco = request.form.get('preco')
        contrato = request.form.get('contrato')
        return 'dados recebidos'


