const input = document.getElementById("lista_tarefa")
const button = document.getElementById("add_tarefa")
const lista = document.getElementById("lista")


function enviarDados() {

    let texto_tarefa = input.value

    if (texto_tarefa.trim() === "") return


    let tarefa_nova = {
        titulo: texto_tarefa,
        concluido: false,
    }

    const item_tarefa = document.createElement("li")
    item_tarefa.classList.add("li")

    const tarefa_txt = document.createElement("p")
    tarefa_txt.textContent = texto_tarefa
    item_tarefa.appendChild(tarefa_txt)

    let tarefas = JSON.parse(localStorage.getItem("tarefas")) || []
    tarefas.push(tarefa_nova)
    tarefas.forEach(tarefa => {
        console.log(tarefa.titulo, tarefa.concluido)
    })

    localStorage.setItem("tarefas", JSON.stringify(tarefas))


    // function salvar_tarefa() {
    //     let tarefa_txt = input.value
    //     localStorage.setItem("texto_tarefa", JSON.stringify(tarefa_txt))
    //     input.value = JSON.parse(localStorage.getItem("texto_tarefa"))
    // }
    // button.addEventListener("input", salvar_tarefa)


    function atualizar_lista() {
        tarefa_nova = []

        document.querySelectorAll(".texto_tarefa").forEach(item_txt => {
            let texto = item_txt.querySelector("p").textContent
            let concluido = item_txt.querySelector("p").style.textDecoration === "line-through"
        })
    }


    const actions = document.createElement("div")
    actions.classList.add("div")
    const remover = document.createElement("button")
    remover.textContent = "X"
    remover.classList.add("li2")

    remover.addEventListener("click", () => {
        item_tarefa.remove()
        let tarefas = JSON.parse(localStorage.getItem("tarefas")) || []
        tarefas = tarefas.filter(t => t.titulo !== texto_tarefa)
        localStorage.setItem("tarefas", JSON.stringify(tarefas))

    })


    const checkbox = document.createElement("input")
    checkbox.type = "checkbox"

    checkbox.addEventListener("change", () => {
        if (checkbox.checked) {
            tarefa_txt.style.textDecoration = "line-through"
        } else {
            tarefa_txt.style.textDecoration = "none"
        }
    })


    lista.appendChild(item_tarefa)

    actions.appendChild(remover)

    actions.appendChild(checkbox)

    item_tarefa.appendChild(actions)


    input.value = ""
}

button.addEventListener("click", enviarDados)

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault()
        enviarDados()
    }

})






// let nome = "veronica"
// let usuario = {
//     "nome": "veronica",
//     "e-mail": "vero@mail.com",
//     "senha": 2365,
//     "logado": false,
// }

// console.log(usuario['nome'])
// localStorage.setItem('usuarios', JSON.stringify(usuario))
// let usuario_salvo = JSON.parse(localStorage.getItem('usuarios'))
// console.log(usuario_salvo['nome', 'e-mail'])







// let tarefa_nova = {
//     "titulo": "titulo_da_tarefa",
//     "concluido": false,
// }

// console.log(tarefa_nova['titulo'])
// localStorage.setItem('tarefas', JSON.stringify(tarefa_nova))
// let tarefa_salva = JSON.parse(localStorage.getItem('tarefas'))
// console.log(tarefa_salva['titulo', 'concluido'])





// button.addEventListener('click', () => {
//     if (event.key === 'Enter') {
//       event.preventDefault();
//       enviarDados();
//     }

//     let texto_tarefa = input.value

//     if (texto_tarefa.trim() === "") return

//     const item_tarefa = document.createElement("li")
//     item_tarefa.classList.add("li")

//     const tarefa_txt = document.createElement("p")
//     tarefa_txt.textContent = texto_tarefa
//     item_tarefa.appendChild(tarefa_txt)

//     const remover = document.createElement("button")
//     remover.textContent = "X"
//     remover.classList.add("li2")

//     remover.addEventListener("click", () => {
//         item_tarefa.remove()
//     })

//     item_tarefa.appendChild(remover)

//     const checkbox = document.createElement('input')
//     checkbox.setAttribute('type', 'checkbox')

//     checkbox.addEventListener('change', () => {
//         if(checkbox.checked === true){
//             tarefa_txt.style.textDecoration = 'line-through'
//             tarefa_txt.style.alignContent = ''
//         }
//         else {
//             tarefa_txt.style.textDecoration = 'none'
//         }
//     })


//     item_tarefa.appendChild(checkbox)

//     lista.appendChild(item_tarefa)

//     input.value = ""
// })



