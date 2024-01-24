def encode_geohash(latitude, longitude, precision=12):
    """
    Converte latitude e longitude para Geohash.

    Parâmetros:
    - latitude: Latitude em graus decimais.
    - longitude: Longitude em graus decimais.
    - precision: Precisão do Geohash (número de caracteres). Padrão é 12.

    Retorna:
    - Uma string representando o Geohash.
    """
    base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
    lat_range = (-90.0, 90.0)
    lon_range = (-180.0, 180.0)

    geohash = ""
    bits = 0
    ch = 0
    even = True

    while len(geohash) < precision:
        if even:
            mid = (lon_range[0] + lon_range[1]) / 2
            if longitude > mid:
                ch |= (1 << bits)
                lon_range = (mid, lon_range[1])
            else:
                lon_range = (lon_range[0], mid)
        else:
            mid = (lat_range[0] + lat_range[1]) / 2
            if latitude > mid:
                ch |= (1 << bits)
                lat_range = (mid, lat_range[1])
            else:
                lat_range = (lat_range[0], mid)

        even = not even
        bits += 1

        if bits == 5:
            geohash += base32[ch]
            bits = 0
            ch = 0

    return geohash

# Exemplo de uso:
latitude = 27.5948
longitude = -48.5569
precision = 12
geohash_result = encode_geohash(latitude, longitude, precision)
print(f"Latitude: {latitude}, Longitude: {longitude} -> Geohash: {geohash_result}")
