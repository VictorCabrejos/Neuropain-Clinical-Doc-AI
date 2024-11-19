#! *** Flask API Routes ***

from flask import Blueprint, request, jsonify
from .langchain_pipeline import (
    generate_medical_report,
    generate_medical_report_original,
    generate_medical_report_with_rag,
)

main = Blueprint("main", __name__)


#! Ruta principal
@main.route("/")
def index():
    return "Welcome to Grossinger Neuropain Specialists PC"


#! Ruta para generar un informe médico (Endpoint version anterior)
@main.route("/generate_report", methods=["POST"])
def generate_report():
    data = request.json
    patient_info = data.get("patient_info", "")
    report = generate_medical_report(patient_info)
    return jsonify({"report": report})


#! Ruta para generar un informe médico (Endpoint para la version original)


@main.route("/generate_report_original", methods=["POST"])
def generate_report_original():
    """
    Genera un informe médico utilizando el pipeline original sin recuperación de datos.
    """
    data = request.json
    patient_info = data.get("patient_info", "")

    # Generar el informe médico utilizando el pipeline original
    report = generate_medical_report_original(patient_info)

    return jsonify({"report": report})


#! Ruta para generar un informe médico (Endpoint para la versión con RAG)


@main.route("/generate_report_with_rag", methods=["POST"])
def generate_report_with_rag():
    """
    Genera un informe médico utilizando el pipeline actualizado con recuperación de datos (RAG).
    """
    data = request.json
    patient_info = data.get("patient_info", "")

    # Generar el informe médico utilizando el pipeline con RAG
    report = generate_medical_report_with_rag(patient_info)

    return jsonify({"report": report})
