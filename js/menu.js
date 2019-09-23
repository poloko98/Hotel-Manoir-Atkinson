let btnMenu = document.getElementById('btnmenu');
let menu = document.getElementById('menu');
btnMenu.addEventListener('click', function(){
    'use strict';
    menu.classList.toggle('mostrar');
});


function validarCorreo(){
    var correo= document.getElementById("mail").value;
    if(correo===""||!(/\w+@\w+\.+[a-z]/).test(correo)){
        alert("Correo no valido");
    }
}

function validarNombre(){
    var nombre= document.getElementById("nombre").value;
    if(nombre===""||!(/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/).test(nombre)){
        alert("Nombre no valido")
        nombre.focus;
    }
}

function validarTelefono(){
    var telefono= document.getElementById("telefono").value;
    if(telefono===""||!(/^\++[0-9]{11}$/).test(telefono)){
        alert("Numero no valido")
    }
}


function validarForm(){
    var telefono= document.getElementById("telefono").value;
    var nombre= document.getElementById("nombre").value;
    var correo= document.getElementById("mail").value;

    if(telefono===""||!(/^\++[0-9]{11}$/).test(telefono)){
        alert("Numero no valido")
    
    } else if(nombre===""||!(/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/).test(nombre)){
        alert("Nombre no valido")
        nombre.focus();
    }else if(correo===""||!(/\w+@\w+\.+[a-z]/).test(correo)){
        alert("Correo no valido");
    }
}

/*function validarFecha(){
    var hoy =new Date();
    var fecha= document.getElementById("fecha").value;

    if(fecha>hoy){
        alert("No puede seleccionar una fecha anterior")
    }
}*/