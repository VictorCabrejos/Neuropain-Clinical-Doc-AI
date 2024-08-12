from flask import Blueprint, request, jsonify
from .langchain_pipeline import generate_medical_report

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Welcome to Grossinger Neuropain Specialists PC"


@main.route("/generate_report", methods=["POST"])
def generate_report():
    # Obtener la información del paciente desde el request
    data = request.json
    patient_info = data.get("patient_info", "")

    # Generar el informe médico utilizando LangChain
    report = generate_medical_report(patient_info)

    return jsonify({"report": report})
