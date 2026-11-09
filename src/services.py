
def validar_endereco_ip(endereco_ip: str) -> bool:
    octetos = endereco_ip.split('.')
    if len(octetos) != 4:
        return False
    return all(0 <= int(octeto) <= 255 for octeto in endereco_ip.split('.'))


def validar_mascara(mascara: str) -> bool:
    # validar se a máscara é um prefixo ou decimal valido

    mascara_com_prefixo = mascara.startswith('/')

    if mascara_com_prefixo:
        if not mascara[1:].isdigit():
            return False
        if not (0 <= int(mascara[1:]) <= 32):
            return False
    else:
        if not all(0 <= int(octeto) <= 255 for octeto in mascara.split('.')):
            return False

    # validar se existe "1"s consecultivos
    if mascara_com_prefixo:
        mascara_binario = '1' * int(mascara[1:]) + '0' * (32 - int(mascara[1:]))
        mascara_binario = "".join([str(int(mascara_binario[i:i+8], 2)) for i in range(0, 32, 8)])
    else:
        mascara_binario = "".join([format(int(octeto), '08b') for octeto in mascara.split('.')])

    for bit in mascara_binario:
        if bit == '1':
            continue
        else:
            if '1' in mascara_binario[mascara_binario.index(bit):]:
                return False

    return True


def calcular_mascara(mascara: str) -> tuple[str, str, str]:
    mascara_com_prefixo = mascara.startswith('/')

    if mascara_com_prefixo:
        prefixo = int(mascara[1:])
        num_binaria = '1' * prefixo + '0' * (32 - prefixo)
        mascara_decimal = ".".join([str(int(num_binaria[i:i+8], 2)) for i in range(0, 32, 8)])
    else:
        mascara_decimal = mascara

    mascara_binario = ".".join([format(int(octeto), '08b') for octeto in mascara_decimal.split('.')])
    mascara_prefixo = '/' + str(mascara_binario.count('1'))

    return mascara_prefixo, mascara_decimal, mascara_binario


def calcular_subrede(endereco_ip_binario: str, mascara_binario: str) -> tuple[str, str, int, str]:

    endereco_ip_binario = endereco_ip_binario.replace('.', '')
    mascara_binario = mascara_binario.replace('.', '')

    # endereço de rede
    # print('endereco_ip_binario:', endereco_ip_binario)
    # print('mascara_binario:', mascara_binario)
    endereco_rede_binario = ''.join(
        [
            '1'
            if endereco_ip_binario[i] == '1' and mascara_binario[i] == '1'
            else '0'
            for i in range(32)
        ]
    )
    # print('endereco_ip_binario & mascara_binario:', ".".join([endereco_rede_binario[i:i+8] for i in range(0, 32, 8)]))

    # endereço de broadcast
    mascara_inversa_binario = ''.join(['0' if bit == '1' else '1' for bit in mascara_binario])
    endereco_broadcast_binario = ''.join(
        [
            '1'
            if endereco_ip_binario[i] == '1' or mascara_inversa_binario[i] == '1'
            else '0'
            for i in range(32)
        ]
    )
    qtd_hosts = 0
    faixa_hosts = ''

    # convertendo binario para decimal
    endereco_rede = ".".join([str(int(endereco_rede_binario[i:i+8], 2)) for i in range(0, 32, 8)])
    endereco_broadcast = ".".join([str(int(endereco_broadcast_binario[i:i+8], 2)) for i in range(0, 32, 8)])

    return endereco_rede, endereco_broadcast, qtd_hosts, faixa_hosts

