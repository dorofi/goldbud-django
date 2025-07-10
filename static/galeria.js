// Получаем все изображения галереи и модальное окно
const images = document.querySelectorAll('.gallery-image');
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');
const closeBtn = document.getElementById('close');

// Открытие модального окна при клике на изображение
images.forEach(image => {
    image.addEventListener('click', function() {
        modal.style.display = "flex";
        modalImg.src = this.src;
    });
});

// Закрытие модального окна при клике на кнопку "закрыть"
closeBtn.addEventListener('click', function() {
    modal.style.display = "none";
});

// Закрытие модального окна при клике за его пределами
window.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});
// Появление кнопки при прокрутке страницы
window.onscroll = function() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
      document.getElementById("backToTop").style.display = "block";
    } else {
      document.getElementById("backToTop").style.display = "none";
    }
  };
  
  // Плавный скролл наверх
  document.getElementById("backToTop").addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
