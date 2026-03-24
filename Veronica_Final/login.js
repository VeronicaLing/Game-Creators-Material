const usuario = document.getElementById("usuario")
const senha = document.getElementById("senha")
const form = document.getElementById("form")

form.addEventListener('submit', function(event){
    event.preventDefault()

    console.log(usuario.value)
    usuario.value = ""
    console.log(senha.value)
    senha.value = ""
})