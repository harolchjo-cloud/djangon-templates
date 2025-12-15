import re

RULES = [
    (re.compile(r"\b(vacaci[oó]n|vacaciones|vacacion|licencia)\b", re.I),
     "Para solicitar vacaciones, crea una solicitud en el portal o contacta a RRHH. Dame tu nombre y fechas."),

    (re.compile(r"\b(cita|turno de cita|consultar cita|reservar cita)\b", re.I),
     "Para consultar tu cita, revisa el portal de empleados o escríbeme la fecha y te ayudo a verificarla."),

    (re.compile(r"\b(beneficio|beneficios|seguro|prestaciones)\b", re.I),
     "Los beneficios incluyen seguro médico y bonos. Revisa la documentación interna o contacta RRHH."),

    (re.compile(r"\b(hora|horario|entrada|salida|turno)\b", re.I),
     "El horario estándar es de 8:00 a 17:00 con 1 hora de almuerzo. Para cambios de turno, consulta con tu jefe directo."),

    (re.compile(r"\b(salario|pago|nomina|n[oó]mina)\b", re.I),
     "Para consultas de nómina, revisa con el departamento de Nómina o usa la API interna de nóminas."),

    (re.compile(r"\b(hola|buenas|buenos)\b", re.I),
     "¡Hola! Soy el asistente de RRHH. ¿En qué puedo ayudarte? Puedes preguntar sobre vacaciones, beneficios, horario o nómina."),
]

DEFAULT_REPLY = "Perdón, no entendí. Puedo ayudar con vacaciones, beneficios, horario o nómina."


def get_reply(message: str) -> str:
    """Devuelve una respuesta basada en reglas simples."""
    if not message or not message.strip():
        return "Por favor escribe tu pregunta."

    text = message.strip()
    for pattern, reply in RULES:
        if pattern.search(text):
            return reply

    # Preguntas abiertas
    if re.search(r"\b(c[oó]mo|qu[eé]|d[oó]nde|cu[aá]ndo|quien|quién)\b", text, re.I):
        return "Buena pregunta — ¿podrías dar más detalles para que pueda ayudarte mejor?"

    return DEFAULT_REPLY
