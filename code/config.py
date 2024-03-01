class config():
    NEWS_API_URL = "https://mboum-finance.p.rapidapi.com/v1/markets/news"
    HISTORY_API_URL = "https://mboum-finance.p.rapidapi.com/hi/history"
    API_Key = '16b6588570msh97735c663173c8dp1179e0jsnac0844091cb9'
    RapidAPI_Host = 'mboum-finance.p.rapidapi.com'

    headers = {
        "X-RapidAPI-Key": API_Key,
        "X-RapidAPI-Host": RapidAPI_Host
    }
