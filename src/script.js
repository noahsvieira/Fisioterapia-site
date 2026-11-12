document.addEventListener('DOMContentLoaded', () => {
  const itensFaq = document.querySelectorAll('.accordion-item');

  itensFaq.forEach((item) => {
    const botao = item.querySelector('.accordion-header');
    
    botao.addEventListener('click', () => {
      const estaAberto = item.classList.contains('active');

      
      itensFaq.forEach((el) => {
        el.classList.remove('active');
        el.querySelector('.accordion-header').setAttribute('aria-expanded', 'false');
        el.querySelector('.icon').textContent = '+';
      });

     
      if (!estaAberto) {
        item.classList.add('active');
        botao.setAttribute('aria-expanded', 'true');
        botao.querySelector('.icon').textContent = '−';
      }
    });
  });
});