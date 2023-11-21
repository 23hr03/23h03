var nombre = document.getElementById("nombre");
var apellido = document.getElementById("apellido");
var telefono = document.getElementById("telefono");
var email = document.getElementById("e-mail");
var contraseña = document.getElementById("password");
var error = document.getElementById("error");

function enviarFormulario(){
    console.log("enviando formulario...");

    var mensajeError = [];
    if(nombre === null || nombre === ""){
        error.push("Ingrese su nombre")
    }

    
    if(email === null || email === ""){
        error.push("Ingrese su nombre")
    }
    
    if(contraseña === null || contraseña === ""){
        error.push("Ingrese su nombre")
    }
    error.innerHTML = error
    

    return false
}