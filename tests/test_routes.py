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
    patient_info = "Paciente con síntomas generales."
    response = client.post("/generate_report", json={"patient_info": patient_info})
    assert response.status_code == 200
    data = response.get_json()
    report = data["report"]

    # Check if the report is a generic template indicating insufficient information
    assert (
        "Información no proporcionada" in report
        or "Información insuficiente para generar un informe detallado." in report
    )


#! TC-004: Prueba con Input Parcialmente Completo
def test_generate_report_partial_input(client):
    patient_info = "Paciente de 60 años con diabetes."
    response = client.post("/generate_report", json={"patient_info": patient_info})
    assert response.status_code == 200
    data = response.get_json()
    report = data["report"].lower()

    # Adjusted expectation based on structured but incomplete report output
    assert (
        "información no proporcionada" in report
        or "información insuficiente para generar un informe detallado" in report
    )


#! TC-005: Prueba de Respuestas Consistentes
def test_generate_report_consistent_responses(client):
    patient_info = "Paciente de 50 años con hipertensión y dolor de cabeza recurrente."

    response1 = client.post("/generate_report", json={"patient_info": patient_info})
    assert response1.status_code == 200
    report1 = response1.get_json()["report"]

    response2 = client.post("/generate_report", json={"patient_info": patient_info})
    assert response2.status_code == 200
    report2 = response2.get_json()["report"]

    # Allow minor differences in non-critical fields (like exact wording) but check for key consistency
    assert "diagnóstico" in report1.lower() and "diagnóstico" in report2.lower()
    assert "hipertensión" in report1.lower() and "hipertensión" in report2.lower()
