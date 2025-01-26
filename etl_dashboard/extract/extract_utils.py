import pymysql

def fetch_from_mysql(query, db_config):
    """MySQL에서 데이터를 가져오는 함수"""
    connection = pymysql.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    finally:
        connection.close()

import gspread

def fetch_from_google_sheets(sheet_id, sheet_name, credentials_path):
    """Google Sheets에서 데이터를 가져오는 함수"""
    gc = gspread.service_account(filename=credentials_path)
    sheet = gc.open_by_key(sheet_id).worksheet(sheet_name)
    return sheet.get_all_records()

import requests

def fetch_from_api(url, params=None, headers=None):
    """API에서 데이터를 가져오는 함수"""
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API 요청 오류: {e}")
        return None

from google.cloud import bigquery

def fetch_from_bigquery(query, project_id, credentials_path):
    """BigQuery에서 데이터를 가져오는 함수"""
    client = bigquery.Client.from_service_account_json(credentials_path)
    query_job = client.query(query)
    return [row for row in query_job.result()]

