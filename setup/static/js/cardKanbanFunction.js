document.addEventListener('DOMContentLoaded', function() {
    var showDetailsLinks = document.querySelectorAll('.show-details');
    
    showDetailsLinks.forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        var card = this.parentNode;
        const cardKanban = document.querySelector('.card-kanban1')
        var cardDetails = card.querySelector('.card-details');
        cardDetails.classList.toggle('show');
        cardKanban.style.display = 'none';
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    const btnReprove = document.querySelector('.btn-reprove');
    const btnReproveTrue = document.querySelector('.btn-reprove-true');
    console.log(btnReprove);

    btnReprove.addEventListener('click', (event) => {
      event.preventDefault()
      const textArea = document.querySelector('.text-area')
      console.log(textArea);
      textArea.hidden = false;
      btnReprove.style.display = 'none';
      btnReproveTrue.style.display = '';
    }) 
  });
