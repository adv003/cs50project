from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////movie.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(255), nullable=False)
    lead_actors = db.Column(db.String(255), nullable=False)
    genres = db.Column(db.String(255), nullable=False)
    plot_summary = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    title = request.form['title']
    release_year = request.form['release_year']
    director = request.form['director']
    lead_actors = request.form['lead_actors']
    genres = request.form['genres']
    query = Movie.query
    if title:
        query = query.filter(Movie.title.like('%' + title + '%'))
    if release_year:
        query = query.filter(Movie.release_year == release_year)
    if director:
        query = query.filter(Movie.director.like('%' + director + '%'))
    if lead_actors:
        query = query.filter(Movie.lead_actors.like('%' + lead_actors + '%'))
    if genres:
        query = query.filter(Movie.genres.like('%' + genres + '%'))
    movies = query.all()
    return render_template('search_results.html', movies=movies)
