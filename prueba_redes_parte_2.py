
import urllib.parse
import requests

main_cesar_leiva = "https://www.mapquestapi.com/directions/v2/route?" 
llave_cesar_leiva = "pC0eXuTP3pJlTNn85GxbAoafz6MDH94G"

def millas_a_kilometros(millas):
    kilometros = millas * 1.60934
    return kilometros

def calcular_consumo(distancia, rendimiento):
    litros_combustible = distancia / rendimiento
    return litros_combustible

while True:
    origen_cesar_leiva = input("Inicio: ")
    if origen_cesar_leiva == "salir" or origen_cesar_leiva == "ok":
        break
    destino_cesar_leiva = input("Destino: ")
    if destino_cesar_leiva == "salir" or destino_cesar_leiva == "OK":
        break 

    url = main_cesar_leiva + urllib.parse.urlencode({"key": llave_cesar_leiva, "from":origen_cesar_leiva, "to":destino_cesar_leiva})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Dirección desde " + origen_cesar_leiva + " hasta " + destino_cesar_leiva)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])

        distancia_millas = json_data["route"]["distance"]
        distancia_kilometros = millas_a_kilometros(distancia_millas)
        print("Distancia: {:.2f} millas".format(distancia_millas))
        print("Distancia: {:.2f} kilómetros".format(distancia_kilometros))

        print("=============================================")
        print("Consumo de combustible:")

        while True:
            tipo_vehiculo = input("Ingrese tipo de vehículo: (City Car, Sedan, SUV):    ").lower()
            if tipo_vehiculo == "city car":
                consumo = calcular_consumo(distancia_kilometros, 20)
                print("City Car: {:.2f} litros".format(consumo))
                break
            elif tipo_vehiculo == "sedan":
                consumo = calcular_consumo(distancia_kilometros, 15)
                print("Sedan: {:.2f} litros".format(consumo))
                break
            elif tipo_vehiculo == "suv":
                consumo = calcular_consumo(distancia_kilometros, 12)
                print("SUV: {:.2f} litros".format(consumo))
                break
            else:
                print("ERROR. Por favor, ingrese City Car, Sedan o SUV.")

        print("=============================================")

        costo_litro_bencina = 1308

        costo_total_bencina = consumo * costo_litro_bencina
        print("Costo total de bencina(97): CLP {:.2f}".format(costo_total_bencina))

        print("========================================================")
        print("Instrucciones de manejo:")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61)) + " km)")

