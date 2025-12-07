# utils/validators.py
from django.core.exceptions import ValidationError

def limpiar_rut(rut):
    """Elimina puntos, guiones y espacios de un RUT."""
    return str(rut).replace(".", "").replace("-", "").replace(" ", "")

def validar_rut_chileno(rut, dv):
    """
    Valida un RUT chileno (7 u 8 dígitos antes del DV).
    """
    rut = limpiar_rut(rut)
    numero = str(rut)

    # Validar longitud: 7 o 8 dígitos
    if len(numero) not in [7, 8]:
        raise ValidationError("RUT inválido: debe tener 7 u 8 dígitos antes del DV.")

    dv = dv.upper()

    # Cálculo del dígito verificador
    suma = 0
    factor = 2
    for digito in reversed(numero):
        suma += int(digito) * factor
        factor = factor + 1 if factor < 7 else 2

    mod = suma % 11
    dv_calculado = 11 - mod
    if dv_calculado == 10:
        dv_calculado = "K"
    elif dv_calculado == 11:
        dv_calculado = "0"
    else:
        dv_calculado = str(dv_calculado)

    if dv != dv_calculado:
        raise ValidationError(f"RUT inválido. DV correcto: {dv_calculado}")
