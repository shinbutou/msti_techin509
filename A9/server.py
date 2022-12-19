from flask import Flask, render_template, request, redirect, session
from logic import *
import json

# To access the on-going game
def write_board(a_list):
    with open("board.json", "w") as fp:
        json.dump(a_list, fp)

def write_board_record(a_list):
    with open("board_record.json", "w") as fp:
        json.dump(a_list, fp)

def read_board():
    with open('board.json', 'rb') as fp:
        n_list = json.load(fp)
        return n_list

def read_board_record():
    # for reading also binary mode is important
    with open('board_record.json', 'rb') as fp:
        n_list = json.load(fp)
        return n_list

df = pd.read_csv('./database.csv')

app = Flask(__name__)
app.secret_key = 'TECHIN509'

@app.route("/", methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        session['mode'] = request.form['mode']
        session['player'] = 'X'
        return redirect('/play')
    return render_template("index.html")

@app.route("/play", methods=['GET', 'POST'])
def game():
    game = TicTacToe(session.get('mode'))
    game.board, game.board_slots = read_board(), read_board_record()

    if request.method == 'POST':
        loc = int(request.form['loc']) - 1
        game.board[loc // 3][loc % 3] = session.get('player')
        write_board(game.board)
        game.board_slots.remove(loc + 1)
        write_board_record(game.board_slots)

        result = game.get_winner()

        # TODO: Update who's turn it is.
        if game.mode == '2':
            session['player'] = game.other_player(session['player'])
        elif game.mode == '1' and len(game.board_slots) != 0: # Or ask the computer to finish its turn on a random block
            game.random_move()
            write_board(game.board)
            write_board_record(game.board_slots)

        # Result
        result = game.get_winner()
            
        if result != None:
            df.loc[len(df.index)] = [int(game.mode), result]
            df.to_csv('./database.csv', index=False) # Record the game
            winning_times = df['result'].value_counts().tolist()[df['result'].value_counts().keys().tolist().index(result)]
            winning_rate = str(round(winning_times / len(df) * 100, 2)) # Calculate and display relevant statistics
            write_board([[None, None, None], [None, None, None], [None, None, None]]) # Reset
            write_board_record([1, 2, 3, 4, 5, 6, 7, 8, 9])
            session['result'], session['winning_rate'] = result, winning_rate
            return redirect("/result")

    return render_template("play.html", board=game.board, player=session.get('player'))

@app.route("/result")
def end():
    result = session.get('result')
    if result == 'X' or result == 'O':
        return render_template("result.html", result=result, winning_rate=session.get('winning_rate'))
    elif result == 'D':
        return render_template("result.html", winning_rate=session.get('winning_rate'))

@app.route("/stats")
def display_stats():
    return render_template("stats.html")

@app.errorhandler(400) # Redirecting "Bad Request"
def bad_request(e):
    return redirect("/")


@app.errorhandler(404) # Redirecting undefined URLs
def page_not_found(e):
    return redirect("/")


@app.errorhandler(500) # Redirecting "Internal Server Error"
def internal_server_error(e):
    return redirect("/")

if __name__ == "__main__":
    app.run()