
const frm = document.querySelector('form');
const mensagemErro = document.getElementById('mensagem_erro');
const spinner = document.getElementById('spinner');
const textoBotao = document.getElementById('texto_botao');
const btn = document.getElementById('btn_calcular');
const resultados = document.getElementById('resultados');

frm.addEventListener('submit', async (e) => {
    e.preventDefault();

    mensagemErro.textContent = '';
    mensagemErro.style.display = 'none';
    resultados.style.display = 'none';

    btn.disabled = true;
    spinner.style.display = 'inline-block';
    textoBotao.textContent = 'Calculando...';

    const formData = new FormData(frm);

    try {
        const response = await fetch(frm.action, {
            headers: {
                'Content-Type': 'application/json'
            },
            method: frm.method,
            body: JSON.stringify(Object.fromEntries(formData))
        });

        const result = await response.json();

        if (response.ok) {
            exibirResultados(result);
            resultados.style.display = 'block';
        } else {
            mensagemErro.textContent = result.error || 'Ocorreu um erro ao realizar o cálculo.';
            mensagemErro.style.display = 'block';
        }

    } catch (error) {
        mensagemErro.textContent = 'Ocorreu um erro ao realizar o cálculo.';
        mensagemErro.style.display = 'block';

    } finally {
        btn.disabled = false;
        spinner.style.display = 'none';
        textoBotao.textContent = 'Calcular';
    }
});


function exibirResultados(result) {
    document.getElementById('endereco_ip_binario').textContent = result.endereco_ip_binario;
    document.getElementById('mascara_prefixo').textContent = result.mascara_prefixo;
    document.getElementById('mascara_decimal').textContent = result.mascara_decimal;
    document.getElementById('mascara_binario').textContent = result.mascara_binario;
    document.getElementById('endereco_rede').textContent = result.endereco_rede;
    document.getElementById('endereco_broadcast').textContent = result.endereco_broadcast;
    document.getElementById('quantidade_hosts').textContent = result.quantidade_hosts;
    document.getElementById('faixa_hosts').textContent = result.faixa_hosts;
}
