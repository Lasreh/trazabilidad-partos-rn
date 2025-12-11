# parto/models.py
from django.db import models
from django.conf import settings

# ----------------------
# App: parto/models.py
# ----------------------

# --- CHOICES extraídos del Libro Modelo Parto (claves cortas) ---
TIPO_PACIENTE_CHOICES = [
    ('INSTIT', 'Institucional'),
    ('PREH', 'Prehospitalario'),
    ('FUERA_RED', 'Fuera de la Red Asistencial'),
    ('DOM_PROF', 'Domicilio con Atención Profesional'),
    ('DOM_NOPROF', 'Domicilio sin Atención Profesional'),
]

ORIGEN_INGRESO_CHOICES = [
    ('URG', 'Urgencia'),
    ('SALA', 'Sala'),
    ('SAMU', 'Derivación SAMU'),
    ('CPREN', 'Control Prenatal'),
    ('HOSP', 'Hospitalización previa'),
    ('OTRO', 'Otro'),
]

TIPO_PARTO_CHOICES = [
    ('V_EUT', 'Parto vaginal eutócico'),
    ('V_INS', 'Parto vaginal instrumental'),
    ('CES_ELE', 'Cesárea electiva'),
    ('CES_URG', 'Cesárea urgencia'),
    ('POD', 'Presentación podálica'),
    ('GEM', 'Parto gemelar'),
    ('OTRO', 'Otro'),
]

# Clasificación Robson (grupos detectados en el libro)
ROBSON_CHOICES = [
    ('G1', 'Grupo 1'),
    ('G2A', 'Grupo 2.A'),
    ('G2B', 'Grupo 2.B'),
    ('G3', 'Grupo 3'),
    ('G4', 'Grupo 4'),
    ('G51', 'Grupo 5.1'),
    ('G52', 'Grupo 5.2'),
    ('G6', 'Grupo 6'),
    ('G7', 'Grupo 7'),
    ('G8', 'Grupo 8'),
    ('G9', 'Grupo 9'),
    ('G10', 'Grupo 10'),
]

POSICION_MATERNA_CHOICES = [
    ('SEMIS', 'Semisentada'),
    ('SENT', 'Sentada'),
    ('LIT', 'Litotomía'),
    ('DDOR', 'Decúbito Dorsal'),
    ('CUAD', 'Cuadrúpeda'),
    ('DLAT', 'Decúbito Lateral'),
    ('DEPIE', 'De Pie'),
    ('CUCL', 'Cuclillas'),
    ('OTRO', 'Otro'),
]

ESTADO_PERINE_CHOICES = [
    ('INDEM', 'Indemne'),
    ('EPIS', 'Episiotomía'),
    ('G1', 'Desgarro Grado 1'),
    ('G2', 'Desgarro Grado 2'),
    ('G3A', 'Desgarro Grado 3A'),
    ('G3B', 'Desgarro Grado 3B'),
    ('G3C', 'Desgarro Grado 3C'),
    ('G4', 'Desgarro Grado 4'),
    ('FIS', 'Fisura'),
]

TIPO_REGIMEN_CHOICES = [
    ('IOP', 'IOP'),
    ('RAM', 'RAM'),
    ('REM_COM', 'REM Común'),
    ('RPM', 'RPM'),
    ('OTRO', 'Otro'),
]

RESULTADO_EXAMEN_CHOICES = [
    ('REACT', 'Reactivo'),
    ('NO_REACT', 'No Reactivo'),
    ('POS', 'Positivo'),
    ('NEG', 'Negativo'),
]

PERSONA_ACOMP_CHOICES = [
    ('PAREJA', 'Pareja'),
    ('MADRE', 'Madre'),
    ('PADRE', 'Padre'),
    ('AMIGA', 'Amiga'),
    ('HERMANA', 'Hermana'),
    ('DOULA', 'Doula'),
    ('NINGUNA', 'Ninguna'),
    ('OTRO', 'Otro'),
]

# ----------------------
# Modelos
# ----------------------

class Parto(models.Model):
    # Relación con paciente (de la app pacientes)
    paciente = models.ForeignKey('pacientesApp.Paciente', on_delete=models.CASCADE, related_name="partos")

    # Relaciones convertidas a choices (se reemplazaron las FK a catalogos)
    tipo_paciente = models.CharField(max_length=10, choices=TIPO_PACIENTE_CHOICES, null=True, blank=True)
    origen_ingreso = models.CharField(max_length=10, choices=ORIGEN_INGRESO_CHOICES, null=True, blank=True)
    tipo_parto = models.CharField(max_length=10, choices=TIPO_PARTO_CHOICES, null=True, blank=True)
    clasificacion_robson = models.CharField(max_length=10, choices=ROBSON_CHOICES, null=True, blank=True)
    posicion_materna = models.CharField(max_length=10, choices=POSICION_MATERNA_CHOICES, null=True, blank=True)
    estado_perine = models.CharField(max_length=10, choices=ESTADO_PERINE_CHOICES, null=True, blank=True)
    tipo_regimen = models.CharField(max_length=10, choices=TIPO_REGIMEN_CHOICES, null=True, blank=True)

    # Datos del parto
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    plan_parto = models.BooleanField(default=False)
    visita_guiada = models.BooleanField(default=False)
    imc = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    paridad = models.IntegerField(null=True, blank=True)
    control_prenatal = models.BooleanField(default=False)
    consultorio_origen = models.CharField(max_length=150, null=True, blank=True)
    nro_aro = models.IntegerField(null=True, blank=True)
    sem_obst_semanas = models.IntegerField(null=True, blank=True)
    sem_obst_dias = models.IntegerField(null=True, blank=True)
    monitor = models.BooleanField(default=False)
    ttc = models.BooleanField(default=False)
    induccion = models.BooleanField(default=False)
    aceleracion = models.BooleanField(default=False)
    nro_tv = models.IntegerField(null=True, blank=True)
    rotura_membrana = models.BooleanField(default=False)
    tiempo_membranas_rotas = models.CharField(max_length=50, null=True, blank=True)
    tiempo_dilatacion = models.CharField(max_length=50, null=True, blank=True)
    tiempo_expulsivo = models.CharField(max_length=50, null=True, blank=True)
    libertad_movimiento = models.BooleanField(default=False)
    alumbramiento_dirigido = models.BooleanField(default=False)
    ofrecimiento_posiciones = models.BooleanField(default=False)
    esterilizacion = models.BooleanField(default=False)
    revision = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)
    uso_sala_saip = models.BooleanField(default=False)
    folio_valido = models.BooleanField(default=False)
    folio_nulo = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Parto"
        verbose_name = "Parto"
        verbose_name_plural = "Partos"
        indexes = [
            models.Index(fields=['paciente'], name='idx_parto_paciente'),
            models.Index(fields=['fecha'], name='idx_parto_fecha'),
        ]

    def __str__(self):
        return f"Parto {self.id} - {self.paciente.nombre_completo() if self.paciente else 'sin paciente'}"


class Examenes(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="examenes")
    vih_preparto = models.BooleanField(default=False)
    vih_sala = models.BooleanField(default=False)
    pesquisa = models.CharField(max_length=100, null=True, blank=True)
    resultado_vih = models.CharField(max_length=10, choices=RESULTADO_EXAMEN_CHOICES, null=True, blank=True)
    antibiotico_sgb = models.BooleanField(default=False)
    resultado_vdrl = models.CharField(max_length=10, choices=RESULTADO_EXAMEN_CHOICES, null=True, blank=True)
    tratamiento_sifilis = models.BooleanField(default=False)
    examen_hepatitis_b = models.BooleanField(default=False)
    derivacion_hepatologo = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Examenes"
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"

    def __str__(self):
        return f"Exámenes Parto {self.parto_id}"


class Patologia(models.Model):
    parto = models.ForeignKey(Parto, on_delete=models.CASCADE, related_name="patologias")
    preeclampsia_severa = models.BooleanField(default=False)
    eclampsia = models.BooleanField(default=False)
    sepsis_grave = models.BooleanField(default=False)
    infeccion_ovular = models.BooleanField(default=False)
    otra_patologia = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Patologia"
        verbose_name = "Patología"
        verbose_name_plural = "Patologías"

    def __str__(self):
        return f"Patología {self.id} - Parto {self.parto_id}"


class Procedimiento(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="procedimiento")
    inercia_uterina = models.BooleanField(default=False)
    restos_placentarios = models.BooleanField(default=False)
    trauma = models.BooleanField(default=False)
    alteracion_coagulacion = models.BooleanField(default=False)
    manejo_quirurgico = models.BooleanField(default=False)
    histerectomia = models.BooleanField(default=False)
    transfusion = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Procedimiento"
        verbose_name = "Procedimiento"
        verbose_name_plural = "Procedimientos"

    def __str__(self):
        return f"Procedimiento Parto {self.parto_id}"


class Anestesia(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="anestesia")

    neuroaxial = models.BooleanField(default=False)
    oxido_nitroso = models.BooleanField(default=False)
    analgesia_endovenosa = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    local = models.BooleanField(default=False)
    no_farmacologica = models.BooleanField(default=False)
    balon_kinesico = models.BooleanField(default=False)
    lenteja_parto = models.BooleanField(default=False)
    rebozo = models.BooleanField(default=False)
    aromaterapia = models.BooleanField(default=False)

    peridural_solicitada = models.BooleanField(default=False)
    peridural_indicada = models.BooleanField(default=False)
    peridural_administrada = models.BooleanField(default=False)
    tiempo_espera_peridural = models.CharField(max_length=50, null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Anestesia"
        verbose_name = "Anestesia"
        verbose_name_plural = "Anestesias"

    def __str__(self):
        return f"Anestesia Parto {self.parto_id}"


class Apego(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="apego")
    tiempo_apego = models.CharField(max_length=50, null=True, blank=True)
    apego_canguro = models.BooleanField(default=False)
    acomp_preparto = models.BooleanField(default=False)
    acomp_parto = models.BooleanField(default=False)
    acomp_rn = models.BooleanField(default=False)
    motivo_no_acompanamiento = models.TextField(null=True, blank=True)
    persona_acompanante = models.CharField(max_length=10, choices=PERSONA_ACOMP_CHOICES, null=True, blank=True)
    corta_cordon = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Apego"
        verbose_name = "Apego"
        verbose_name_plural = "Apegos"

    def __str__(self):
        return f"Apego Parto {self.parto_id}"


class Profesionales(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="profesionales")
    responsable = models.CharField(max_length=200, null=True, blank=True)
    alumno = models.CharField(max_length=200, null=True, blank=True)
    causa_cesarea = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Profesionales"
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"Profesionales Parto {self.parto_id}"


class OtrosDatos(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="otrosdatos")
    ley_dominga = models.BooleanField(default=False)
    placenta = models.BooleanField(default=False)
    registro_civil = models.BooleanField(default=False)
    recuerdos_entregados = models.BooleanField(default=False)
    motivo_no_recuerdos = models.TextField(null=True, blank=True)
    retira_placenta = models.BooleanField(default=False)
    estampado_placenta = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "OtrosDatos"
        verbose_name = "Otros Datos"
        verbose_name_plural = "Otros Datos"

    def __str__(self):
        return f"OtrosDatos Parto {self.parto_id}"