TIMEOUT = 10  
BASE_URL = "https://api.restcountries.com/countries/v5"

def test_get_all_countries(api):
    """Получить все страны."""
    response = api.get(f"{BASE_URL}", timeout=TIMEOUT)
    assert response.status_code == 200
    json_data = response.json()
    countries = json_data["data"]["objects"]
    assert len(countries) > 0, "Список стран не должен быть пустым"
    first_country = countries[0]
    assert "names" in first_country, "У страны должно быть поле 'names'"
    assert "common" in first_country["names"], "Должно быть общее название"
  
def test_get_country_by_name(api):
    """Поиск страны по названию."""
    query = "Germany"
    response = api.get(f"{BASE_URL}?q={query}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    countries = data["data"]["objects"]
    assert len(countries) > 0, "Список стран не должен быть пустым"
    country_name = countries[0]["names"]["common"], "Должно быть общее название"
    assert query in country_name

def test_get_country_by_alpha_code(api):
    """Поиск страны по буквенноу коду."""
    code = "GER"
    response = api.get(f"{BASE_URL}/code?q={code}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    countries = data["data"]["objects"]
    assert len(countries) == 1, "Должна быть найдена одна страна"
    assert code in countries[0]["codes"]["cioc"], "Код страны не совпадает"
    
def test_get_countries_by_region(api):
    """Поиск стран по названию региона."""
    region = "Europe"
    response = api.get(f"{BASE_URL}?region={region}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    countries = data["data"]["objects"]
    for country in countries:
        assert country["region"] == region, "Регионы найденных стран не совпадают с искомой"

def test_search_country_by_partial_name(api):
    """Поиск страны по части названия."""
    query = "united"
    response = api.get(f"{BASE_URL}/names.common?q={query}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    countries = data["data"]["objects"]
    names = [country["names"]["common"] for country in countries]
    assert any(query.lower() in name.lower() for name in names), "Искомая часть слова не найдена в ответе"
    
def test_non_existent_country(api):
    """Поиск несуществующей страны."""
    response = api.get(f"{BASE_URL}/names.common?q=d'xyz'")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]["objects"]) == 0, "Не должно быть найдено ни одной страны"
    assert data["data"]["meta"]["total"] == 0, "Сервер не должен найти ни одной страны"

def test_get_country_by_name_too_short(api):
    """Поиск по одной букве - допустим, но результат может быть любым."""
    response = api.get(f"{BASE_URL}?q=a", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data

def test_get_country_by_name_special_chars(api):
    """Поиск со спецсимволами - сервер должен отработать без ошибок."""
    response = api.get(f"{BASE_URL}?q=!@#$%", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]["objects"]) == 0

def test_get_country_by_name_empty_query(api):
    """Поиск с пустым запросом должен вернуть 400 или пустой список."""
    response = api.get(f"{BASE_URL}?q=", timeout=TIMEOUT)
    # API может вернуть 400 Bad Request или 200 с пустым списком
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        data = response.json()
        assert len(data["data"]["objects"]) == 0