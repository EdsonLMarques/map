from folium import Polygon, Popup

def addRealState(lista_imoveis):
    poligonos = []
    for imovel in lista_imoveis:
        loc = imovel
        popup_content = f"<b>Imóvel:</b> {imovel.nome}<br><b>Endereço:</b> {imovel.endereco}<br><b>Preço:</b> {imovel.preco}"
        poligono = Polygon(
            locations=[(loc.lat1, loc.lon1), (loc.lat2, loc.lon2), (loc.lat3, loc.lon3), (loc.lat4, loc.lon4)],
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.4,
            popup=Popup(html=popup_content, max_width=300)
        )
        poligonos.append(poligono)
    return poligonos
    return imoveis