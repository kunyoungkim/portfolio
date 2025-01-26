# extract_ga4.py
from google.analytics.data import BetaAnalyticsDataClient

def extract_ga4_data(property_id, start_date, end_date):
    client = BetaAnalyticsDataClient()
    request = {
        "property": f"properties/{property_id}",
        "date_ranges": [{"start_date": start_date, "end_date": end_date}],
        "dimensions": [{"name": "sessionSource"}],
        "metrics": [{"name": "activeUsers"}],
    }
    response = client.run_report(request)
    return response.rows

