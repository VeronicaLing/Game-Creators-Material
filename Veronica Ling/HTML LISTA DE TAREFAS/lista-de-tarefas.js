const input = document.getElementById("lista_tarefa")
const button = document.getElementById("add_tarefa")
const lista = document.getElementById("lista")

button.addEventListener('click', () => {

    let texto_tarefa = input.value

    if (texto_tarefa.trim() === "") return

    const item_tarefa = document.createElement("li")
    item_tarefa.classList.add("li")

    const tarefa_txt = document.createElement("p")
    tarefa_txt.textContent = texto_tarefa
    item_tarefa.appendChild(tarefa_txt)

    const remover = document.createElement("button")
    remover.textContent = "X"
    remover.classList.add("li2")

    remover.addEventListener("click", () => {
        item_tarefa.remove()
    })

    item_tarefa.appendChild(remover)

    const checkbox = document.createElement('input')
    checkbox.setAttribute('type', 'checkbox')

    checkbox.addEventListener('change', () => {
        if(checkbox.checked === true){
            tarefa_txt.style.textDecoration = 'line-through'
            tarefa_txt.style.alignContent = ''
        }
        else {
            tarefa_txt.style.textDecoration = 'none'
        }
    })


    item_tarefa.appendChild(checkbox)

    lista.appendChild(item_tarefa)

    input.value = ""
})



