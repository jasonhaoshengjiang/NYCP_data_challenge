import requests
import pandas as pd
import geopandas as gpd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import contextily as ctx
import os

def get_data(agency):
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    query_params = {
        "$limit": 50000,
        "$where": "created_date >= '{}' and agency = '{}'".format(
            (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S'), agency)
    }
    response = requests.get(url, params=query_params)
    df = pd.read_json(response.text)
    df_2 = pd.read_json(response.text)
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_csv("data/raw.csv", index=False)
    df['created_date'] = pd.to_datetime(df['created_date'])
    df['created_date_hour'] = df['created_date'].dt.floor('h')
    df['complaint_type'] = df['complaint_type'].str.strip()
    df_2['created_date'] = pd.to_datetime(df_2['created_date'])
    df_2['complaint_type'] = df_2['complaint_type'].str.strip()
    ts_df = df.groupby(['created_date_hour', 'complaint_type']).size().reset_index(name='count')
    ts_df.to_csv("data/time_series.csv", index=False)
    ts_df['created_date_hour'] = pd.to_datetime(ts_df['created_date_hour'])
    pivot_df = ts_df.pivot(index='created_date_hour', columns='complaint_type', values='count')
    return pivot_df, df_2

def main():
    agency = input("Enter agency value: ")

    df, df_raw = get_data(agency)

    plt.figure(figsize=(10, 6))
    plt.title("Total Service Requests by Complaint Type and Created Date/Hour")
    plt.xlabel("Created Date/Hour")
    plt.ylabel("Total Service Requests")
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

    plt.savefig("data/service_requests.png")

    complaint_type = input("Enter complaint_type value: ")

    url = "https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=GeoJSON"

    response = requests.get(url)

    with open("data/nta.geojson", "wb") as f:
        f.write(response.content)

    nta_gdf = gpd.read_file("data/nta.geojson")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    filtered_df = df_raw[
        (df_raw['complaint_type'] == complaint_type) &
        (df_raw['created_date'] >= start_date) &
        (df_raw['created_date'] <= end_date)
    ]

    filtered_gdf = gpd.GeoDataFrame(
        filtered_df, geometry=gpd.points_from_xy(filtered_df.longitude, filtered_df.latitude)
    )
    
    filtered_gdf.crs = "EPSG:4326"

    merged_gdf = gpd.sjoin(nta_gdf, filtered_gdf, how='left')

    incident_counts = merged_gdf.groupby('ntacode').size().reset_index(name='count')

    nta_with_counts = nta_gdf.merge(incident_counts, on='ntacode', how='left').fillna(0)

    nta_with_counts_web_mercator = nta_with_counts.to_crs(epsg=3857)

    fig, ax = plt.subplots(1, figsize=(12, 12))
    ax.set_aspect('equal')
    nta_with_counts_web_mercator.plot(column='count', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    
    ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite, zoom=10)

    ax.axis('off')
    
    ax.set_title('7-day total count of {} by NTA'.format(complaint_type), fontdict={'fontsize': '20', 'fontweight': '3'})

    plt.savefig("data/nta_with_counts_web_mercator.png")


if __name__ == "__main__":
    main()

