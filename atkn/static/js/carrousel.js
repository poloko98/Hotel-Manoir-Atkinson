var imagenes = ['img/slider1.jpg', 'img/slider2.jpg', 'img/slider3.jpg', 'img/slider4.jpg'],
  cont = 0;

function carrousel(tslider) {
  tslider.addEventListener('click', e => {
    let prev = tslider.querySelector('.prev'),
      next = tslider.querySelector('.next'),
      img = tslider.querySelector('img'),
      tgt = e.target;
    if (tgt == prev) {
      if (cont > 0) {
        img.src = imagenes[cont-1];
        cont--;
      } else {
        img.src = imagenes[imagenes.length - 1];
        cont = imagenes.length - 1;
      }
    } else if (tgt == next) {
      if (cont < imagenes.length - 1) {
        img.src = imagenes[cont + 1];
        cont++;
      } else {
        img.src = imagenes[0];
        cont = 0;
      }
    }
  });
}


  window.addEventListener('load', function (){
    var imagauto = ['img/slider1.jpg', 'img/slider2.jpg', 'img/slider3.jpg', 'img/slider4.jpg']
    var indice = 0;
    
    
    function cambiarImagen(){
      document.auto.src=imagauto[indice]
      if(indice<3){
        indice++;
      }else{
        indice=0
      }
    }
    setInterval(cambiarImagen,6000);
  });


document.addEventListener("DOMContentLoaded", ()=>{
  let tslider = document.querySelector('.tslider');
  carrousel(tslider);
  cambiarImagen(tslider);
});