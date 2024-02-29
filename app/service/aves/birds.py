import app.service.repository.api_manager as api_manager

URL_PHOTOS = "https://aves.ninjas.cl/api/birds"

def obtener_aves():
    url = URL_PHOTOS
    respuesta = api_manager.get(url)
    return respuesta