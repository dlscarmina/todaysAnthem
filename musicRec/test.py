import os

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


from recommender.api import Recommender

@app.route('/rec/<genre>/<danceability>/<energy>/<tempo>/<valence>')
def rec(genre, danceability, energy, tempo, valence):
    recommender = Recommender()
    #recommender.artists = 'Green Day'
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
    output = ""
    for recommendation in recommendations['tracks']:
        output += ("%s - %s\n" % (recommendation['name'], recommendation['artists'][0]['name']))
        output += ("URL: %s\n\n" % (recommendation['external_urls'])['spotify'] )    
    return output

@app.route('/form', methods = ['POST'])
def songRecommender():
    if request.method == 'POST':
        mygenre = request.form['genre']
        mydance = request.form['dance'],
        myenergy = request.form['energy'],
        mytempo = request.form['tempo'],
        myvalence = request.form['valence']

        return redirect(url_for('rec', genre = mygenre, danceability = mydance, energy = myenergy, tempo = mytempo, valence = myvalence))

if __name__ == '__main__':
    app.run()
