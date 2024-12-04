import pandas as pd

# Actualizar las listas de datos para incluir más circuitos por era

# Lista extendida de circuitos históricos para cada era
data_atmospheric_era = [
    {"Circuito": "Silverstone", "Piloto": "Juan Manuel Fangio", "Coche": "Alfa Romeo 158", "Tiempo": "1:44.200"},
    {"Circuito": "Monaco", "Piloto": "Stirling Moss", "Coche": "Maserati 250F", "Tiempo": "1:44.300"},
    {"Circuito": "Spa-Francorchamps", "Piloto": "Alberto Ascari", "Coche": "Ferrari 375", "Tiempo": "4:23.200"},
    {"Circuito": "Monza", "Piloto": "Juan Manuel Fangio", "Coche": "Maserati 250F", "Tiempo": "2:50.100"},
    {"Circuito": "Nürburgring", "Piloto": "Stirling Moss", "Coche": "Mercedes W196", "Tiempo": "9:17.400"},
]

data_mixed_era = [
    {"Circuito": "Silverstone", "Piloto": "Ayrton Senna", "Coche": "McLaren MP4/4", "Tiempo": "1:27.460"},
    {"Circuito": "Monaco", "Piloto": "Ayrton Senna", "Coche": "McLaren MP4/4", "Tiempo": "1:26.540"},
    {"Circuito": "Spa-Francorchamps", "Piloto": "Alain Prost", "Coche": "McLaren MP4/2", "Tiempo": "2:01.690"},
    {"Circuito": "Monza", "Piloto": "Nelson Piquet", "Coche": "Brabham BT52", "Tiempo": "1:25.150"},
    {"Circuito": "Brands Hatch", "Piloto": "Niki Lauda", "Coche": "Ferrari 312T", "Tiempo": "1:19.450"},
    {"Circuito": "Zandvoort", "Piloto": "James Hunt", "Coche": "McLaren M23", "Tiempo": "1:19.830"},
]

data_v10_v12_era = [
    {"Circuito": "Silverstone", "Piloto": "Michael Schumacher", "Coche": "Ferrari F2004", "Tiempo": "1:18.739"},
    {"Circuito": "Monaco", "Piloto": "Rubens Barrichello", "Coche": "Ferrari F2004", "Tiempo": "1:14.439"},
    {"Circuito": "Spa-Francorchamps", "Piloto": "Kimi Raikkonen", "Coche": "McLaren MP4-20", "Tiempo": "1:45.108"},
    {"Circuito": "Monza", "Piloto": "Juan Pablo Montoya", "Coche": "Williams FW26", "Tiempo": "1:19.525"},
    {"Circuito": "Imola", "Piloto": "Michael Schumacher", "Coche": "Ferrari F2004", "Tiempo": "1:20.411"},
    {"Circuito": "Indianapolis", "Piloto": "Rubens Barrichello", "Coche": "Ferrari F2004", "Tiempo": "1:10.399"},
]

data_v8_era = [
    {"Circuito": "Silverstone", "Piloto": "Sebastian Vettel", "Coche": "Red Bull RB9", "Tiempo": "1:29.607"},
    {"Circuito": "Monaco", "Piloto": "Mark Webber", "Coche": "Red Bull RB6", "Tiempo": "1:14.820"},
    {"Circuito": "Spa-Francorchamps", "Piloto": "Lewis Hamilton", "Coche": "McLaren MP4-27", "Tiempo": "1:47.893"},
    {"Circuito": "Monza", "Piloto": "Fernando Alonso", "Coche": "Ferrari F2012", "Tiempo": "1:24.178"},
    {"Circuito": "Yas Marina", "Piloto": "Sebastian Vettel", "Coche": "Red Bull RB9", "Tiempo": "1:40.696"},
    {"Circuito": "Shanghai", "Piloto": "Nico Rosberg", "Coche": "Mercedes W03", "Tiempo": "1:35.256"},
]

data_hybrid_era = [
    {"Circuito": "Silverstone", "Piloto": "Lewis Hamilton", "Coche": "Mercedes W11", "Tiempo": "1:24.303"},
    {"Circuito": "Monza", "Piloto": "Lewis Hamilton", "Coche": "Mercedes W11", "Tiempo": "1:18.887"},
    {"Circuito": "Suzuka", "Piloto": "Valtteri Bottas", "Coche": "Mercedes W10", "Tiempo": "1:27.064"},
    {"Circuito": "Spa-Francorchamps", "Piloto": "Lewis Hamilton", "Coche": "Mercedes W11", "Tiempo": "1:41.252"},
    {"Circuito": "Interlagos", "Piloto": "Max Verstappen", "Coche": "Red Bull RB15", "Tiempo": "1:10.620"},
    {"Circuito": "Baku", "Piloto": "Charles Leclerc", "Coche": "Ferrari SF21", "Tiempo": "1:41.218"},
]

# Actualizar DataFrames
df_atmospheric_era = pd.DataFrame(data_atmospheric_era)
df_mixed_era = pd.DataFrame(data_mixed_era)
df_v10_v12_era = pd.DataFrame(data_v10_v12_era)
df_v8_era = pd.DataFrame(data_v8_era)
df_hybrid_era = pd.DataFrame(data_hybrid_era)

# Guardar CSVs
paths = {
    "Atmospheric": "./php/motores_atmosfericos.csv",
    "Mixed": "./php/aspiracion_mixta.csv",
    "V10_V12": "./php/motores_v10_y_v12.csv",
    "V8": "./php/motores_v8.csv",
    "Hybrid": "./php/motores_hibridos.csv",
}

df_atmospheric_era.to_csv(paths["Atmospheric"], index=False)
df_mixed_era.to_csv(paths["Mixed"], index=False)
df_v10_v12_era.to_csv(paths["V10_V12"], index=False)
df_v8_era.to_csv(paths["V8"], index=False)
df_hybrid_era.to_csv(paths["Hybrid"], index=False)

paths
