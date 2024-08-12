# tests/test_routes.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


#! TC-001: Generación de Informe con Input Válido
def test_generate_report_valid_input(client):
    """
    Prueba que el endpoint /generate_report genere un informe médico válido cuando se le
    proporciona información de paciente válida.

    Se espera que el informe contenga las secciones clave como "Informe Médico Detallado",
    "Motivo de Consulta", "Antecedentes Médicos", y "Examen Físico".
    """
    # Datos de ejemplo para un paciente
    patient_info = "Paciente de 45 años con neuropatía diabética y dolor crónico en extremidades inferiores."

    # Realizar una solicitud POST al endpoint /generate_report
    response = client.post("/generate_report", json={"patient_info": patient_info})

    # Verificar que la solicitud se completó exitosamente (código 200)
    assert response.status_code == 200

    # Verificar que el informe contiene las palabras clave esperadas
    data = response.get_json()
    assert "Informe Médico Detallado" in data["report"]
    assert "Motivo de Consulta" in data["report"]
    assert "Antecedentes Médicos" in data["report"]
    assert "Examen Físico" in data["report"]


#! TC-002: Manejo de Input Vacío
def test_generate_report_invalid_input(client):
    """
    Prueba que el endpoint /generate_report maneje adecuadamente un input vacío.

    Se espera que el informe no esté vacío, lo que indica que el sistema ha manejado
    el input de manera apropiada.
    """
    # Proporcionar un input vacío
    patient_info = ""

    # Realizar una solicitud POST al endpoint /generate_report
    response = client.post("/generate_report", json={"patient_info": patient_info})

    # Verificar que la solicitud se completó exitosamente (código 200)
    assert response.status_code == 200

    # Verificar que el informe maneje el caso adecuadamente
    data = response.get_json()
    assert data["report"] != ""  # Asegurarse de que el informe no esté vacío

    # Se puede agregar más validaciones según la lógica que maneje un input vacío
    assert "error" not in data["report"].lower()


#! TC-003: Prueba de Alucinaciones
def test_generate_report_avoid_hallucinations(client):
    """
    Prueba que el modelo no genere información inventada (alucinaciones) cuando
    se le proporciona un input ambiguo o con poca información.

    Se espera que el informe generado sea limitado y no incluya información detallada
    que no se haya proporcionado explícitamente.
    """
    patient_info = "Paciente con síntomas generales."

    response = client.post("/generate_report", json={"patient_info": patient_info})

    assert response.status_code == 200
    data = response.get_json()

    # Asegúrate de que el informe no contenga información detallada inventada
    assert "Informe Médico Detallado" not in data["report"]
    assert "Antecedentes Médicos" not in data["report"]
    assert "Examen Físico" not in data["report"]
    # Verifica que el contenido sea genérico y no especulativo
    assert "síntomas generales" in data["report"].lower()


#! TC-004: Prueba con Input Parcialmente Completo
def test_generate_report_partial_input(client):
    """
    Prueba cómo el sistema maneja un input parcialmente completo, donde
    solo se proporciona parte de la información del paciente.

    Se espera que el informe generado reconozca la falta de información y
    no intente completar los datos faltantes de manera especulativa.
    """
    patient_info = "Paciente de 60 años con diabetes."

    response = client.post("/generate_report", json={"patient_info": patient_info})

    assert response.status_code == 200
    data = response.get_json()

    # Verifica que el informe no intente llenar los datos faltantes
    assert "antecedentes médicos" in data["report"].lower()
    assert "diabetes" in data["report"].lower()
    assert "edad" in data["report"].lower()
    # Asegúrate de que no se inventen detalles
    assert "hipertensión" not in data["report"].lower()
    assert "tratamiento" not in data["report"].lower()


#! TC-005: Prueba de Respuestas Consistentes
def test_generate_report_consistent_responses(client):
    """
    Prueba que el modelo genere respuestas consistentes cuando se le proporciona
    la misma entrada varias veces.

    Se espera que el informe generado sea idéntico o muy similar en cada solicitud.
    """
    patient_info = "Paciente de 50 años con hipertensión y dolor de cabeza recurrente."

    # Realizar la primera solicitud
    response1 = client.post("/generate_report", json={"patient_info": patient_info})
    assert response1.status_code == 200
    report1 = response1.get_json()["report"]

    # Realizar una segunda solicitud con el mismo input
    response2 = client.post("/generate_report", json={"patient_info": patient_info})
    assert response2.status_code == 200
    report2 = response2.get_json()["report"]

    # Verificar que las respuestas sean consistentes
    assert report1 == report2
