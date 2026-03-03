#imports and libraries
from inputs import countryselect
from inputs import country_code
from inputs import inpyear
import sys
import requests
import matplotlib.pyplot as plt

#generating chart
def generate_chart(data, country_name, indicator_name):
    years = sorted(data.keys())
    values = [data[year] for year in years]
    plt.figure(figsize=(12, 6))
    plt.plot(years, values, marker="o", linewidth=2, color="blue", markersize=4)
    plt.title(f"{country_name} — {indicator_name}", fontsize=14, fontweight="bold")
    plt.xlabel("Year")
    plt.ylabel(indicator_name)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()
    print("\n✅ Chart saved as chart.png")

#averaging the data
def summarize_data(data):
    values = [v for v in data.values() if v is not None]
    if not values:
        raise ValueError("No data to summarize")
    avg = sum(values) / len(values)
    max_year = max(data, key=lambda y: data[y])
    min_year = min(data, key=lambda y: data[y])
    return {
        "average": round(avg, 2),
        "max": (max_year, round(data[max_year], 2)),
        "min": (min_year, round(data[min_year], 2))
    }

#indicators
INDICATORS = {
    "1": ("GDP Growth (%)", "NY.GDP.MKTP.KD.ZG"),
    "2": ("GDP (Current US$)", "NY.GDP.MKTP.CD"),
    "3": ("GDP per Capita (US$)", "NY.GDP.PCAP.CD"),
    "4": ("Inflation Rate (%)", "FP.CPI.TOTL.ZG"),
    "5": ("Unemployment (%)", "SL.UEM.TOTL.ZS"),
    "7": ("Military Expenditure (US$)", "MS.MIL.XPND.CD"),
    "8": ("Armed Forces Personnel (% labor)", "SL.MIL.TOTL.ZS"),
    "9": ("Arms Exports (current US$)", "MS.MIL.XPRT.KD"),
    "10": ("Arms Imports (current US$)", "MS.MIL.MPRT.KD"),
    "11": ("Govt Spending on Education (% GDP)", "SE.XPD.TOTL.GD.ZS")
}

#request response
def fetch_indicator(country_code, indicator, start_year, end_year):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    data = response.json()
    if data[1] is None:
        return {}
    result = {}
    for entry in data[1]:
        year = entry["date"]
        value = entry["value"]
        if value is not None:
            result[year] = value

    return result


def main():
    nation=countryselect()
    #getting user input for the data they require
    for _ in INDICATORS.keys():
        print(f"press {_} for {INDICATORS[_][0]}")

    userindicator =(input("Enter the indicator: "))
    if int(userindicator)>11 or int(userindicator)<1:
        sys.exit("invalid indicator")
    indicator = INDICATORS[userindicator][1]
    print("enter the start year")
    STyear=inpyear()
    print("enter the end year")
    ENyear=inpyear()
    if STyear == ENyear or STyear > ENyear:
        sys.exit("INVALID year combination!!")

    print(nation)
    nationISO=country_code(nation)
    print(f"the ISO/code for {nation} is: {nationISO}")
    print("fetching requested data !")
    print(f"\n{nationISO} :{INDICATORS[userindicator][0]}")
    data=fetch_indicator(nationISO, indicator,STyear,ENyear)
    print("\nData:")
    for year, value in sorted(data.items()):
        print(year, value)
    generate_chart(data, nation, INDICATORS[userindicator][0])


if __name__ == "__main__":
    main()
