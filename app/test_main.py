from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """
    Prueba de Sanidad: Verifica que la API levanta correctamente 
    y responde el mensaje base.
    """
    response = client.get("/")
    
    assert response.status_code == 200
    
    assert response.json() == {
        "status": "ok", 
        "message": "Estructura base configurada y en línea."
    }