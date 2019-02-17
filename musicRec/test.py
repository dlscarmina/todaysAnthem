import os

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


from recommender.api import Recommender

@app.route('/rec/<genre>/<danceability>/<energy>/<tempo>/<valence>')
def rec(genre, danceability, energy, tempo, valence):
    recommender = Recommender()
    recommender.genres = [
                genre
    ]
    recommender.track_attributes = {
                'danceability': danceability,
                'energy': energy,
                'tempo': tempo,
                'valence': valence
                }
    
    recommendations = recommender.find_recommendations()
    output = []

    for recommendation in recommendations['tracks']:
        output.append({
            'song' : recommendation['name'],
            'artist' : recommendation['artists'][0]['name'],
            'url' : (recommendation['external_urls'])['spotify']
            }) 
    return render_template('anthem.html', recs = output)

@app.route('/form', methods = ['POST'])
def songRecommender():
    if request.method == 'POST':
        mygenre = request.form['genre']
        mydance = request.form['dance'],
        myenergy = request.form['energy'],
        mytempo = request.form['tempo'],
        myvalence = request.form['valence']

        return redirect(url_for('rec', genre = mygenre, danceability = mydance, energy = myenergy, tempo = mytempo, valence = myvalence))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
