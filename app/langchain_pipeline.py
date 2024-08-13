from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


def generate_medical_report(patient_info):
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
