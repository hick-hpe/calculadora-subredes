from utils import converter_ip_binario_para_decimal, converter_ip_decimal_para_binario


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
            print("[ERROR-VALIDATE-MASK] A máscara de rede deve ser um número entre 0 e 32, ou uma máscara decimal válida.")
            return False
        if not (0 <= int(mascara[1:]) <= 32):
            print("[ERROR-VALIDATE-MASK] A máscara de rede deve ser um número entre 0 e 32.")
            return False
    else:
        if not all(0 <= int(octeto) <= 255 for octeto in mascara.split('.')):
            print("[ERROR-VALIDATE-MASK] A máscara de rede deve ser um número entre 0 e 32, ou uma máscara decimal válida.")
            return False

    # validar se existe "1"s consecultivos
    if mascara_com_prefixo:
        mascara_binario = '1' * int(mascara[1:]) + '0' * (32 - int(mascara[1:]))
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


def calcular_endereco_rede(endereco_ip_binario: str, mascara_binario: str) -> str:
    endereco_ip_binario_sem_pontos = endereco_ip_binario.replace('.', '')
    mascara_binario_sem_pontos = mascara_binario.replace('.', '')

    endereco_rede_binario = ''.join(
        [
            '1'
            if endereco_ip_binario_sem_pontos[i] == '1' and mascara_binario_sem_pontos[i] == '1'
            else '0'
            for i in range(32)
        ]
    )

    endereco_rede = converter_ip_binario_para_decimal(endereco_rede_binario)
    return endereco_rede


def calcular_endereco_broadcast(endereco_ip_binario: str, mascara_binario: str) -> str:
    endereco_ip_binario_sem_pontos = endereco_ip_binario.replace('.', '')
    mascara_binario_sem_pontos = mascara_binario.replace('.', '')

    mascara_inversa_binario = ''.join(['0' if bit == '1' else '1' for bit in mascara_binario_sem_pontos])
    endereco_broadcast_binario = ''.join(
        [
            '1'
            if endereco_ip_binario_sem_pontos[i] == '1' or mascara_inversa_binario[i] == '1'
            else '0'
            for i in range(32)
        ]
    )

    endereco_broadcast = converter_ip_binario_para_decimal(endereco_broadcast_binario)
    return endereco_broadcast


def obter_tipo_mascara(mascara_binario: str) -> str:
    mascara_binario_sem_pontos = mascara_binario.replace('.', '')

    mascara_binario_cidr_31 = '1' * 31 + '0'
    mascara_binario_cidr_32 = '1' * 32

    if mascara_binario_sem_pontos == mascara_binario_cidr_31:
        return "CIDR /31"
    elif mascara_binario_sem_pontos == mascara_binario_cidr_32:
        return "CIDR /32"
    else:
        return "Máscara padrão"


def calcular_quantidade_hosts(mascara_binario: str) -> int:

    tipo_mascara = obter_tipo_mascara(mascara_binario)

    if tipo_mascara == "CIDR /31":
        return 2
    elif tipo_mascara == "CIDR /32":
        return 1
    else:
        mascara_inversa_binario = mascara_binario.replace('.', '').replace('1', 'x').replace('0', '1').replace('x', '0')
        return 2 ** mascara_inversa_binario.count('1') - 2


def calcular_faixa_hosts(endereco_rede: str, endereco_broadcast: str, mascara_binario: str) -> str:
    mascara_binario_sem_pontos = mascara_binario.replace('.', '')

    mascara_binario_cidr_31 = '1' * 31 + '0'
    mascara_binario_cidr_32 = '1' * 32

    if mascara_binario_sem_pontos == mascara_binario_cidr_31:
        return f"{endereco_rede} a {endereco_broadcast}"
    elif mascara_binario_sem_pontos == mascara_binario_cidr_32:
        return endereco_rede
    else:
        primeiro_host_decimal = converter_ip_binario_para_decimal(
            format(
                int(converter_ip_decimal_para_binario(endereco_rede).replace('.', ''), 2) + 1,
                '032b'
            )
        )
        ultimo_host_decimal = converter_ip_binario_para_decimal(
            format(
                int(converter_ip_decimal_para_binario(endereco_broadcast).replace('.', ''), 2) - 1,
                '032b'
            )
        )
    
        return f"{primeiro_host_decimal} a {ultimo_host_decimal}"


def calcular_subrede(endereco_ip_binario: str, mascara_binario: str) -> tuple[str, str, int, str]:

    ENDERECO_NAO_DEFINIDO = "não há"

    # quantidade de hosts
    quantidade_hosts = calcular_quantidade_hosts(mascara_binario)

    # endereço de rede
    endereco_rede = calcular_endereco_rede(endereco_ip_binario, mascara_binario)

    # endereço de broadcast
    endereco_broadcast = calcular_endereco_broadcast(endereco_ip_binario, mascara_binario)
    
    # faixa de hosts
    faixa_hosts = calcular_faixa_hosts(endereco_rede, endereco_broadcast, mascara_binario)

    tipo_mascara = obter_tipo_mascara(mascara_binario)
    if tipo_mascara == "CIDR /31" or tipo_mascara == "CIDR /32":
        endereco_rede = ENDERECO_NAO_DEFINIDO
        endereco_broadcast = ENDERECO_NAO_DEFINIDO

    return endereco_rede, endereco_broadcast, quantidade_hosts, faixa_hosts
