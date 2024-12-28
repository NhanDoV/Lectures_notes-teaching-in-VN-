#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class GuessANumberGame {
private:
    int secretNumber;  // The secret number that the player needs to guess
    int minRange;      // Minimum range for the number
    int maxRange;      // Maximum range for the number

public:
    // Constructor to initialize the secret number and the range
    GuessANumberGame(int min, int max) {
        minRange = min;
        maxRange = max;
        secretNumber = rand() % (max - min + 1) + min;  // Generate a random secret number within the range
    }

    // Function to generate a random hint number for each turn
    string getHint(int guess) {
        /*
        Returns a hint based on the user's guess.
        If the guess is smaller than the secret number, it will say "greater".
        If the guess is greater than the secret number, it will say "smaller".
        If the guess is correct, it will return an empty string.
        */
        if (guess < secretNumber) {
            return "greater";  // The secret number is greater than the guess
        } else if (guess > secretNumber) {
            return "smaller";  // The secret number is smaller than the guess
        } else {
            return "";  // The guess is correct, no hint needed
        }
    }

    // Function to start the Guess-a-Number game
    void playGame() {
        /*
        Starts the game and continuously prompts the user to guess the secret number.
        The game gives a "greater" or "smaller" hint on each guess based on the secret number.
        The game ends when the user guesses the correct number.
        */

        int guess;
        int attempts = 0;
        bool isGuessedCorrectly = false;

        cout << "Welcome to the Guess-a-Number Game!" << endl;
        cout << "I'm thinking of a number between " << minRange << " and " << maxRange << "." << endl;

        // Main game loop
        while (!isGuessedCorrectly) {
            cout << "Enter your guess: ";
            cin >> guess;
            attempts++;

            // Get the hint for the current guess
            string hint = getHint(guess);

            if (hint == "") {
                // If no hint, the guess is correct
                cout << "Congratulations! You guessed the correct number in " << attempts << " attempts!" << endl;
                isGuessedCorrectly = true;
            } else {
                // Provide a hint based on the user's guess
                cout << "The secret number is " << hint << " than your guess. Try again!" << endl;
            }
        }
    }
};

int main() {
    // Initialize the random number generator
    srand(static_cast<unsigned int>(time(0))); 

    // Create a game instance with a range from 1 to 100
    GuessANumberGame game(1, 100);
    game.playGame();  // Start the game

    return 0;
}