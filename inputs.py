def countryselect():
    country=input("Enter the full name of the country: ")
    country=country.title().strip()
    world=("Afghanistan, Albania, Algeria, American Samoa, Andorra, Angola,"
           " Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria,"
           " Azerbaijan, Bahamas, The, Bahrain, Bangladesh, Barbados, Belarus, Belgium,"
           " Belize, Benin, Bermuda, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana, "
           "Brazil, British Virgin Islands, Brunei Darussalam, Bulgaria, Burkina Faso,"
           " Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Cayman Islands, "
           "Central African Republic, Chad, Channel Islands, Chile, China, Colombia,"
           " Comoros, Congo, Dem. Rep., Congo, Rep., Costa Rica, Cote d’Ivoire, Croatia,"
           " Cuba, Curacao, Cyprus, Czechia, Denmark, Djibouti, Dominica, Dominican Republic,"
           " Ecuador, Egypt, Arab Rep., El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini,"
           " Ethiopia, Faroe Islands, Fiji, Finland, France, French Polynesia, Gabon, Gambia,"
           " The, Georgia, Germany, Ghana, Gibraltar, Greece, Greenland, Grenada, Guam,"
           " Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Honduras, Hong Kong SAR,"
           " China, Hungary, Iceland, India, Indonesia, Iran, Islamic Rep., Iraq, Ireland,"
           " Isle of Man, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya,"
           " Kiribati, Korea, Dem. People’s Rep., Korea, Rep., Kosovo, Kuwait,"
           " Kyrgyz Republic, Lao PDR, Latvia, Lebanon, Lesotho, Liberia, Libya,"
           " Liechtenstein, Lithuania, Luxembourg, Macao SAR, China, Madagascar,"
           " Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Mauritania, "
           "Mauritius, Mexico, Micronesia, Fed. Sts., Moldova, Monaco, Mongolia, Montenegro,"
           " Morocco, Mozambique, Myanmar, Namibia, Nauru, Nepal, Netherlands, New Caledonia,"
           " New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Northern Mariana Islands, "
           "Norway, Oman, Pakistan, Palau, Panama, Papua New Guinea, Paraguay, Peru, Philippines,"
           " Poland, Portugal, Puerto Rico (US), Qatar, Romania, Russian Federation, Rwanda, Samoa,"
           " San Marino, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone,"
           " Singapore, Sint Maarten (Dutch part), Slovak Republic, Slovenia, Solomon Islands, Somalia,"
           " South Africa, South Sudan, Spain, Sri Lanka, St. Kitts and Nevis, St. Lucia,"
           " St. Martin (French part), St. Vincent and the Grenadines, Sudan, Suriname, Sweden, "
           "Switzerland, Syrian Arab Republic, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo,"
           " Tonga, Trinidad and Tobago, Tunisia, Türkiye, Turkmenistan, Tuvalu, Uganda, Ukraine,"
           " United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Vanuatu,"
           " Venezuela, Rep. Bolivariana de, Viet Nam, Yemen, Rep., Zambia, Zimbabwe")
    world = [c.strip() for c in world.split(",")]
    if country in world:
        return country
    else:
        print("you chose an invalid country")
        return countryselect()

def inpyear ():
    year=int(input())
    if (year>2026 or year<1950):
        print("you chose an invalid year")
        return inpyear()
    else:
        return year



def country_code(country):
    countryISO = {
        "Afghanistan": "AF",
        "Albania": "AL",
        "Algeria": "DZ",
        "American Samoa": "AS",
        "Andorra": "AD",
        "Angola": "AO",
        "Antigua And Barbuda": "AG",
        "Argentina": "AR",
        "Armenia": "AM",
        "Aruba": "AW",
        "Australia": "AU",
        "Austria": "AT",
        "Azerbaijan": "AZ",
        "Bahamas": "BS",
        "Bahrain": "BH",
        "Bangladesh": "BD",
        "Barbados": "BB",
        "Belarus": "BY",
        "Belgium": "BE",
        "Belize": "BZ",
        "Benin": "BJ",
        "Bermuda": "BM",
        "Bhutan": "BT",
        "Bolivia": "BO",
        "Bosnia And Herzegovina": "BA",
        "Botswana": "BW",
        "Brazil": "BR",
        "British Virgin Islands": "VG",
        "Brunei Darussalam": "BN",
        "Bulgaria": "BG",
        "Burkina Faso": "BF",
        "Burundi": "BI",
        "Cabo Verde": "CV",
        "Cambodia": "KH",
        "Cameroon": "CM",
        "Canada": "CA",
        "Cayman Islands": "KY",
        "Central African Republic": "CF",
        "Chad": "TD",
        "Chile": "CL",
        "China": "CN",
        "Colombia": "CO",
        "Comoros": "KM",
        "Congo, Dem. Rep.": "CD",
        "Congo, Rep.": "CG",
        "Costa Rica": "CR",
        "Cote D’Ivoire": "CI",
        "Croatia": "HR",
        "Cuba": "CU",
        "Cyprus": "CY",
        "Czechia": "CZ",
        "Denmark": "DK",
        "Djibouti": "DJ",
        "Dominica": "DM",
        "Dominican Republic": "DO",
        "Ecuador": "EC",
        "Egypt": "EG",
        "El Salvador": "SV",
        "Equatorial Guinea": "GQ",
        "Eritrea": "ER",
        "Estonia": "EE",
        "Eswatini": "SZ",
        "Ethiopia": "ET",
        "Fiji": "FJ",
        "Finland": "FI",
        "France": "FR",
        "Gabon": "GA",
        "Gambia": "GM",
        "Georgia": "GE",
        "Germany": "DE",
        "Ghana": "GH",
        "Greece": "GR",
        "Greenland": "GL",
        "Grenada": "GD",
        "Guam": "GU",
        "Guatemala": "GT",
        "Guinea": "GN",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Haiti": "HT",
        "Honduras": "HN",
        "Hong Kong Sar, China": "HK",
        "Hungary": "HU",
        "Iceland": "IS",
        "India": "IN",
        "Indonesia": "ID",
        "Iran": "IR",
        "Iraq": "IQ",
        "Ireland": "IE",
        "Isle Of Man": "IM",
        "Israel": "IL",
        "Italy": "IT",
        "Jamaica": "JM",
        "Japan": "JP",
        "Jordan": "JO",
        "Kazakhstan": "KZ",
        "Kenya": "KE",
        "Kiribati": "KI",
        "Korea, Rep.": "KR",
        "Korea, Dem. People’s Rep.": "KP",
        "Kosovo": "XK",
        "Kuwait": "KW",
        "Kyrgyz Republic": "KG",
        "Lao Pdr": "LA",
        "Latvia": "LV",
        "Lebanon": "LB",
        "Lesotho": "LS",
        "Liberia": "LR",
        "Libya": "LY",
        "Liechtenstein": "LI",
        "Lithuania": "LT",
        "Luxembourg": "LU",
        "Macao Sar, China": "MO",
        "Madagascar": "MG",
        "Malawi": "MW",
        "Malaysia": "MY",
        "Maldives": "MV",
        "Mali": "ML",
        "Malta": "MT",
        "Marshall Islands": "MH",
        "Mauritania": "MR",
        "Mauritius": "MU",
        "Mexico": "MX",
        "Micronesia, Fed. Sts.": "FM",
        "Moldova": "MD",
        "Monaco": "MC",
        "Mongolia": "MN",
        "Montenegro": "ME",
        "Morocco": "MA",
        "Mozambique": "MZ",
        "Myanmar": "MM",
        "Namibia": "NA",
        "Nauru": "NR",
        "Nepal": "NP",
        "Netherlands": "NL",
        "New Zealand": "NZ",
        "Nicaragua": "NI",
        "Niger": "NE",
        "Nigeria": "NG",
        "North Macedonia": "MK",
        "Norway": "NO",
        "Oman": "OM",
        "Pakistan": "PK",
        "Palau": "PW",
        "Panama": "PA",
        "Papua New Guinea": "PG",
        "Paraguay": "PY",
        "Peru": "PE",
        "Philippines": "PH",
        "Poland": "PL",
        "Portugal": "PT",
        "Puerto Rico": "PR",
        "Qatar": "QA",
        "Romania": "RO",
        "Russian Federation": "RU",
        "Rwanda": "RW",
        "Saudi Arabia": "SA",
        "Senegal": "SN",
        "Serbia": "RS",
        "Seychelles": "SC",
        "Sierra Leone": "SL",
        "Singapore": "SG",
        "Slovak Republic": "SK",
        "Slovenia": "SI",
        "Solomon Islands": "SB",
        "Somalia": "SO",
        "South Africa": "ZA",
        "South Sudan": "SS",
        "Spain": "ES",
        "Sri Lanka": "LK",
        "Sudan": "SD",
        "Suriname": "SR",
        "Sweden": "SE",
        "Switzerland": "CH",
        "Syrian Arab Republic": "SY",
        "Tajikistan": "TJ",
        "Tanzania": "TZ",
        "Thailand": "TH",
        "Timor-Leste": "TL",
        "Togo": "TG",
        "Tonga": "TO",
        "Trinidad And Tobago": "TT",
        "Tunisia": "TN",
        "Türkiye": "TR",
        "Turkmenistan": "TM",
        "Tuvalu": "TV",
        "Uganda": "UG",
        "Ukraine": "UA",
        "United Arab Emirates": "AE",
        "United Kingdom": "GB",
        "United States": "US",
        "Uruguay": "UY",
        "Uzbekistan": "UZ",
        "Vanuatu": "VU",
        "Venezuela": "VE",
        "Viet Nam": "VN",
        "Yemen": "YE",
        "Zambia": "ZM",
        "Zimbabwe": "ZW"
    }
    if country in countryISO:
        return countryISO[country]
