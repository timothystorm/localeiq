from src.localeiq.routers.countries import get_country_list, get_countries_count


def test_get_country_list_not_empty():
    countries = get_country_list()
    assert isinstance(countries, list)
    assert len(countries) > 0


def test_get_country_list_structure():
    for country in get_country_list():
        assert "code" in country
        assert "name" in country
        assert isinstance(country["code"], str)
        assert isinstance(country["name"], str)


def test_get_countries_count():
    count_response = get_countries_count()
    assert isinstance(count_response, dict)
    assert "count" in count_response
    assert count_response["count"] == len(get_country_list())
