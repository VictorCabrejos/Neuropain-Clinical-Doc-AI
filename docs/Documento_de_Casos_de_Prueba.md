
# Documento de Casos de Prueba

## TC-001: Generación de Informe con Input Válido
- **Descripción:** Verifica que la API genere un informe médico válido cuando se le proporciona información completa del paciente.
- **Precondiciones:** La API debe estar en ejecución y accesible.
- **Pasos:**
  1. Enviar una solicitud POST al endpoint `/generate_report` con un JSON que contenga la información del paciente.
- **Entrada:** 
  ```json
  {
    "patient_info": "Paciente de 45 años con neuropatía diabética y dolor crónico en extremidades inferiores."
  }
  ```
- **Resultados Esperados:** La respuesta debe contener un informe médico con las secciones "Informe Médico Detallado", "Motivo de Consulta", "Antecedentes Médicos", y "Examen Físico".
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]

## TC-002: Manejo de Input Vacío
- **Descripción:** Verifica que la API maneje adecuadamente un input vacío.
- **Precondiciones:** La API debe estar en ejecución y accesible.
- **Pasos:**
  1. Enviar una solicitud POST al endpoint `/generate_report` con un JSON vacío.
- **Entrada:** 
  ```json
  {
    "patient_info": ""
  }
  ```
- **Resultados Esperados:** La respuesta no debe estar vacía, y no debe contener errores.
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]
