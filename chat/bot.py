import re

# Motor de respuestas simple basado en reglas
RULES = [
    (re.compile(r"\b(vacaci[oó]n|vacaciones|vacacion|licencia)\b", re.I),
     "Para solicitar vacaciones, crea una solicitud en el portal o contacta a RRHH. Necesito tu nombre y fechas para generar un borrador."),

    (re.compile(r"\b(beneficio|beneficios|seguro|prestaciones)\b", re.I),
     "Los beneficios disponibles incluyen seguro médico y bonos. Revisa /api/v3/beneficios/ o contacta a RRHH para más detalles."),

    (re.compile(r"\b(hora|horario|entrada|salida|turno)\b", re.I),
     "El horario estándar es de 8:00 a 17:00 con 1 hora de almuerzo. Para cambios de turno, consulta con tu jefe directo."),

    (re.compile(r"\b(salario|pago|nomina|n[oó]mina)\b", re.I),
     "Para consultas de nómina, revisa /api/v3/nominas/ o contacta al departamento de Nómina."),

    (re.compile(r"\b(hola|hola|buenas|buenos)\b", re.I),
     "¡Hola! Soy el asistente de RRHH. ¿En qué puedo ayudarte? Puedes preguntar sobre vacaciones, beneficios, horario o nómina."),
]

DEFAULT_REPLY = "Perdón, no entendí. Puedo ayudar con vacaciones, beneficios, horario o nómina."


def get_reply(message: str) -> str:
    """Devuelve una respuesta basada en reglas simples."""
    text = message.strip()
    if not text:
        return "Por favor escribe tu pregunta."

    for pattern, reply in RULES:
        if pattern.search(text):
            return reply

    # Reglas simples para preguntas con ¿quién? ¿cómo? etc.
    if re.search(r"\b(c[oó]mo|qu[eé]|d[oó]nde|cu[aá]ndo|quien|quién)\b", text, re.I):
        return "Buena pregunta — ¿podrías dar más detalles para que pueda ayudarte mejor?"

    return DEFAULT_REPLY
