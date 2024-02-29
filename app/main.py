
from app.service.aves.birds import obtener_aves
from string import Template

def app():
   
    res_aves = obtener_aves()
    
    # for ave_nombre in res_aves:
    #     pass
    #     # print(ave_nombre['name'])
    
    # for ave_imagen in res_aves:
    #     pass
    #     # print(ave_imagen['images']['main'])
    
    
    img_template = Template("""
                            <div class="card" style="width: 18rem;">
                                <img src="$url" class="card-img-top" alt="$nombre_espaniol">
                                <div class="card-body">
                                    <h5 class="text-center">Nombre latin: $nombre_latin</h2>
                                    <p class="text-center">Nombre español: $nombre_espaniol</p>
                                    <p class="text-center">Nombre ingles: $nombre_ingles</p>
                                </div>
                            </div>
                            """)
        

    html_template = Template('''
                             <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>Document</title>
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                                </head>
                                <body>
                                    <h1 class="text-center">Aves de Chile</h1>
                                    
                                    
                                    <div class="container">
                                        <div class="row gap-3">
                                            $body   
                                        </div>   
                                    </div>                                                                       
                                    
                                </body>
                                </html>
                             ''')
     
    texto_img = ""
    
    for aves in res_aves:

        texto_img += img_template.substitute(url = aves['images']['main'],nombre_espaniol = aves['name']['spanish'],nombre_ingles = aves['name']['english'],nombre_latin = aves['name']['latin']) + "\n"
        
                                
    print("Renderizando html....")
    html = html_template.substitute(body = texto_img)
    with open("aves.html", "w", encoding="utf-8") as html_file:
        html_file.write(html)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # //no funcionó me renderizaba todos los español , luego todos los
    # // ingles, los latin y luego
    # // las imagenes asi que mejor cree un template que tomase todos los valores como el de arriba
    # lista_urls = [ave_img['images']['main'] for ave_img in res_aves]
    # nombre_espaniol = [ave_nombre_spanish['name']['spanish'] for ave_nombre_spanish in res_aves] 
    # nombre_ingles = [ave_nombre_spanish['name']['english'] for ave_nombre_spanish in res_aves]
    # nombre_latin = [ave_nombre_spanish['name']['latin'] for ave_nombre_spanish in res_aves]
    # nombre_espaniol_template = Template('<h2>Nombre español: $nombre_espaniol</h2>') 
    # nombre_ingles_template = Template('<h2>Nombre ingles: $nombre_ingles</h2>') 
    # nombre_latin_template = Template('<h2>Nombre latin: $nombre_latin</h2>') 
    # print(img_template) // imprime el  espacio en memoria del objeto
    # print(html_template) // imprime el otro espacio en memoria del objeto, 
    # print([ave_nombre_spanish['name']['spanish'] for ave_nombre_spanish in res_aves]) // prueba comprension para trener datos
    # print([ave_nombre_spanish['name']['english'] for ave_nombre_spanish in res_aves]) // prueba comprension para trener datos
    # print([ave_nombre_spanish['name']['latin'] for ave_nombre_spanish in res_aves]) //  prueba comprension para trener datos
    # print([ave_img['images']['main'] for ave_img in res_aves]) // prueba comprension para trener datos
    # texto_espaniol = ""
    # texto_ingles = ""
    # texto_latin = ""
    
    # for url in lista_urls:
    #     texto_img += img_template.substitute(url = url) + "\n"
        
    # for nombre_espaniol in lista_urls:
    #     texto_espaniol += nombre_espaniol_template.substitute(nombre_espaniol = nombre_espaniol) + "\n"

    # for nombre_ingles in lista_urls:
    #     texto_ingles += nombre_ingles_template.substitute(nombre_ingles = nombre_ingles) + "\n"

    # for nombre_latin in lista_urls:
    #     texto_latin += nombre_latin_template.substitute(nombre_latin = nombre_latin) + "\n"
            # texto_espaniol += nombre_espaniol_template.substitute(nombre_espaniol = aves['name']['spanish']) + "\n"
        # texto_ingles += nombre_ingles_template.substitute(nombre_ingles = aves['name']['english']) + "\n"
        # texto_latin += nombre_latin_template.substitute(nombre_latin = aves['name']['latin']) + "\n"
    
