from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
    # localhost:5000/say/flask - have it say "Hi Flask!"
    # localhost:5000/say/michael - have it say "Hi Michael!"
    # localhost:5000/say/john - have it say "Hi John!"

@app.route('/say/<string:word>')
def say_flask(word):
    return 'Hi '+word+'!'
    
# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):

    # localhost:5000/repeat/35/hello - have it say "hello" 35 times
    # localhost:5000/repeat/80/bye - have it say "bye" 80 times
    # localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

@app.route('/repeat/<int:num>/<string:word>')
def repeating(num,word):
    repeat_words=''
    for i in range(0,num):
        repeat_words += f"<p>{word}</p>"
    return repeat_words

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



