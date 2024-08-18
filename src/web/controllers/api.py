from flask import Blueprint, jsonify, render_template
import requests
import plotly.express as px
import pandas as pd


api_blueprint = Blueprint("api", __name__, url_prefix="/api/")

@api_blueprint.get("reports")
def reports():
    return render_template('reports.html')


@api_blueprint.get("humidity-report")
def humidity_report():
    df = pd.read_csv('/home/santiago/Projects/eco-track-solutions/src/sensors_data.csv')
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    df_filtered = df[df['timestamp'].dt.date == pd.to_datetime("2024-07-08").date()]
    
    humidity_avg = df_filtered.resample('H', on='timestamp')['humedad'].mean().reset_index()
    
    fig = px.line(humidity_avg, x='timestamp', y='humedad', 
                  title='', 
                  labels={'humedad':'Humedad Promedio', 'timestamp':'Hora'})
    
    fig_html = fig.to_html(full_html=False)
    
    return render_template('report.html', 
                           plot_div=fig_html, 
                           report_name = 'Humedad Promedio')


@api_blueprint.get("/temperature-report")
def temperature_report():
    df = pd.read_csv('/home/santiago/Projects/eco-track-solutions/src/sensors_data.csv')
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    df_filtered = df[df['timestamp'].dt.date == pd.to_datetime("2024-07-08").date()]
    
    temperature_avg_per_hour = df_filtered.resample('H', on='timestamp')['temperatura'].mean().reset_index()
    
    fig = px.bar(temperature_avg_per_hour, 
                 x=temperature_avg_per_hour['timestamp'].dt.strftime('%H:%M'), 
                 y='temperatura', 
                 title='',
                 labels={'temperatura':'Temperatura Promedio (°C)', 'timestamp':'Hora'},
                 color='temperatura',  
                 color_continuous_scale='Viridis') 
 
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)', 
        font=dict(size=12),
        xaxis_title='Hora',
        yaxis_title='Temperatura Promedio (°C)',
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1
        )
    )
    
    fig_html = fig.to_html(full_html=False)
    
    return render_template('report.html', 
                           plot_div=fig_html, 
                           report_name='Temperatura Promedio')



@api_blueprint.get("/traffic")
def get_traffic():
    url = "https://idealspot-geodata.p.rapidapi.com/api/v1/traffic/counts/1595369397"
    headers = {
        'x-rapidapi-host': 'idealspot-geodata.p.rapidapi.com',
        'x-rapidapi-key': '47ad8cc699msh958e94e8cb205ffp1522e0jsn9d2bacecf952'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
         data = response.json()['data'][0]
         return render_template('traffic.html', segment=data)
    else:
        return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
