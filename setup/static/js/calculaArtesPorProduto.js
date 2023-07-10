document.addEventListener('DOMContentLoaded', function() {
    const camposInputs = document.querySelectorAll('input[name^="arte_"]');
  
    for (var i = 0; i < camposInputs.length; i++) {
      camposInputs[i].addEventListener('click', (event) => {
        event.preventDefault();
        let quantidadeProdutosElemento = document.getElementById('quantidade-produtos');
        let quantidadeProdutos = quantidadeProdutosElemento.value
        
        console.log(quantidadeProdutos);
        console.log(camposInputs);
        console.log(quantidadeProdutosElemento);
  
        let somaValores = 0;
        for (var j = 0; j < camposInputs.length; j++) {
          somaValores += parseInt(camposInputs[j].value) || 0;
        }
        for (var j = 0; j < camposInputs.length; j++) {
            const valorCampo = parseInt(camposInputs[j].value) || 0;
            const novoMaximo = quantidadeProdutos - somaValores + valorCampo;
            if (novoMaximo >= valorCampo) {
              camposInputs[j].max = novoMaximo;
            } else {
              camposInputs[j].max = valorCampo;
            }
        }
      });
    }
  });