
def converter_ip_decimal_para_binario(endereco_ip: str) -> str:
    return ".".join([format(int(octeto), '08b') for octeto in endereco_ip.split('.')])


def converter_ip_binario_para_decimal(endereco_binario: str) -> str:
    return ".".join([str(int(endereco_binario[i:i+8], 2)) for i in range(0, 32, 8)])


def normalizar_mascara_para_decimal(mascara_str: str) -> str:
    """Garante que qualquer formato de máscara retorne sua versão decimal para conversão binária."""

    limpa = mascara_str.replace("/", "")
    if limpa.isdigit():
        prefixo = int(limpa)

        bits = ("1" * prefixo) + ("0" * (32 - prefixo))
        octetos = [str(int(bits[i:i+8], 2)) for i in range(0, 32, 8)]
        return ".".join(octetos)
    return mascara_str
