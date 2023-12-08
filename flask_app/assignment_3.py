from model.smart_devices import Home
from model.smart_devices import SmartDevice
from model.smart_devices import LightBulb
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    home = Home("1 Hacker Way")
    try:
        with open('light.json', 'r') as file:
            light_bulb_data = json.load(file)
            for LB in light_bulb_data:
                light_bulb = LightBulb(LB['name'], LB['manufacturer'], LB['brightness'])
                home.add_device(light_bulb)
    except FileNotFoundError:
        pass
    return render_template('home.html', home=home)

@app.route('/add_lightbulb', methods=['POST'])
def add_lightbulb():
    data = request.json
    name = data.get('name')
    manufacturer = data.get('manufacturer')
    brightness = data.get('brightness')
    if name and manufacturer and brightness is not None:
        light_bulb = LightBulb(name, manufacturer, brightness)
        new_light_bulb_json = light_bulb.to_json()
        try:
             with open('light.json' , 'r') as file:
                light_bulbs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            light_bulbs = []
        light_bulbs.append(json.loads(new_light_bulb_json))
        
        with open('light.json', 'w') as file:
            json.dump(light_bulbs, file)

        return jsonify({"message": "LightBulb added successfully!"}), 201
    else:
        return jsonify({"error": "There was a problem, data missing."}), 400

if __name__ == '__main__':
    app.run(debug=True)
