def city_country(city, country, population=None):

    if population:
        hasil = f"{city}, {country} - population {population}"
    else:
        hasil = f"{city}, {country}"

    return hasil.title()