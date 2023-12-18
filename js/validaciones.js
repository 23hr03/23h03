function validarFormulario() {
    // Obtener los valores ingresados por el usuario y recortar
    // los posibles espacios en blanco al principio y al final.
    var nombre = document.getElementById("nombre").value.trim();
    var dni = document.getElementById("dni").value.trim();
    var direccion = document.getElementById("direccion").value.trim();
    var mail= document.getElementById("e-mail").value.trim()

    // Verificar si algún campo está en blanco
    if (nombre === "" || mail === "" || dni === "" || direccion === "") {
      alert("Por favor, complete todos los campos del formulario.");
      return false;
    }

    // Verificar si el nombre contiene solo caracteres alfabéticos y espacios
    for (var i = 0; i < nombre.length; i++) {
      var charCode = nombre.charCodeAt(i);
      if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
        alert("El campo 'nombre' solo puede contener caracteres alfabéticos y espacios.");
        return false;
      }
    }

    // Verificar si el DNI contiene solo 8 dígitos numéricos
    if (dni.length !== 8) {
      alert("El campo 'dni' debe contener exactamente 8 dígitos numéricos.");
      return false;
    }
    for (var j = 0; j < dni.length; j++) {
      var digit = dni.charAt(j);
      if (digit < "0" || digit > "9") {
        alert("El campo 'dni' solo puede contener dígitos numéricos.");
        return false;
      }
    }

    // Si todas las validaciones son exitosas, enviar el formulario
    alert("Formulario enviado correctamente.");
    alert("Pronto un operador se pondra en contacto con usted para acesorarlo")
    return true;
  }
const { createApp } = Vue
createApp({
    data() {
        return {
            usuarios: [],
            //url:'http://localhost:5000/productos',
            // si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
            url: 'http://127.0.0.1:5001/usuario', // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /*atributos para el guardar los valores del formulario */
            id: 0,
            nombre: "",
            gmail: "",
            dni: 0,
            direccion: "",
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)

                .then(response => response.json())
                .then(data => {
                    this.usuarios = data;
                    this.cargando = false
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        eliminar(usuario) {
            const url = this.url + '/' + usuario;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    location.reload();
                })
        },
        grabar() {
            let usuario = {
                nombre: this.nombre,
                gmail: this.gmail,
                dni: this.dni,
                direccion: this.direccion,
                
            }
            var options = {
                body: JSON.stringify(usuario),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./contacto2.htm";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabarr")

                })
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')