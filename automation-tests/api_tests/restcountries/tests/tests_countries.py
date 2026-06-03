BASE_URL = "https://restcountries.com/v3.1"
TIMEOUT = 10  

def test_get_all_countries(api):
    response = api.get(f"{BASE_URL}/all?fields=name,capital,currences", timeout=TIMEOUT)
    assert response.status_code == 200
    countries = response.json()
    for country in countries:
        assert "name" in country

def test_get_country_by_name(api):
    name = "Germany"
    response = api.get(f"{BASE_URL}/name/{name}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"]["common"] == name

def test_get_country_by_alpha_code(api):
    code = "de"
    response = api.get(f"{BASE_URL}/alpha/{code}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["cca2"].lower() == code

def test_get_countries_by_region(api):
    region = "Europe"
    response = api.get(f"{BASE_URL}/region/{region}", timeout=TIMEOUT)
    assert response.status_code == 200
    countries = response.json()
    for country in countries:
        assert country["region"] == region

def test_search_country_by_partial_name(api):
    query = "united"
    response = api.get(f"{BASE_URL}/name/{query}", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    names = [country["name"]["common"] for country in data]
    assert any("United" in name for name in names)
    
def test_non_existent_country(api):
    response = api.get(f"{BASE_URL}/name/xyz")
    assert response.status_code == 404