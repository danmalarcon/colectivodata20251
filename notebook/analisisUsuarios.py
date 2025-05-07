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