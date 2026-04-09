const $container = document.getElementById("container")
const $b1 = document.getElementById("b1")
const $b2 = document.getElementById("b2")
const $b3 = document.getAnimations("b3")
const $b4 = document.getElementById("b4")
const $b5 = document.getElementById("b5")
const $b6 = document.getElementById("b6")
const URL_PRODUTOS = "https://pacoca-store.onrender.com/api/produtos"
const URL_CATEGORIAS = `https://pacoca-store.onrender.com/api/produtos?categoria=${categoria}`

async function produtos_categorias() {

    produtos = await (fetch(URL_PRODUTOS))
    categorias = await (produtos.json())
    console.log(produtos)
    console.log(categorias)
    console.log(categorias[0].url)

    console.log(categorias)
    categorias.forEach(() => {

        const produto = document.createElement("p")
        let $all_cat = document.createElement("p")
        let $eletronicos = document.createElement("p")
        let $eletrodomesticos = document.createElement("p")
        let $roupas = document.createElement("p")
        let $livros = document.createElement("p")
        let $diversos = document.createElement("p")

        
        $all_cat.textContent = categorias[0].categoria
        $

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

produtos_categorias()
