from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize the game state
random_number = random.randint(1, 100)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def game():
    global random_number, attempts

    message = ''
    if request.method == 'POST':
        guess = request.form.get('guess')
        if guess:
            guess = int(guess)
            attempts += 1

            if guess < random_number:
                message = f"❌ You gussed {guess} that is too low! Try again."
            elif guess > random_number:
                message = f"❌ You gussed {guess} that is too high! Try again."
            else:
                message = f"🎉Congratulations🎉! You guessed the correct number {random_number} in {attempts} attempts 🎯."
                random_number = random.randint(1, 100)  # Reset the game
                attempts = 0

    return render_template('game.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
