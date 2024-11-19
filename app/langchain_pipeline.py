#! ****** Imports ******#

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import json

#! Endpoint Original Debe Usar la Versión Original del Pipeline


def generate_medical_report(patient_info):
    """
    Alias para la versión original del pipeline.
    """
    return generate_medical_report_original(patient_info)


#! ****** Helper Functions ******#


def extract_diagnosis_from_input(patient_info):
    """
    Extrae un diagnóstico del texto proporcionado por el usuario.

    Args:
        patient_info (str): Información clínica del paciente.

    Returns:
        str: Diagnóstico extraído.
    """
    # Lista de diagnósticos comunes como ejemplo
    common_diagnoses = [
        "radiculopatía bilateral C5",
        "neuropatía diabética",
        "migraña crónica",
        "espondilosis lumbar",
        "fibromialgia",
        "hernia de disco cervical",
        "tendinitis de hombro",
        "síndrome del túnel carpiano",
        "artritis reumatoide",
        "insuficiencia venosa crónica",
    ]

    # Buscar coincidencias con los diagnósticos
    for diagnosis in common_diagnoses:
        if diagnosis.lower() in patient_info.lower():
            return diagnosis

    # Si no se encuentra nada, devolver None
    return None


def retrieve_medical_data(diagnosis, field="diagnóstico"):
    """
    Recupera datos médicos de la base de datos JSON basada en el diagnóstico.

    Args:
        diagnosis (str): Diagnóstico a buscar.
        field (str): Campo de búsqueda (por defecto, "diagnóstico").

    Returns:
        dict: Datos médicos relevantes o None si no se encuentra nada.
    """
    if not diagnosis:
        return None

    try:
        # Cargar la base de datos desde el archivo JSON
        with open("medical_notes.json", "r") as file:
            medical_data = json.load(file)

        # Buscar en la base de datos
        for entry in medical_data:
            if diagnosis.lower() in entry.get(field, "").lower():
                return entry
    except FileNotFoundError:
        raise FileNotFoundError("El archivo medical_notes.json no fue encontrado.")

    # Si no se encuentra nada, devolver None
    return None


#! ****** Pipeline Principal ******#


def generate_medical_report_original(patient_info):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("No se encontró la clave API en las variables de entorno.")

    model = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)

    example_report = """
    Ejemplo de Informe Médico:
    **Informe Médico Detallado**

    **Paciente:** Juan Pérez
    **Edad:** 45 años
    **Diagnóstico:** Neuropatía Diabética
    **Motivo de Consulta:** Dolor crónico en extremidades inferiores.
    **Antecedentes Médicos:** Diabetes Mellitus Tipo 2, Hipertensión Arterial.
    **Examen Físico:** Disminución de la sensibilidad en los pies, reflejos osteotendinosos disminuidos.
    **Plan de Tratamiento:** Ajuste de medicación antidiabética, inicio de tratamiento con gabapentina.
    """

    prompt = f"""
    Eres un experto en medicina. Aquí hay un ejemplo de cómo debería ser un informe médico:
    {example_report}

    Genera un informe médico detallado para un paciente con la siguiente información clínica:
    {patient_info}

    **Instrucciones Importantes:**
    1. Si la información crítica está presente (edad, diagnóstico, etc.), genera un "Informe Médico Detallado" completo.
    2. Si falta información crítica, NO generes un informe completo. Devuelve una indicación clara de que la información es insuficiente para un informe detallado.
    3. Usa frases fijas como "Información no proporcionada" para campos faltantes, y mantén la consistencia en la terminología y estructura en cada generación.
    """

    messages = [
        {"role": "system", "content": "Eres un experto en medicina."},
        {"role": "user", "content": prompt},
    ]

    report = model.invoke(messages)
    return report.content.strip()


def generate_medical_report_with_rag(patient_info):
    """
    Versión con RAG que incluye recuperación de datos médicos antes de la generación.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("No se encontró la clave API en las variables de entorno.")

    # Recuperación de datos médicos
    diagnosis = extract_diagnosis_from_input(patient_info)
    retrieved_data = retrieve_medical_data(diagnosis)

    if retrieved_data:
        context = (
            f"Paciente: {retrieved_data['paciente']}\n"
            f"Fecha: {retrieved_data['fecha']}\n"
            f"Diagnóstico: {retrieved_data['diagnóstico']}\n"
            f"Síntomas: {retrieved_data['síntomas']}\n"
            f"Exámenes: {retrieved_data['examenes']}\n"
            f"Plan de Tratamiento: {retrieved_data['plan_de_tratamiento']}\n"
            f"Procedimientos: {', '.join([proc['nombre'] for proc in retrieved_data['procedimientos']])}\n"
            f"Notas: {retrieved_data['notas']}\n"
        )
    else:
        context = "No se encontraron datos médicos relevantes en la base de datos.\n\n"

    # Prompt actualizado con RAG
    prompt = f"""
    Eres un experto en medicina. Usa la información a continuación para generar un informe médico detallado:
    {context}
    Información adicional del paciente: {patient_info}
    """

    model = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)
    messages = [
        {"role": "system", "content": "Eres un experto en medicina."},
        {"role": "user", "content": prompt},
    ]

    report = model.invoke(messages)
    return report.content.strip()
