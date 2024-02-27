from app import app
import folium
from flask import render_template, request, redirect, url_for
from app.imoveis.criar_poligonos import addRealState

@app.route('/')
@app.route('/index')
def mapa():
    # Criar um mapa Folium centrado em uma localização específica
    mapa = folium.Map(location=[-22.242551711272572, -45.69640872722838], zoom_start=15)

    # Criar pontos
    # imoveis = addRealState(lista, informacoes)
    # for imovel in imoveis:
    #     imovel.add_to(mapa)

    # Converter o mapa para uma string HTML
    mapa_html = mapa.get_root().render()

    # Renderizar o mapa na página index.html
    return render_template('index.html', mapa_html=mapa_html)


lista = [[[-22.247689550756, -45.70342720741], [-22.247620655379, -45.70329529419], [-22.247876178571, -45.703147362947], [-22.247937224999, -45.703268911555]],
         [[-22.24752210876, -45.70385404091] , [-22.247413969042, -45.703681611490], [-22.24756484137, -45.70355064050], [-22.247672108892, -45.7037004562]]
         ]

informacoes = [
        {'nome': 'Imóvel 1', 'endereco': 'Rua A, 123', 'preco': 200000, 'tipo': 'Casa'},
        {'nome': 'Imóvel 2', 'endereco': 'Rua B, 456', 'preco': 300000, 'tipo': 'Apartamento'}
    ]