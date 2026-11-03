def city_country(city, country):
    """Kembalikan string 'Kota, Negara'."""
    return f"{city}, {country}".title()

print(city_country('santiago', 'chile'))
print(city_country('semarang', 'indonesia'))
print(city_country('tokyo', 'jepang'))