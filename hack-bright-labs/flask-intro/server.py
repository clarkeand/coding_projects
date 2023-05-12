"""Greeting Flask app."""

from random import choice

from flask import Flask, request, redirect

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

MEANNESS = [
    'You broke!', 'You are a fat ass!', 'WE ALL SPRING FROM APES BUT YOU DID NOT SPRING FAR ENOUGH.']

COMMENT = ['Comp', 'Dis']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html><a href="/hello"> Hi! This is the home page.</a></html>"""



@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" action="/dis">
          What's your name? <input type="text" name="person">
          <br>
            <label for="compliment-select">Select your compliment:</label>
              <select name="compliment" id="compliment-select">
                <option value="awesome">Awesome</option>
                <option value="terrific">Terrific</option>
                <option value="fantastic">Fantastic</option>
                <option value="neato">Neato</option>
                <option value="fantabulous">Fantabulous</option>
                <option value="wowza">Wowza</option>
                <option value="oh-so-not-meh">Oh So Not Meh</option>
                <option value="brilliant">Brilliant</option>
                <option value="ducky">Ducky</option>
                <option value="coolio">Coolio</option>
                <option value="incredible">Incredible</option>
                <option value="wonderful">Wonderful</option>
                <option value="smashing">Smashing</option>
                <option value="lovely">Lovely</option>
              </select>
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    option = choice(COMMENT)

    if option == 'Comp':
      compliment = request.args.get("compliment")
      return f"""
      <!doctype html>
      <html>
        <head>
          <title>A Compliment</title>
        </head>
        <body>
          Hi, {player}! I think you're {compliment}!
        </body>
      </html>
      """
    else:
        return redirect('/dis')

@app.route('/dis')
def haters_be_hating():
    doodoo_head = request.args.get("person")
    # print(f"aaaaaaaaaaaaaaaa  {doodoo_head}")
    
    dis = choice(MEANNESS)

    return f"""
          <!doctype html>
          <html>
            <head>
              <title>A Compliment</title>
            </head>
            <body>
              Psych, {doodoo_head}! {dis}!
            </body>
          </html>
            """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, port=3000, host="0.0.0.0")
