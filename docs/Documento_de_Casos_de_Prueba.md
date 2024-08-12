
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
- **Resultados Esperados:** La respuesta debe contener un informe médico con secciones clave como "Informe Médico", "Motivo de Consulta", "Antecedentes Médicos", y "Examen Físico". Se permite cierta flexibilidad en la estructura exacta del texto.
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
- **Resultados Esperados:** La respuesta no debe estar vacía y no debe contener errores inesperados. Debe manejar el caso adecuadamente sin inventar detalles no proporcionados.
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]

## TC-003: Prueba de Alucinaciones
- **Descripción:** Verifica que el modelo no genere información inventada (alucinaciones) cuando se le proporciona un input ambiguo o con poca información.
- **Precondiciones:** La API debe estar en ejecución y accesible.
- **Pasos:**
  1. Enviar una solicitud POST al endpoint `/generate_report` con un JSON que contenga una información ambigua del paciente.
- **Entrada:** 
  ```json
  {
    "patient_info": "Paciente con síntomas generales."
  }
  ```
- **Resultados Esperados:** La respuesta debe ser genérica y no contener información detallada que no haya sido proporcionada explícitamente. No debe incluir diagnósticos o tratamientos específicos a menos que se mencione en el input.
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]

## TC-004: Prueba con Input Parcialmente Completo
- **Descripción:** Verifica cómo el sistema maneja inputs donde la información del paciente es parcial.
- **Precondiciones:** La API debe estar en ejecución y accesible.
- **Pasos:**
  1. Enviar una solicitud POST al endpoint `/generate_report` con un JSON que contenga información incompleta del paciente.
- **Entrada:** 
  ```json
  {
    "patient_info": "Paciente de 60 años con diabetes."
  }
  ```
- **Resultados Esperados:** El informe debe reflejar la falta de información sin inventar detalles adicionales como hipertensión u otros diagnósticos no mencionados en el input.
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]

## TC-005: Prueba de Respuestas Consistentes
- **Descripción:** Verifica que el modelo genere respuestas consistentes cuando se le proporciona la misma entrada varias veces.
- **Precondiciones:** La API debe estar en ejecución y accesible.
- **Pasos:**
  1. Enviar una solicitud POST al endpoint `/generate_report` con un JSON que contenga información del paciente.
  2. Repetir la solicitud con el mismo JSON.
  3. Comparar las respuestas para asegurarse de que sean consistentes en elementos clave.
- **Entrada:** 
  ```json
  {
    "patient_info": "Paciente de 50 años con hipertensión y dolor de cabeza recurrente."
  }
  ```
- **Resultados Esperados:** Las respuestas deben contener los mismos elementos clave (como "hipertensión"), aunque el texto pueda variar ligeramente. No se espera una coincidencia exacta, pero sí una consistencia en el contenido crítico.
- **Resultado Real:** [Completar después de la ejecución]
- **Estado:** [Pasa/Falla]
