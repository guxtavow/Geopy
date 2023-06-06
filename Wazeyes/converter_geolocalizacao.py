from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereço com numero e cidade:  ")
resultado = str(geolocator.geocode(endereco)).split(",")
if resultado[0]!='None':
    print("Endereço Completo: ", resultado)
    print("Bairro...........: ", resultado[1])
    print("Cidade...........: ", resultado[2])
    print("Regiao...........: ", resultado[3])