"""IBM DV0101EN – Automobile Sales Statistics Dashboard.
Install: pip install dash pandas plotly
Run: python code/Part2_Automobile_Sales_Dashboard.py
Open: http://127.0.0.1:8050
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
data = pd.read_csv(DATA_URL)
app = Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"
years = sorted(data["Year"].dropna().unique())

app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard"),
    html.Label("Select Statistics:"),
    dcc.Dropdown(id="dropdown-statistics", options=[
        {"label": "Yearly Statistics", "value": "Yearly Statistics"},
        {"label": "Recession Period Statistics", "value": "Recession Period Statistics"}
    ], placeholder="Select a report type"),
    html.Label("Select Year:"),
    dcc.Dropdown(id="select-year",
                 options=[{"label": int(y), "value": int(y)} for y in years],
                 placeholder="Select a year"),
    html.Div(id="output-container")
])

@app.callback(Output("select-year", "disabled"), Input("dropdown-statistics", "value"))
def update_input_container(selected_statistics):
    return selected_statistics != "Yearly Statistics"

@app.callback(Output("output-container", "children"),
              [Input("dropdown-statistics", "value"), Input("select-year", "value")])
def update_output_container(selected_statistics, selected_year):
    if selected_statistics == "Recession Period Statistics":
        rec = data[data["Recession"] == 1]
        yearly = rec.groupby("Year", as_index=False)["Automobile_Sales"].mean()
        vehicle = rec.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"].mean()
        ads = rec.groupby("Vehicle_Type", as_index=False)["Advertising_Expenditure"].sum()
        unemployment = rec.groupby(["Vehicle_Type", "unemployment_rate"], as_index=False)["Automobile_Sales"].mean()
        charts = [
            dcc.Graph(figure=px.line(yearly, x="Year", y="Automobile_Sales", title="Average Sales During Recession")),
            dcc.Graph(figure=px.bar(vehicle, x="Vehicle_Type", y="Automobile_Sales", title="Sales by Vehicle Type")),
            dcc.Graph(figure=px.pie(ads, names="Vehicle_Type", values="Advertising_Expenditure", title="Advertising Share")),
            dcc.Graph(figure=px.bar(unemployment, x="Vehicle_Type", y="Automobile_Sales", color="unemployment_rate",
                                     title="Unemployment and Sales"))
        ]
        return html.Div(charts, style={"display":"grid","gridTemplateColumns":"1fr 1fr","gap":"18px"})
    if selected_statistics == "Yearly Statistics" and selected_year is not None:
        year_data = data[data["Year"] == selected_year]
        yearly = data.groupby("Year", as_index=False)["Automobile_Sales"].mean()
        monthly = year_data.groupby("Month", as_index=False)["Automobile_Sales"].sum()
        vehicle = year_data.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"].mean()
        ads = year_data.groupby("Vehicle_Type", as_index=False)["Advertising_Expenditure"].sum()
        charts = [
            dcc.Graph(figure=px.line(yearly, x="Year", y="Automobile_Sales", title="Yearly Sales")),
            dcc.Graph(figure=px.line(monthly, x="Month", y="Automobile_Sales", title=f"Monthly Sales in {selected_year}")),
            dcc.Graph(figure=px.bar(vehicle, x="Vehicle_Type", y="Automobile_Sales", title="Sales by Vehicle Type")),
            dcc.Graph(figure=px.pie(ads, names="Vehicle_Type", values="Advertising_Expenditure", title="Advertising by Type"))
        ]
        return html.Div(charts, style={"display":"grid","gridTemplateColumns":"1fr 1fr","gap":"18px"})
    return html.Div("Select a report; for Yearly Statistics, also select a year.")

if __name__ == "__main__":
    app.run(debug=True)
