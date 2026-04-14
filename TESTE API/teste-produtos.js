const $container = document.getElementById("container")
const $container2 = document.getElementById("container2")
const button1 = document.getElementById("b1")
const button2 = document.getElementById("b2")
const button3 = document.getElementById("b3")
const button4 = document.getElementById("b4")
const button5 = document.getElementById("b5")
const button6 = document.getElementById("b6")
const URL_PRODUTOS = "https://pacoca-store.onrender.com/api/produtos"

async function produtos_categorias(categoria) {

    const url = `${URL_PRODUTOS}?categoria=${categoria}`

    const produtos = await (fetch(url))
    const categorias = await (produtos.json())
    console.log(produtos)
    console.log(categorias)

    $container2.innerHTML = ""

    categorias.forEach(produto => {
        const p = document.createElement("div")
        p.classList.add("b")
        $container.appendChild(p)

        const produto_info = document.createElement("div")
        produto_info.classList.add("b1")
        $container2.appendChild(produto_info)

        const nome_produto = document.createElement("h3")
        nome_produto.classList.add("produto-nome")
        nome_produto.textContent = produto.nome
        produto_info.appendChild(nome_produto)

        const imagem = document.createElement("img")
        $container2.appendChild(imagem)
        imagem.classList.add("p")
        imagem.src = "https://placehold.co/400"
    })



    console.log(categorias)
    categorias.forEach(() => {

        const produto = document.createElement("p")
        let $all_cat = document.createElement("p")
        let $eletronicos = document.createElement("p")
        let $eletrodomesticos = document.createElement("p")
        let $roupas = document.createElement("p")
        let $livros = document.createElement("p")
        let $diversos = document.createElement("p")

        $container.appendChild($all_cat)
        $container.appendChild($eletronicos)
        $container.appendChild($eletrodomesticos)
        $container.appendChild($roupas)
        $container.appendChild($livros)
        $container.appendChild($diversos)

        console.log($all_cat)
        console.log($eletronicos)
        console.log($eletrodomesticos)
        console.log($roupas)
        console.log($livros)
        console.log($diversos)


    })

}


button1.addEventListener("click", () => {
    produtos_categorias("")
})

button2.addEventListener("click", () => {
    produtos_categorias("eletronicos")
})

button3.addEventListener("click", () => {
    produtos_categorias("eletrodomesticos")
})

button4.addEventListener("click", () => {
    produtos_categorias("roupas")
})

button5.addEventListener("click", () => {
    produtos_categorias("livros")
})

button6.addEventListener("click", () => {
    produtos_categorias("diversos")
})


produtos_categorias()

