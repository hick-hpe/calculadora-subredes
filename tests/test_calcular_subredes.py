import pytest
import requests
from src.data import testes


@pytest.mark.parametrize("caso", testes)
def test_calcular_subredes(caso):

    url = "http://localhost:5000/subredes"

    # envia os dados do caso de teste
    payload = {
        "endereco_ip": caso["entrada"]["endereco_ip"],
        "mascara": caso["entrada"]["mascara"],
    }

    response = requests.post(url, json=payload)

    assert (
        response.status_code == 200
    ), f"A API falhou com status {response.status_code} para a entrada {payload} --> {response.json().get('error', 'Erro desconhecido')}"

    dados_api = response.json()

    # valida a saida esperada na lista de testes
    assert dados_api["endereco_ip_binario"] == caso["saida"]["endereco_ip_binario"]
    assert dados_api["mascara_prefixo"] == caso["saida"]["mascara_prefixo"]
    assert dados_api["mascara_decimal"] == caso["saida"]["mascara_decimal"]
    assert dados_api["mascara_binario"] == caso["saida"]["mascara_binario"]
    assert dados_api["endereco_rede"] == caso["saida"]["endereco_rede"]
    assert dados_api["endereco_broadcast"] == caso["saida"]["endereco_broadcast"]
    assert dados_api["quantidade_hosts"] == caso["saida"]["quantidade_hosts"]
    assert dados_api["faixa_hosts"] == caso["saida"]["faixa_hosts"]
