from langchain_openai import ChatOpenAI  # Usar la importación desde langchain_openai
import os
from dotenv import load_dotenv


def generate_medical_report(patient_info):
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la clave API desde la configuración
    api_key = os.getenv("OPENAI_API_KEY")

    # Verificar que la clave API no sea None
    if api_key is None:
        raise ValueError("No se encontró la clave API en las variables de entorno.")

    # Configurar el modelo ChatOpenAI con la clave API
    model = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)

    # Crear el prompt específico para generar un informe médico
    messages = [
        {"role": "system", "content": "Eres un experto en medicina."},
        {
            "role": "user",
            "content": f"Genera un informe médico detallado para un paciente con la siguiente información clínica: {patient_info}",
        },
    ]

    # Generar el informe médico
    report = model.invoke(messages)  # Usar invoke en lugar de __call__

    return report.content.strip()


# patient_info = "Paciente de 45 años con neuropatía diabética y dolor crónico en extremidades inferiores."
# report = generate_medical_report(patient_info)
# print(report)
