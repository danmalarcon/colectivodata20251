import pandas as pd
from datetime import datetime

# Cargar el archivo Excel con manejo de errores
try:
    dataFrameUsuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")
    exit()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Asegurarse de que las columnas relevantes no tengan valores nulos
dataFrameUsuarios['especialidad'] = dataFrameUsuarios['especialidad'].fillna("")
dataFrameUsuarios['direccion'] = dataFrameUsuarios['direccion'].fillna("")
dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')

# Filtros y consultas
# 1. Solo estudiantes
soloEstudiantes = dataFrameUsuarios.query('tipo_usuario == "estudiante"')
print(soloEstudiantes)

# 2. Solo profesores
soloProfesores = dataFrameUsuarios.query('tipo_usuario == "profesor"')
print(soloProfesores)

# 3. Todos excepto estudiantes
sinEstudiantes = dataFrameUsuarios.query('tipo_usuario != "estudiante"')
print(sinEstudiantes)

# 4. Filtrar por especialidad (ejemplo: "Matemáticas")
especialidadFiltro = dataFrameUsuarios.query('especialidad == "Matemáticas"')
print(especialidadFiltro)

# 5. Excluir una especialidad (ejemplo: "Informática")
sinEspecialidadFiltro = dataFrameUsuarios.query('especialidad != "Informática"')
print(sinEspecialidadFiltro)

# 6. Excluir administrativos
sinAdministrativos = dataFrameUsuarios.query('tipo_usuario != "administrativo"')
print(sinAdministrativos)

# 7. Direcciones en Medellín
medellinDirecciones = dataFrameUsuarios.query('direccion.str.contains("Medellín")', engine="python")
print(medellinDirecciones)

# 8. Direcciones terminadas en "Sur"
direccionesSur = dataFrameUsuarios.query('direccion.str.endswith("Sur")', engine="python")
print(direccionesSur)

# 9. Direcciones que inician con "Calle"
direccionesCalle = dataFrameUsuarios.query('direccion.str.startswith("Calle")', engine="python")
print(direccionesCalle)

# 10. Especialidades que contienen la palabra "datos"
especialidadDatos = dataFrameUsuarios.query('especialidad.str.contains("datos", case=False, na=False)', engine="python")
print(especialidadDatos)

# 11. Instructores en Itagüí
instructoresItagui = dataFrameUsuarios.query('tipo_usuario == "instructor" and direccion.str.contains("Itagüí")', engine="python")
print(instructoresItagui)

# 12. Nacidos después del 2000
nacidos2000 = dataFrameUsuarios.query('fecha_nacimiento > "2000-01-01"')
print(nacidos2000)

# 13. Nacidos en los 90
nacidos90 = dataFrameUsuarios.query('fecha_nacimiento >= "1990-01-01" and fecha_nacimiento < "2000-01-01"')
print(nacidos90)

# 14. Direcciones en Envigado
envigadoDirecciones = dataFrameUsuarios.query('direccion.str.contains("Envigado")', engine="python")
print(envigadoDirecciones)

# 15. Especialidades que empiezan por "I"
especialidadI = dataFrameUsuarios.query('especialidad.str.startswith("I")', engine="python")
print(especialidadI)

# 16. Usuarios sin dirección
sinDireccion = dataFrameUsuarios.query('direccion == ""')
print(sinDireccion)

# 17. Usuarios sin especialidad
sinEspecialidad = dataFrameUsuarios.query('especialidad == ""')
print(sinEspecialidad)

# 18. Profesores que viven en Sabaneta
profesoresSabaneta = dataFrameUsuarios.query('tipo_usuario == "profesor" and direccion.str.contains("Sabaneta")', engine="python")
print(profesoresSabaneta)

# 19. Aprendices que viven en Bello
aprendicesBello = dataFrameUsuarios.query('tipo_usuario == "aprendiz" and direccion.str.contains("Bello")', engine="python")
print(aprendicesBello)

# 20. Nacidos en el nuevo milenio (2000 en adelante)
nacidosNuevoMilenio = dataFrameUsuarios.query('fecha_nacimiento >= "2000-01-01"')
print(nacidosNuevoMilenio)

# Agrupaciones y cálculos
# 1. Total por tipo de usuario
totalPorTipo = dataFrameUsuarios['tipo_usuario'].value_counts()
print(totalPorTipo)

# 2. Total por especialidad
totalPorEspecialidad = dataFrameUsuarios['especialidad'].value_counts()
print(totalPorEspecialidad)

# 3. Cantidad de especialidades distintas
cantidadEspecialidades = dataFrameUsuarios['especialidad'].nunique()
print(cantidadEspecialidades)

# 4. Tipos de usuario por especialidad
tiposPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['tipo_usuario'].value_counts()
print(tiposPorEspecialidad)

# 5. Usuario más antiguo por tipo
usuarioMasAntiguo = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].min()
print(usuarioMasAntiguo)

# 6. Usuario más joven por tipo
usuarioMasJoven = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].max()
print(usuarioMasJoven)

# 7. Primer registro por tipo
primerRegistro = dataFrameUsuarios.groupby('tipo_usuario').first()
print(primerRegistro)

# 8. Último registro por tipo
ultimoRegistro = dataFrameUsuarios.groupby('tipo_usuario').last()
print(ultimoRegistro)

# 9. Combinación de tipo y especialidad
combinacionTipoEspecialidad = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size()
print(combinacionTipoEspecialidad)

# 10. El más viejo por especialidad
masViejoPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].min()
print(masViejoPorEspecialidad)

# 11. Cuántos de cada especialidad por tipo
cantidadPorEspecialidadTipo = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size()
print(cantidadPorEspecialidadTipo)

# 12. Edad promedio por tipo
current_date = datetime(2025, 5, 7)
dataFrameUsuarios['edad'] = current_date.year - pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year
edadPromedioPorTipo = dataFrameUsuarios.groupby('tipo_usuario')['edad'].mean()
print(edadPromedioPorTipo)

# 13. Año de nacimiento más frecuente por especialidad
anioNacimientoFrecuente = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].apply(pd.Series.mode)
print(anioNacimientoFrecuente)

# 14. Mes de nacimiento más frecuente por tipo
mesNacimientoFrecuente = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].apply(pd.Series.mode)
print(mesNacimientoFrecuente)

# 15. Especialidades más comunes entre estudiantes
especialidadesEstudiantes = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] == 'estudiante']['especialidad'].value_counts()
print(especialidadesEstudiantes)