const $container = document.getElementById("container")
const URL_FOTOS = "https://api.thecatapi.com/v1/images/search?limit=10"


async function pegar_fotos() {

    console.log("Carregando...")
    foto_response = await (fetch(URL_FOTOS))
    foto_obj = await (foto_response.json())
    console.log(foto_response)
    console.log(foto_obj)
    console.log(foto_obj[0].url)
    let obj_index = 0

    console.log(foto_obj)
    foto_obj.forEach(() => {

        const imagem = document.createElement("img")
        let $foto_info = document.createElement("p")
        let $foto_id = document.createElement("p")
        let $foto_width = document.createElement("p")
        let $foto_height = document.createElement("p")
        let $foto_orientation = document.createElement("p")
        $foto_info.classList.add("p")
        $foto_id.classList.add("p")
        $foto_width.classList.add("p")
        $foto_height.classList.add("p")
        $foto_orientation.classList.add("p0")
        $container.appendChild(imagem)
        imagem.classList.add("p1")
        imagem.src = foto_obj[obj_index].url
        imagem.style.imageRendering = "auto"
        imagem.style.border = "5px solid #868686"

        $foto_info.textContent = `URL: ${foto_obj[obj_index].url}`
        $foto_id.textContent = `ID: ${foto_obj[obj_index].id}`
        $foto_width.textContent = `Largura: ${foto_obj[obj_index].width}`
        $foto_height.textContent = `Altura: ${foto_obj[obj_index].height}`
        $container.appendChild($foto_info)
        $container.appendChild($foto_id)
        $container.appendChild($foto_width)
        $container.appendChild($foto_height)
        console.log($foto_info)
        console.log($foto_id)
        console.log($foto_width)
        console.log($foto_height)

        const foto_orientation = document.createElement("p")
        $container.appendChild(foto_orientation)
        foto_orientation.classList.add("p0")
        imagem.onload = () => {
            if (imagem.width > imagem.height) {
                foto_orientation.textContent = "Orientação: Horizontal"
            } else if (imagem.height > imagem.width) {
                foto_orientation.textContent = "Orientação: Vertical"
            } else {
                foto_orientation.textContent = "Orientação: Quadrada"
            }
        }

        console.log(foto_obj[obj_index].url)
        obj_index++
    })

    setTimeout(() => {

    }, 1500);

}


pegar_fotos()

