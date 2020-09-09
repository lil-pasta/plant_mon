#!/usr/bin/python3
import atexit, json
from flask import Flask, jsonify
from temphum.temphum import get_temp, get_hum
from vocsen.vocsen import save_base, get_voc, start_sgp
from lightsen.lightsen import get_lux
from moistsen.moistsen import get_moist

"""init stuff"""
sgp = start_sgp()
atexit.register(save_base, sgp)
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/temphum/api/getEnv', methods=['GET'])
def get_env():
    data_sources = {'trl': get_trl,
                    'envVoc': get_envVoc,
                    'lum': get_lum,
                    'moist': get_wet
                    }
    data = {}
    for d in data_sources.values():
        source = d().get_json()
        data.update(source)
    return jsonify({'env_info': data})

@app.route('/temphum/api/wet', methods=['GET'])
def get_wet():
    moisture = get_moist()
    data = {
            'light': {
                'value': moisture,
                'unit': ''
                }
            }
    return jsonify({'moisture_data': data})

@app.route('/temphum/api/voc', methods=['GET'])
def get_envVoc():
    voc_data = get_voc(sgp)
    data = {
            'eCO2': {
                'value': voc_data[0],
                'unit': 'ppm'
                },
            'TVOC': {
                'value': voc_data[1],
                'unit': 'ppb'
                },
            'baseline': {
                'eCO2': voc_data[2],
                'TVOC': voc_data[3]
        }
            }
    return jsonify({'voc_data': data})

@app.route('/temphum/api/temp_relhum', methods=['GET'])
def get_trl():
    temp = get_temp()
    hum = get_hum()
    data = {
            'temperature': {
                'value': temp,
                'unit': 'Deg F'
                },
            'relative_humidity': {
                'value': hum,
                'unit': '%'
                }
            }
    return jsonify({'temphum_data': data})

@app.route('/temphum/api/lux', methods=['GET'])
def get_lum():
    lux = get_lux()
    data = {
            'light': {
                'value': lux,
                'unit': 'lux'
                }
            }
    return jsonify({'light_data': data})

if __name__ == '__main__':
    app.run()
