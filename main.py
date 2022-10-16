import random
import time
def calefactor(medicion, temp_actual):
    # Calefactor encendido
    if temp_actual<medicion:
        estado = True
        medicion = temp_actual + random.uniform(0,2)
    else:
    # Calefactor apagado
        estado = False
        medicion = temp_actual - random.uniform(0,2)
  
    linea = '{:.2f};{}\n'.format(medicion, estado)
    print(linea)
    archivo.write(linea)
    
    return medicion

tpo_funcion = int(input('Ingrese el tiempo en segundos de funcionamiento total del programa : '))
tpo_muestra = int(input('Ingrese el tiempo en segundos de cada medicion : '))
tem_calefac = int(input('Ingrese la Temperatura deseada : '))
tem_ambien = int(random.randint(0,35))
tpo_operando = 0
medicion = 0
archivo = open('log-tempinicial_'+str(tem_ambien)+'-temcalefactor_'+str(tem_calefac)+'-tiempototal_'+str(tpo_funcion)+'-tiempomedicion_'+str(tpo_muestra)+'.csv', 'w')
while tpo_operando <= tpo_funcion:
    medicion = calefactor(tem_calefac,tem_ambien)
    tem_ambien = medicion
    time.sleep(tpo_muestra)
    tpo_operando += tpo_muestra
archivo.close()

