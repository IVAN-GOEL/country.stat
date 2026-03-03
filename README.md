# 🌍 WorldData

> A command-line tool for fetching and visualizing economic, military, and education data from the World Bank API.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Test Status](https://img.shields.io/badge/tests-12%20passing-brightgreen)]()

## 📺 Video Demo

**[Watch the demo here](INSERT YOUR VIDEO URL HERE)**

---

## 🎯 Overview

WorldData is a Python CLI application that transforms raw economic data into actionable insights. Select any of **180+ countries**, choose from **10 economic/military indicators**, specify a **year range**, and get instant data analysis with professional visualizations.

**Key benefit**: Real-time World Bank data without API keys or authentication.

---

## ✨ Features

- 🌏 **180+ Countries** - Full country name support with automatic ISO code conversion
- 📊 **10 Indicators** - GDP, inflation, military spending, education investment, and more
- 🔄 **Live API Data** - Always current, sourced directly from World Bank
- 📈 **Auto-Generated Charts** - Professional line charts saved as PNG
- ✅ **Smart Validation** - Input checking at every step (countries, years, indicators)
- 📉 **Data Summaries** - Average, highest, and lowest year calculations
- 🧪 **12 Unit Tests** - Full test coverage with pytest

---

## 📁 Project Structure

```
project/
├── project.py          # Core logic: fetch, summarize, chart, main
├── inputs.py           # User input handling & country-ISO lookup
├── test_project.py     # pytest unit tests (12 tests)
├── requirements.txt    # Dependencies
└── README.md          # This file
```

---

## 🔧 Files & Functions

### **project.py** - Main Application
| Function | Purpose |
|----------|---------|
| `fetch_indicator(country_code, indicator, start_year, end_year)` | Calls World Bank API, returns year-value pairs |
| `summarize_data(data)` | Calculates average, max year, min year |
| `generate_chart(data, country_name, indicator_name)` | Creates Matplotlib line chart, saves as chart.png |
| `main()` | Orchestrates entire workflow: input → fetch → summarize → visualize |

### **inputs.py** - User Input & Validation
| Function | Purpose |
|----------|---------|
| `countryselect()` | Prompts for country, validates against 180+ names, recursively re-prompts if invalid |
| `inpyear()` | Prompts for year (1950–2026), validates range, recursively re-prompts if invalid |
| `country_code(country)` | Dictionary lookup: country name → ISO alpha-2 code (e.g., "India" → "IN") |

### **test_project.py** - Test Suite
- ✅ 5 tests for `fetch_indicator()` - data retrieval, validation, edge cases
- ✅ 4 tests for `summarize_data()` - statistics, empty data handling
- ✅ 3 tests for `generate_chart()` - file creation, error handling

Run: `pytest test_project.py`

---

## 🚀 Quick Start

### Requirements
```bash
pip install -r requirements.txt
```

**Dependencies:**
- `requests` - HTTP library for API calls
- `matplotlib` - Professional charting library
- `pytest` - Testing framework

### Usage
```bash
python project.py
```

Then follow the prompts:
1. Enter a country name (e.g., "United States", "India", "Japan")
2. Select an indicator (1–10 from the menu)
3. Enter start year and end year (1950–2026)
4. View results + auto-generated chart

---

## 📋 Indicators Available

| # | Indicator | Category |
|---|-----------|----------|
| 1 | GDP Growth (%) | Economic |
| 2 | GDP (Current US$) | Economic |
| 3 | GDP per Capita (US$) | Economic |
| 4 | Inflation Rate (%) | Economic |
| 5 | Unemployment (%) | Economic |
| 6 | Military Expenditure (US$) | Military |
| 7 | Armed Forces Personnel (% labor) | Military |
| 8 | Arms Exports (current US$) | Military |
| 9 | Arms Imports (current US$) | Military |
| 10 | Govt Spending on Education (% GDP) | Education |

---

## 💡 Example Output

```
Enter the full name of the country: India
press 1 for GDP Growth (%)
press 2 for GDP (Current US$)
...
press 10 for Govt Spending on Education (% GDP)
Enter the indicator: 1
enter the start year
2015
enter the end year
2020
India
the ISO/code for India is: IN
fetching requested data !

IN :GDP Growth (%)
Data:
2015 7.6
2016 8.2
2017 7.1
2018 6.5
2019 4.2
2020 -6.6

✅ Chart saved as chart.png
```

---

## 🧪 Testing

Run all tests:
```bash
pytest test_project.py
```

Expected output:
```
test_project.py::test_fetch_indicator_returns_dict PASSED
test_project.py::test_fetch_indicator_invalid_country PASSED
test_project.py::test_fetch_indicator_years_in_range PASSED
test_project.py::test_fetch_indicator_no_none_values PASSED
test_project.py::test_summarize_data_basic PASSED
test_project.py::test_summarize_data_single_entry PASSED
test_project.py::test_summarize_data_empty_raises PASSED
test_project.py::test_generate_chart_creates_file PASSED
test_project.py::test_generate_chart_empty_data PASSED
======================== 9 passed in 0.25s ========================
```

---

## 🎨 Design Decisions

### Modular Architecture
- **Separation of concerns**: Input (inputs.py) → Logic (project.py) → Testing (test_project.py)
- **Easier to test, maintain, and extend**

### Data Structures
- **Dictionaries** for year-value pairs: O(1) lookup, intuitive, Pythonic
- **Automatic null filtering** from API responses ensures clean data

### Input Validation
- **Recursive prompting** instead of while-loops for clean, functional style
- **Whitelist validation** for country names (180+ verified entries)
- **Year range validation** (1950–2026) with logical checks

### API & Visualization Choices
- **World Bank API**: Free, no authentication, always current
- **Matplotlib**: Professional quality, works in CLI environments, easy PNG export
- **Menu system**: Hides cryptic API codes behind human-readable options

---

## 📚 Technologies

| Technology | Purpose |
|-----------|---------|
| **Python 3.7+** | Core language |
| **requests** | HTTP requests to World Bank API |
| **matplotlib** | Data visualization & chart generation |
| **pytest** | Unit testing framework |

---

## 📖 Learn More

- [World Bank API Docs](https://data.worldbank.org/developers)
- [Matplotlib Documentation](https://matplotlib.org/)
- [pytest Documentation](https://docs.pytest.org/)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Made by Ivan Goel**

---

<div align="center">

**[⬆ Back to Top](#-worlddata)**

</div>
