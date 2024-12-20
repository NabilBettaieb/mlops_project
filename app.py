import Flask as fl
import requests

fl.title("Prédiction")

features = fl.text_input("Entrez les caractéristiques ")


if fl.button("Prediction"):
    data = {"features": [float(x) for x in features.split(",")]}
    response = requests.post("http://localhost:5000/predict", json=data)
    if response.status_code == 200:
        st.write("Prédiction :", response.json()['prediction'])
    else:
        st.write("Erreur :", response.status_code)
