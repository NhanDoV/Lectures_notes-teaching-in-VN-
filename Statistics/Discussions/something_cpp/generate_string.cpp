#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

class TopicGuessingGame {
private:
    unordered_map<string, vector<string>> topics;

public:
    /**
     * Constructor to initialize the topics and their respective names.
     * 
     * Initializes predefined topics and a list of objects under each topic.
     * The topics include:
     * - Animal
     * - Fruit
     * - Vehicle
     * - Plant
     * - Operator Names
     * - Solar System Names
     */
    TopicGuessingGame() {
        // Initialize the topics with sample data for each category (animal, fruit, etc.)
        topics["animal"] = {
            "elephant", "dog", "cat", "lion", "tiger", "giraffe", "whale", "zebra", "horse", "kangaroo",
            "rabbit", "panda", "monkey", "koala", "deer", "bear", "wolf", "fox", "hippopotamus", "rhino",
            "crocodile", "alligator", "camel", "cheetah", "leopard", "penguin", "flamingo", "ostrich", "gorilla",
            "chimpanzee", "koala", "lemur", "bison", "buffalo", "yak", "moose", "seal", "walrus", "otter",
            "whale", "dolphin", "shark", "jellyfish", "octopus", "squid", "starfish", "sea turtle", "snail",
            "bat", "squirrel", "raccoon", "skunk", "ferret", "badger", "hedgehog", "armadillo", "beaver",
            "porcupine", "mouse", "rat", "gerbil", "hamster", "guinea pig", "parrot", "eagle", "hawk",
            "owl", "falcon", "vulture", "turkey", "chicken", "duck", "goose", "peacock", "pigeon", "crow",
            "sparrow", "cardinal", "woodpecker", "canary", "robin", "swallow", "stork", "bat", "firefly", "moth",
            "butterfly", "beetle", "dragonfly", "ant", "termite", "cockroach", "ladybug", "tick", "bee", "wasp"
        };

        topics["fruit"] = {
            "apple", "banana", "orange", "grape", "mango", "pineapple", "watermelon", "blueberry", "strawberry",
            "blackberry", "raspberry", "cherry", "peach", "plum", "apricot", "nectarine", "kiwi", "papaya",
            "lychee", "pomegranate", "fig", "pear", "cantaloupe", "honeydew", "lime", "lemon", "grapefruit",
            "coconut", "dragon fruit", "passion fruit", "tangerine", "jackfruit", "sapodilla", "starfruit",
            "persimmon", "avocado", "date", "cranberry", "goji berry", "elderberry", "mulberry", "lingonberry",
            "guava", "kumquat", "longan", "soursop", "carambola", "miracle fruit", "black currant", "white currant",
            "currant", "fruit cocktail", "raspberry", "tamarind", "medlar", "quince", "prickly pear", "rose apple",
            "breadfruit", "marula", "pomelo", "pomelo", "mangosteen", "breadfruit", "soursop", "acai berry",
            "fig", "clementine", "cocoa", "olive", "pluot", "pawpaw", "chayote", "jambul", "salak", "loquat",
            "genip", "sweat pea", "citrus", "sugar apple", "carambola", "bael fruit", "bell pepper", "grape fruit"
        };

        topics["vehicle"] = {
            "car", "bus", "train", "airplane", "bicycle", "motorcycle", "boat", "ship", "submarine", "helicopter",
            "truck", "van", "scooter", "skateboard", "rollerblades", "tractor", "bulldozer", "forklift", "trolley",
            "rickshaw", "cart", "tricycle", "snowmobile", "jet ski", "hot air balloon", "zeppelin", "spacecraft",
            "rocket", "space shuttle", "ferry", "yacht", "cruise ship", "cargo plane", "passenger plane", "glider",
            "blimp", "hovercraft", "ambulance", "fire truck", "police car", "taxi", "limousine", "tow truck",
            "ice cream truck", "ambulance", "garbage truck", "streetcar", "monorail", "high-speed train", "tram",
            "cable car", "funicular", "motorboat", "rowboat", "kayak", "canoe", "paddle boat", "fishing boat",
            "jet boat", "speedboat", "cargo ship", "cruise liner", "container ship", "luxury yacht", "fishing vessel",
            "electric car", "hybrid car", "sports car", "minivan", "compact car", "sedan", "convertible", "coupe",
            "muscle car", "electric scooter", "dune buggy", "snowcat", "caravan", "camping trailer", "mobile home",
            "buggy", "golf cart", "hoverboard", "electric skateboard", "chopper", "dirt bike", "cross bike", "moped"
        };

        topics["plant"] = {
            "rose", "tulip", "sunflower", "lily", "orchid", "daisy", "cactus", "palm", "bamboo", "ferns", "poinsettia",
            "violet", "marigold", "petunia", "daffodil", "cherry blossom", "lavender", "jasmine", "begonia",
            "geranium", "cineraria", "azalea", "honeysuckle", "dandelion", "holly", "heather", "iris", "lotus",
            "gardenia", "amaryllis", "hydrangea", "fuchsia", "snowdrop", "rhododendron", "camellia", "aloe vera",
            "ivy", "basil", "rosemary", "thyme", "oregano", "mint", "chives", "sage", "parsley", "cilantro",
            "bay leaf", "oregano", "dill", "tarragon", "lemon balm", "lavender", "chamomile", "lemongrass",
            "marjoram", "curry plant", "gerbera", "columbine", "zinnia", "petunia", "poppy", "jasmine", "forsythia",
            "bellflower", "fuchsia", "bougainvillea", "lilac", "camellia", "cherry laurel", "hosta", "fern", "mint",
            "ginger", "turmeric", "galangal", "parsnip", "carrot", "radish", "beetroot", "turnip", "artichoke",
            "asparagus", "onion", "lettuce", "spinach", "cucumber", "tomato", "aubergine", "pumpkin", "squash",
            "sweet potato", "leek", "broccoli", "cauliflower", "celery", "brussels sprout", "kale", "spinach",
            "chard", "potato", "pumpkin", "garlic", "chili pepper", "bean", "pea", "chickpea", "lentil", "soybean",
            "corn", "maize", "quinoa", "wheat", "barley", "rye", "rice", "sorghum", "buckwheat", "chia", "flax",
            "sunflower", "sesame", "hemp", "cotton", "bamboo", "cottonwood", "willow", "oak", "maple", "pine", "cedar",
            "fir", "spruce", "cypress", "redwood", "sequoia", "juniper", "ash", "cherry", "apple", "pear", "plum",
            "peach", "grape", "blackberry", "blueberry", "elderberry", "raspberry", "mulberry", "fig", "apricot",
            "pomegranate", "persimmon", "kiwi", "papaya", "coconut", "melon", "watermelon", "fruiting tree"
        };
    }

    // Function to generate a random number between min and max (inclusive)
    int getRandomNumber(int min, int max) {
        return rand() % (max - min + 1) + min;
    }

    // Function to play the guessing game
    void playGame() {
        srand(time(0));  // Seed the random number generator

        // Randomly select a topic from the available list
        vector<string> topicsList = {"animal", "fruit", "vehicle", "plant"};
        string topic = topicsList[getRandomNumber(0, topicsList.size() - 1)];

        // Randomly select an object from the chosen topic
        vector<string> objects = topics[topic];
        string secretObject = objects[getRandomNumber(0, objects.size() - 1)];

        // Welcome message
        cout << "Welcome to the Topic Guessing Game!" << endl;
        cout << "I have selected a random object from the category: " << topic << endl;
        cout << "Try to guess the name of the object!" << endl;

        string userGuess;  // Variable to store user's guess
        bool correctGuess = false;  // Flag to indicate whether the user has guessed correctly

        // Main loop for guessing
        while (!correctGuess) {
            cout << "Enter your guess (or type 'exit' to quit): ";
            getline(cin, userGuess);  // Use getline to read full input

            // Handle exit condition
            if (userGuess == "exit") {
                cout << "Thanks for playing! The correct answer was: " << secretObject << endl;
                break;  // Exit the game
            }

            // Trim spaces and convert to lowercase for comparison
            userGuess = trim(userGuess);
            transform(userGuess.begin(), userGuess.end(), userGuess.begin(), ::tolower);

            // Handle clue requests
            if (userGuess == "need a clue" || userGuess == "need a support") {
                cout << "Clue: The first letter of the object is: " << secretObject[0] << endl;
                continue;  // Go to the next iteration to let the user continue guessing
            }

            // Provide additional help on request (another clue)
            if (userGuess == "another help") {
                cout << "Another clue: The last letter of the object is: " << secretObject[secretObject.size() - 1] << endl;
                continue;  // Go to the next iteration to continue guessing
            }

            // Check if the guess is correct
            if (userGuess == secretObject) {
                correctGuess = true;  // Correct guess, exit the loop
                cout << "Congratulations! You've guessed the correct object: " << secretObject << endl;
            } else {
                cout << "Wrong guess, try again!" << endl;
            }
        }
    }

private:
    // Function to trim leading and trailing spaces from a string
    string trim(const string &str) {
        size_t first = str.find_first_not_of(" \t\n\r");
        size_t last = str.find_last_not_of(" \t\n\r");
        return (first == string::npos || last == string::npos) ? "" : str.substr(first, last - first + 1);
    }
};

int main() {
    // Create a game instance and start the game
    TopicGuessingGame game;
    game.playGame();
    return 0;
}