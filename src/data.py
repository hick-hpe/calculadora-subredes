testes = [
    {
        "entrada": {
            "endereco_ip": "192.168.10.85",
            "mascara": "255.255.255.192"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00001010.01010101",
            "mascara_prefixo": "/26",
            "mascara_decimal": "255.255.255.192",
            "mascara_binario": "11111111.11111111.11111111.11000000",
            "endereco_rede": "192.168.10.64",
            "endereco_broadcast": "192.168.10.127",
            "quantidade_hosts": 62,
            "faixa_hosts": "192.168.10.65 a 192.168.10.126"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.1.50",
            "mascara": "255.255.255.0"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00000001.00110010",
            "mascara_prefixo": "/24",
            "mascara_decimal": "255.255.255.0",
            "mascara_binario": "11111111.11111111.11111111.00000000",
            "endereco_rede": "192.168.1.0",
            "endereco_broadcast": "192.168.1.255",
            "quantidade_hosts": 254,
            "faixa_hosts": "192.168.1.1 a 192.168.1.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "172.16.45.12",
            "mascara": "/16"
        },
        "saida": {
            "endereco_ip_binario": "10101100.00010000.00101101.00001100",
            "mascara_prefixo": "/16",
            "mascara_decimal": "255.255.0.0",
            "mascara_binario": "11111111.11111111.00000000.00000000",
            "endereco_rede": "172.16.0.0",
            "endereco_broadcast": "172.16.255.255",
            "quantidade_hosts": 65534,
            "faixa_hosts": "172.16.0.1 a 172.16.255.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "10.0.0.5",
            "mascara": "/30"
        },
        "saida": {
            "endereco_ip_binario": "00001010.00000000.00000000.00000101",
            "mascara_prefixo": "/30",
            "mascara_decimal": "255.255.255.252",
            "mascara_binario": "11111111.11111111.11111111.11111100",
            "endereco_rede": "10.0.0.4",
            "endereco_broadcast": "10.0.0.7",
            "quantidade_hosts": 2,
            "faixa_hosts": "10.0.0.5 a 10.0.0.6"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.10.64",
            "mascara": "255.255.255.192"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00001010.01000000",
            "mascara_prefixo": "/26",
            "mascara_decimal": "255.255.255.192",
            "mascara_binario": "11111111.11111111.11111111.11000000",
            "endereco_rede": "192.168.10.64",
            "endereco_broadcast": "192.168.10.127",
            "quantidade_hosts": 62,
            "faixa_hosts": "192.168.10.65 a 192.168.10.126"
        }
    },
    # --- Novos Casos Adicionados ---
    {
        "entrada": {
            "endereco_ip": "192.168.1.10",
            "mascara": "255.255.255.0"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00000001.00001010",
            "mascara_prefixo": "/24",
            "mascara_decimal": "255.255.255.0",
            "mascara_binario": "11111111.11111111.11111111.00000000",
            "endereco_rede": "192.168.1.0",
            "endereco_broadcast": "192.168.1.255",
            "quantidade_hosts": 254,
            "faixa_hosts": "192.168.1.1 a 192.168.1.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "10.20.30.40",
            "mascara": "255.0.0.0"
        },
        "saida": {
            "endereco_ip_binario": "00001010.00010100.00011110.00101000",
            "mascara_prefixo": "/8",
            "mascara_decimal": "255.0.0.0",
            "mascara_binario": "11111111.00000000.00000000.00000000",
            "endereco_rede": "10.0.0.0",
            "endereco_broadcast": "10.255.255.255",
            "quantidade_hosts": 16777214,
            "faixa_hosts": "10.0.0.1 a 10.255.255.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "200.135.80.130",
            "mascara": "255.255.255.224"
        },
        "saida": {
            "endereco_ip_binario": "11001000.10000111.01010000.10000010",
            "mascara_prefixo": "/27",
            "mascara_decimal": "255.255.255.224",
            "mascara_binario": "11111111.11111111.11111111.11100000",
            "endereco_rede": "200.135.80.128",
            "endereco_broadcast": "200.135.80.159",
            "quantidade_hosts": 30,
            "faixa_hosts": "200.135.80.129 a 200.135.80.158"
        }
    },
    {
        "entrada": {
            "endereco_ip": "172.31.5.9",
            "mascara": "255.255.254.0"
        },
        "saida": {
            "endereco_ip_binario": "10101100.00011111.00000101.00001001",
            "mascara_prefixo": "/23",
            "mascara_decimal": "255.255.254.0",
            "mascara_binario": "11111111.11111111.11111110.00000000",
            "endereco_rede": "172.31.4.0",
            "endereco_broadcast": "172.31.5.255",
            "quantidade_hosts": 510,
            "faixa_hosts": "172.31.4.1 a 172.31.5.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.100.5",
            "mascara": "255.255.255.254"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.01100100.00000101",
            "mascara_prefixo": "/31",
            "mascara_decimal": "255.255.255.254",
            "mascara_binario": "11111111.11111111.11111111.11111110",
            "endereco_rede": "não há",
            "endereco_broadcast": "não há",
            "quantidade_hosts": 2,
            "faixa_hosts": "192.168.100.4 a 192.168.100.5"
        }
    },
    {
        "entrada": {
            "endereco_ip": "8.8.8.8",
            "mascara": "255.255.255.255"
        },
        "saida": {
            "endereco_ip_binario": "00001000.00001000.00001000.00001000",
            "mascara_prefixo": "/32",
            "mascara_decimal": "255.255.255.255",
            "mascara_binario": "11111111.11111111.11111111.11111111",
            "endereco_rede": "não há",
            "endereco_broadcast": "não há",
            "quantidade_hosts": 1,
            "faixa_hosts": "8.8.8.8"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.1.0",
            "mascara": "/24"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00000001.00000000",
            "mascara_prefixo": "/24",
            "mascara_decimal": "255.255.255.0",
            "mascara_binario": "11111111.11111111.11111111.00000000",
            "endereco_rede": "192.168.1.0",
            "endereco_broadcast": "192.168.1.255",
            "quantidade_hosts": 254,
            "faixa_hosts": "192.168.1.1 a 192.168.1.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.1.255",
            "mascara": "/24"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00000001.11111111",
            "mascara_prefixo": "/24",
            "mascara_decimal": "255.255.255.0",
            "mascara_binario": "11111111.11111111.11111111.00000000",
            "endereco_rede": "192.168.1.0",
            "endereco_broadcast": "192.168.1.255",
            "quantidade_hosts": 254,
            "faixa_hosts": "192.168.1.1 a 192.168.1.254"
        }
    },
    {
        "entrada": {
            "endereco_ip": "192.168.1.130",
            "mascara": "/25"
        },
        "saida": {
            "endereco_ip_binario": "11000000.10101000.00000001.10000010",
            "mascara_prefixo": "/25",
            "mascara_decimal": "255.255.255.128",
            "mascara_binario": "11111111.11111111.11111111.10000000",
            "endereco_rede": "192.168.1.128",
            "endereco_broadcast": "192.168.1.255",
            "quantidade_hosts": 126,
            "faixa_hosts": "192.168.1.129 a 192.168.1.254"
        }
    },
]
