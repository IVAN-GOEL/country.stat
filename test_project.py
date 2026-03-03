from main import fetch_indicator, summarize_data, generate_chart
import pytest
import os

# ── fetch_indicator ──────────────────────────────────────────────
def test_fetch_indicator_returns_dict():
    result = fetch_indicator("US", "NY.GDP.MKTP.KD.ZG", 2000, 2005)
    assert isinstance(result, dict)
def test_fetch_indicator_invalid_country():
    result = fetch_indicator("INVALID", "NY.GDP.MKTP.KD.ZG", 2000, 2005)
    assert result == {}
def test_fetch_indicator_no_data_returns_empty():
    # some valid countries have missing data for certain indicators
    result = fetch_indicator("US", "NY.GDP.MKTP.KD.ZG", 2000, 2005)
    assert isinstance(result, dict)

def test_fetch_indicator_years_in_range():
    result = fetch_indicator("US", "NY.GDP.MKTP.KD.ZG", 2000, 2005)
    for year in result:
        assert 2000 <= int(year) <= 2005

def test_fetch_indicator_no_none_values():
    result = fetch_indicator("IN", "NY.GDP.MKTP.KD.ZG", 2010, 2020)
    for value in result.values():
        assert value is not None

def test_fetch_indicator_invalid_country():
    result = fetch_indicator("INVALID", "NY.GDP.MKTP.KD.ZG", 2000, 2005)
    assert result == {}

# ── summarize_data ───────────────────────────────────────────────
def test_summarize_data_basic():
    data = {"2000": 3.0, "2001": 5.0, "2002": 1.0}
    result = summarize_data(data)
    assert result["average"] == 3.0
    assert result["max"] == ("2001", 5.0)
    assert result["min"] == ("2002", 1.0)

def test_summarize_data_single_entry():
    data = {"2000": 4.5}
    result = summarize_data(data)
    assert result["average"] == 4.5

def test_summarize_data_empty_raises():
    with pytest.raises(ValueError):
        summarize_data({})

# ── generate_chart ───────────────────────────────────────────────
def test_generate_chart_creates_file():
    data = {"2000": 3.0, "2001": 5.0, "2002": 2.0}
    generate_chart(data, "Test Country", "Test Indicator")
    assert os.path.exists("chart.png")

def test_generate_chart_empty_data():
    with pytest.raises(Exception):
        generate_chart({}, "Test Country", "Test Indicator")