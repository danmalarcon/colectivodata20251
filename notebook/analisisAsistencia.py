import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# ANTES DE FILTRAR COMO ANALISTA DE DATOS DBEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
# print(dataFrameAsistencia['estado'].unique())
# print(dataFrameAsistencia['estrato'].unique())
# print(dataFrameAsistencia['medio_transporte'].unique())


#FILTRO Y CONDICIONES PARA TRANSFORMAR DATOS
# 1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron = dataFrameAsistencia.query('estado == "asistio"')
print(estudiantesQueAsistieron)
# 2. Todos los estudiantes que faltaron
estudiantesQueNoAsistieron = dataFrameAsistencia.query('estado == "inasistencia"')
print(estudiantesQueNoAsistieron)
# 3. Reportar todos los estudiantes que llegaron tarde (Justificado)
estudiantesTardeJustificado = dataFrameAsistencia.query('estado == "tarde_justificado"')
print(estudiantesTardeJustificado)
# 4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno = dataFrameAsistencia.query('estrato == 1')
print(estudiantesEstratoUno)
# 5. Reportar todos los estudiantes de estratos altos
estudiantesEstratosAltos = dataFrameAsistencia.query('estrato >= 4')
print(estudiantesEstratosAltos)
# 6. Reportar todos los estudiantes que llegan en Metro
estudiantesQueUsanMetro = dataFrameAsistencia.query('medio_transporte == "metro"')
# 7. Reportar todos los estudiantes que llegan en bicicleta
estudiantesEnBicicleta = dataFrameAsistencia.query('medio_transporte == "bicicleta"')
print(estudiantesEnBicicleta)
# 8. Reportar todos los estudiantes que no caminan para llegar a la U
estudiantesQueNoCaminan = dataFrameAsistencia.query('medio_transporte != "a pie"')
# 9. Reportar todos los registros de asistencia del mes de junio
dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'])
asistenciasJunio = dataFrameAsistencia[dataFrameAsistencia['fecha'].dt.month == 6]
print(asistenciasJunio)
# 10. Reportar los estudiantes que faltaron y usan BUS para llegar a la U
estudiantesQueFaltanUsanBus = dataFrameAsistencia.query('medio_transporte == "bus" and estado == "inasistencia"')
print(estudiantesQueFaltanUsanBus)
# 11. Reportar los estudiantes que usan bus y son de estratos altos
busEstratoAlto = dataFrameAsistencia.query('medio_transporte == "bus" and estrato >= 4')
print(busEstratoAlto)
# 12. Reportar estudiantes que usan bus y son de estratos bajos
busEstratoBajo = dataFrameAsistencia.query('medio_transporte == "bus" and estrato <= 2')
print(busEstratoBajo)
# 13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
tardeEstratosAltos = dataFrameAsistencia.query('estado == "tarde_justificado" and estrato >= 3')
print(tardeEstratosAltos)
# 14. Reportar estudiantes que usan transportes ecologicos
ecologicos = dataFrameAsistencia.query('medio_transporte in ["bicicleta", "a pie"]')
print(ecologicos)
# 15. Reportar estudiantes que faltan y usan carro para transportarse
faltanCarro = dataFrameAsistencia.query('estado == "inasistencia" and medio_transporte == "carro"')
print(faltanCarro)
# 16. Reportar estudiantes que asisten son estratos altos y caminan
asistenAltosCaminan = dataFrameAsistencia.query('estado == "asistio" and estrato >= 4 and medio_transporte == "a pie"')
print(asistenAltosCaminan) 
# 17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
bajoJustificanInasistencia = dataFrameAsistencia.query('estado == "inasistencia_justificada" and estrato <= 2')
print(bajoJustificanInasistencia)  
# 18. Reportar estudiantes que son estratos altos y justifican su inasistencia
altoJustificanInasistencia = dataFrameAsistencia.query('estado == "inasistencia_justificada" and estrato >= 4')
print(altoJustificanInasistencia)
# 19. Reportar estudiantes que usan carro y justifican su inasistencia
carroJustificanInasistencia = dataFrameAsistencia.query('medio_transporte == "carro" and estado == "inasistencia_justificada"')
print(carroJustificanInasistencia)
# 20. Reportar estudiantes que faltan y usan metro y son estratos medios
faltanMetroEstratoMedio = dataFrameAsistencia.query('estado == "inasistencia" and medio_transporte == "metro" and estrato == 3')
print(faltanMetroEstratoMedio)





# AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
# 1. Contrar cada registro de asistencia por cada estado
conteoRegistrosPorEstado = dataFrameAsistencia.groupby('estado').size()
print(conteoRegistrosPorEstado)
# 2. Numero de registros por estrato, es decir, cuantos faltan de estrato X, asistencias, inasistencia por estrato
conteoRegistrosPorEstrato = dataFrameAsistencia.groupby('estrato').size()
print(conteoRegistrosPorEstrato)
# 3. Cantidad de estudiantes por medio de transporte
conteoPorMedio = dataFrameAsistencia['medio_transporte'].value_counts()
print(conteoPorMedio)
# 4. Cantidad de registro por id_grupo
conteoPorid_grupo = dataFrameAsistencia['id_grupo'].value_counts()
print(conteoPorid_grupo)
# 5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte = dataFrameAsistencia.groupby(['estado', 'medio_transporte']).size()
print(cruceEstadoMedioTransporte)
# 6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)
# 7. Estrato Promedio por medio de transporte
promedioEstratoTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
print(promedioEstratoTransporte)
# 8. Maximo estrato por estado de asistencia
maxEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].max()
print(maxEstratoPorEstado)
# 9. Minimo estrato por estado de asistencia
minEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].min()
print(minEstratoPorEstado)
# 10. Conteo de asistencias por id_grupo y por estado
conteoid_grupoEstado = dataFrameAsistencia.groupby(['id_grupo', 'estado']).size()
print(conteoid_grupoEstado)
# 11. Transporte usado por cada id_grupo
transportePorid_grupo = dataFrameAsistencia.groupby('id_grupo')['medio_transporte'].value_counts()
print(transportePorid_grupo)
# 12. Cuantos id_grupos distintos registraron asistencia por fecha
id_gruposPorFecha = dataFrameAsistencia.groupby('fecha')['id_grupo'].nunique()
print(id_gruposPorFecha) 
# 13. Promedio de estrato por fecha
promedioEstratoFecha = dataFrameAsistencia.groupby('fecha')['estrato'].mean()
print(promedioEstratoFecha)
# 14. Numero de tipos de estado por transporte
tiposEstadoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estado'].nunique()
print(tiposEstadoPorTransporte)
# 15. Primer registro de cada id_grupo
primerRegistroPorid_grupo = dataFrameAsistencia.sort_values('fecha').groupby('id_grupo').first()
print(primerRegistroPorid_grupo)