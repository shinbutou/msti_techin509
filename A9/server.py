from flask import Flask, render_template, request, redirect, url_for
import logic

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        return redirect('/game')
    return render_template("index.html")

@app.route('/game', methods=['GET', 'POST'])
def play():
    board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    if request.method == 'POST':
        return render_template("play.html", board=board)
    return render_template("play.html")

@app.route("/stats")
def display_stats():
    return render_template("stats.html")

if __name__ == "__main__":
    app.run()