function avancarProximo() {
    // Incrementa o índice do produto atual
    var indiceAtual = parseInt(document.getElementById('indice_produto').value);
    var proximoIndice = indiceAtual + 1;

    // Atualiza o valor do campo indice_produto
    document.getElementById('indice_produto').value = proximoIndice;

    // Submete o formulário
    document.getElementById('meu_formulario').submit();
  }

  document.addEventListener('DOMContentLoaded', function() {


    let submitButton = document.querySelector('.submit-button')

    submitButton.addEventListener('click', () => {
      let indiceAtual = parseInt(document.getElementById('indice_produto').value);
      let proximoIndice = indiceAtual + 1;
      console.log(indiceAtual);
      document.getElementById('indice_produto').value = proximoIndice

      document.getElementById('meu_formulario').submit()
  
    })
  });