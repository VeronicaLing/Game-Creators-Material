const $container = document.getElementById ("container")
const URL_FOTOS = "https://api.thecatapi.com/v1/images/search"

async function pegar_fotos(){

    let $foto_info = document.createElement("p")
        
    console.log("Carregando...")
    foto_response = await(fetch(URL_FOTOS))
    foto_obj = await(foto_response.json())
    console.log(foto_response)
    console.log(foto_obj)

    console.log(foto_obj[0].url)
    $foto_info.textContent = foto_obj[0].url
    $container.appendChild($foto_info)
    console.log($foto_info)
}

pegar_fotos()
