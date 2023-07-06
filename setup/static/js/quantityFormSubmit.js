document.addEventListener('DOMContentLoaded', function() {


    let submitButton = document.querySelector('#quantidade_artes')

    submitButton.addEventListener('change', () => {
      console.log('Deu certo');
      document.getElementById('art_quantity_formulario').submit()
  
    })
  });