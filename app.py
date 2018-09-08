from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/pokemon/<int:poke_id>', methods=['GET'])
def get_pokemon_name(poke_id):
    root = 'https://www.pokeapi.co/api/v2/pokemon/'
    r = requests.get(root + str(poke_id))
    resp = r.json()
    return 'The pokemon with id {} is {}'.format(poke_id, resp['name'])

@app.route('/pokemon/<string:poke_name>', methods=['GET'])
def get_pokemon_id(poke_name):
    root = 'https://www.pokeapi.co/api/v2/pokemon/'
    r = requests.get(root + poke_name)
    resp = r.json()
    return '{} has id {}'.format(poke_name, resp['id'])

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
