const $container = document.getElementById("container")
const URL_FOTOS = "https://api.thecatapi.com/v1/images/search"


async function pegar_fotos() {

    let $foto_info = document.createElement("p")
    let $foto_id = document.createElement("p")
    let $foto_width = document.createElement("p")
    let $foto_height = document.createElement("p")
    $foto_info.classList.add("p")
    $foto_id.classList.add("p")
    $foto_width.classList.add("p")
    $foto_height.classList.add("p")

    console.log("Carregando...")
    foto_response = await (fetch(URL_FOTOS))
    foto_obj = await (foto_response.json())
    console.log(foto_response)
    console.log(foto_obj)
    console.log(foto_obj[0].url)

    const imagem = document.createElement("img")
    $container.appendChild(imagem)
    imagem.classList.add("p1")
    imagem.src = foto_obj[0].url
    imagem.style.imageRendering = "auto"
    imagem.style.border = "5px solid #868686"
    
    
    $foto_info.textContent = foto_obj[0].url
    $foto_id.textContent = foto_obj[0].id
    $foto_width.textContent = foto_obj[0].width
    $foto_height.textContent = foto_obj[0].height
    $container.appendChild($foto_info)
    $container.appendChild($foto_id)
    $container.appendChild($foto_width)
    $container.appendChild($foto_height)
    console.log($foto_info)
    console.log($foto_id)
    console.log($foto_width)
    console.log($foto_height)


    setTimeout(() => {
        
    }, 1500);
    
}

pegar_fotos()

