"""
Calculadora de sub-redes IPv4

Desenvolva uma aplicação que receba como entrada um endereço Internet Protocol
versão 4 (IPv4) e a respectiva máscara de rede e apresente as informações da red
à qual o endereço pertence.

"""

from flask import Flask, request, jsonify, render_template
from services import calcular_mascara, calcular_subrede, validar_endereco_ip, validar_mascara

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Bem-vindo à Calculadora de Sub-redes IPv4!"})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/subredes', methods=['POST'])
def calcular_subredes():
    data = request.get_json()
    endereco_ip = data.get('endereco_ip')
    mascara = data.get('mascara')

    # validar dados
    if not endereco_ip or not mascara:
        return jsonify({"error": "Endereço IP e máscara são obrigatórios."}), 400

    if not isinstance(endereco_ip, str) or not isinstance(mascara, str):
        return jsonify({"error": "Endereço IP e máscara devem ser strings."}), 400

    # validar IP
    if not validar_endereco_ip(endereco_ip):
        return jsonify({"error": "Endereço IP inválido."}), 400

    # validar máscara
    if not validar_mascara(mascara):
        return jsonify({"error": "Máscara de rede inválida."}), 400
    
    # ip binario
    endereco_ip_binario = ".".join([format(int(octeto), '08b') for octeto in endereco_ip.split('.')])

    # calcular as mascaras
    mascara_prefixo, mascara_decimal, mascara_binario = calcular_mascara(mascara)

    # calcular endereco de rede, broadcast, quantidade de hosts e faixa de hosts
    endereco_rede, endereco_broadcast, quantidade_hosts, faixa_hosts = calcular_subrede(endereco_ip_binario, mascara_binario)

    return jsonify({
        "endereco_ip_binario": endereco_ip_binario,
        "mascara_prefixo": mascara_prefixo,
        "mascara_decimal": mascara_decimal,
        "mascara_binario": mascara_binario,
        "endereco_rede": endereco_rede,
        "endereco_broadcast": endereco_broadcast,
        "quantidade_hosts": quantidade_hosts,
        "faixa_hosts": faixa_hosts,
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)