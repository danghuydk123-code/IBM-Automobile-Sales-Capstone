"""Context-only Folium map.
The IBM automobile dataset has no verified latitude/longitude per sale.
This map is NOT a geographic distribution or sales-density map.
"""
import folium

m = folium.Map(location=[39.8283, -98.5795], zoom_start=4, tiles="CartoDB positron")
folium.Marker(
    [39.8283, -98.5795],
    popup="United States context only — dataset has no verified sale coordinates",
    tooltip="National dataset scope",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(m)
m.save("automobile_sales_context_map.html")
print("Saved automobile_sales_context_map.html")
