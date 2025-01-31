#include <iostream>  // Allows input/output functionality
#include <vector>    // Enables the use of the vector container (dynamic array)
#include <cstdlib>   // Contains functions for random number generation and conversion
#include <ctime>     // Allows working with time (used for seeding random function)
#include <unordered_map>  // Provides the unordered_map container (hash table)
#include <string>    // Enables the use of the string data type
#include <algorithm> // Contains common algorithms like sort(), find(), etc.

// This line allows us to use components in the std namespace without needing to write 'std::'
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
	 * - Colors
	 * - Vehicle
	 * - Plant
	 * - Operator Names
	 * - Periodic Table of Metals
	 * - Solar System Names
	 * - Programming Languages
	 * - month_name
	 * - countries
	 * - real estate
	 * - food names
	 * - football-club-names
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

		topics["Periodic_Table_of_Metals"] = {"Lithium", "Beryllium", "Sodium", "Magnesium", "Aluminum", "Potassium", "Calcium",
											"Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", 
											"Copper", "Zinc", "Gallium", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", 
											"Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", 
											"Indium", "Tin", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", 
											"Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", 
											"Erbium", "Thulium"
											};

		topics["colors"] = {"Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White", "Gray",
		                    "Cyan", "Magenta", "Lime", "Indigo", "Violet", "Turquoise", "Teal", "Beige", "Coral", "Lavender",
		                    "Olive", "Maroon", "Navy", "Gold", "Silver", "Peach", "Mint", "Chocolate", "Ivory", "Mustard",
		                    "Amber", "Fuchsia", "Rose", "Aqua", "Crimson", "Salmon", "Khaki", "Plum", "Lilac", "Periwinkle",
		                    "Slate", "Copper", "Bronze", "Charcoal", "Taupe", "Emerald", "Sapphire", "Ruby", "Garnet", "Blush",
		                    "Cobalt", "Sand", "Mauve", "Azure", "Eggplant", "Ochre", "Denim", "Pearl", "Mint Green", "Forest Green"
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

		topics["programming_language"] = {"Python", "JavaScript", "Java", "C", "C++", "C#", "Go", "Rust", "PHP", "Swift",
		                                  "Kotlin", "Ruby", "TypeScript", "SQL", "R", "Dart", "Scala", "Shell", "Perl", "Objective-C",
		                                  "Lua", "Haskell", "Elixir", "MATLAB", "Visual Basic", "F#", "Groovy", "Erlang", "Clojure",
		                                  "COBOL", "Fortran", "VBScript", "Pascal", "Assembly", "VHDL", "Verilog", "Ada", "Prolog",
		                                  "Scratch", "PowerShell", "Julia", "Crystal", "Nim", "Scheme", "SAS", "ABAP", "APL", "Smalltalk",
		                                  "RPG", "Q#"
		                                 };

		topics["month_name"] = {"January", "Jan", "February", "Feb", "March", "Mar", "April", "Apr", "May", "June", "Jun",
		                        "July", "Jul", "August", "Aug", "September", "Sep", "October", "Oct", "November", "Nov", "December", "Dec"
		                       };

		topics["food_names"] = {"Pho", "Banh mi", "Banh xeo", "Goi cuon", "Com tam", "Cha gio", "Hu tieu", "Banh bao", "Xoi", "Banh chung", 
								"Banh duc", "Banh canh", "Mi Quang", "Ca ri", "Banh nam", "Chaolom", "Banh khot", "Banh bo", "Com chay", 
								"Banh tet", "Sui cao", "Banh trang nuong", "Mi hoanh thanh", "Dim sum", "Peking duck", "Mapo tofu", "Dumplings",
								 "Hot pot", "Kung Pao chicken", "Xiao long bao", "Chow mein", "Sweet and sour pork", "Jiaozi", "Mooncake", 
								 "Ma la", "Sichuan hotpot", "Chashu", "Sushi", "Ramen", "Tempura", "Tonkatsu", "Takoyaki", "Okonomiyaki", 
								 "Unagi", "Kaiseki", "Sashimi", "Mochi", "Shabu-shabu", "Udon", "Gyoza", "Omurice", "Chirashi", "Kare Raisu", 
								 "Ebi fry", "Yakisoba", "Negima", "Onigiri", "Miso soup", "Katsudon", "Tamagoyaki", "Zaru soba", "Soba", 
								 "Chanko nabe", "Sukiyaki", "Tempura soba", "Izakaya", "Tonkotsu ramen", "Burger", "French fries", "Pizza", 
								 "Hot dog", "Fried chicken", "Chicken nuggets", "Tacos", "Burrito", "Spaghetti", "Lasagna", "Chicken wings", 
								 "Onion rings", "Grilled cheese sandwich", "Poutine", "Fried rice", "Fish and chips", "Doner kebab", 
								 "Cheeseburger", "Falafel", "Bagel", "Gyro", "Shawarma", "Steak", "Barbecue ribs"
								 };

		topics["countries"] = {"Afghanistan", "AFG", "Albania", "ALB", "Algeria", "ALG", "Andorra", "AND", "Angola", "ANG", "Argentina", "ARG",
		                       "Armenia", "ARM", "Australia", "AUS", "Austria", "AUT", "Azerbaijan", "AZE", "Bahamas", "BAH", "Bahrain", "BHR",
		                       "Bangladesh", "BAN", "Barbados", "BAR", "Belarus", "BLR", "Belgium", "BEL", "Belize", "BZE", "Benin", "BEN",
		                       "Bhutan", "BHU", "Bolivia", "BOL", "Bosnia", "BOS", "Botswana", "BOT", "Brazil", "BRA", "Brunei", "BRU",
		                       "Bulgaria", "BUL", "Burkina Faso", "BUR", "Burundi", "BDI", "Cambodia", "CAM", "Cameroon", "CMR", "Canada", "CAN",
		                       "Cape Verde", "CPV", "Chad", "CHA", "Chile", "CHI", "China", "CHN", "Colombia", "COL", "Comoros", "COM",
		                       "Congo", "CON", "Costa Rica", "CRI", "Croatia", "CRO", "Cuba", "CUB", "Cyprus", "CYP", "Czech Republic", "CZE",
		                       "Denmark", "DEN", "Djibouti", "DJI", "Dominica", "DMA", "Dominican Republic", "DOM", "Ecuador", "ECU", "Egypt", "EGY",
		                       "El Salvador", "ELS", "Equatorial Guinea", "EQG", "Eritrea", "ERI", "Estonia", "EST", "Eswatini", "ESW", "Ethiopia", "ETH",
		                       "Fiji", "FIJ", "Finland", "FIN", "France", "FRA", "Gabon", "GAB", "Gambia", "GAM", "Georgia", "GEO",
		                       "Germany", "GER", "Ghana", "GHA", "Greece", "GRE", "Grenada", "GRN", "Guatemala", "GUA", "Guinea", "GUI",
		                       "Guinea-Bissau", "GBS", "Guyana", "GUY", "Haiti", "HAI", "Honduras", "HON", "Hungary", "HUN", "Iceland", "ICE",
		                       "India", "IND", "Indonesia", "IDO", "Iran", "IRN", "Iraq", "IRQ", "Ireland", "IRE", "Israel", "ISR",
		                       "Italy", "ITA", "Ivory Coast", "CIV", "Jamaica", "JAM", "Japan", "JPN", "Jordan", "JOR", "Kazakhstan", "KAZ",
		                       "Kenya", "KEN", "Kiribati", "KIR", "Kuwait", "KUW", "Kyrgyzstan", "KGZ", "Laos", "LAO", "Latvia", "LAT",
		                       "Lebanon", "LEB", "Lesotho", "LES", "Liberia", "LIB", "Libya", "LBY", "Liechtenstein", "LIE", "Lithuania", "LIT",
		                       "Luxembourg", "LUX", "Madagascar", "MAD", "Malawi", "MAW", "Malaysia", "MAS", "Maldives", "MDV", "Mali", "MAL",
		                       "Malta", "MLT", "Mauritania", "MAU", "Mauritius", "MRI", "Mexico", "MEX", "Micronesia", "MIC", "Moldova", "MOL",
		                       "Monaco", "MON", "Mongolia", "MNG", "Montenegro", "MNE", "Morocco", "MOR", "Mozambique", "MOZ", "Myanmar", "MYA",
		                       "Namibia", "NAM", "Nauru", "NRU", "Nepal", "NEP", "Netherlands", "NED", "New Zealand", "NZL", "Nicaragua", "NIC",
		                       "Niger", "NGR", "Nigeria", "NIG", "North Korea", "PRK", "Norway", "NOR", "Oman", "OMA", "Pakistan", "PAK",
		                       "Palau", "PAL", "Panama", "PAN", "Papua New Guinea", "PNG", "Paraguay", "PAR", "Peru", "PER", "Philippines", "PHI",
		                       "Poland", "POL", "Portugal", "POR", "Qatar", "QAT", "Romania", "ROM", "Russia", "RUS", "Rwanda", "RWA",
		                       "Saint Kitts", "SKN", "Saint Lucia", "LCA", "Saint Vincent", "VIN", "Samoa", "SAM", "San Marino", "SMR", "Sao Tome", "STP",
		                       "Saudi Arabia", "KSA", "Senegal", "SEN", "Serbia", "SRB", "Seychelles", "SEY", "Sierra Leone", "SLE", "Singapore", "SIN",
		                       "Slovakia", "SVK", "Slovenia", "SLO", "Solomon Islands", "SOL", "Somalia", "SOM", "South Africa", "RSA", "South Korea", "KOR",
		                       "Spain", "ESP", "Sri Lanka", "SRI", "Sudan", "SUD", "Suriname", "SUR", "Sweden", "SWE", "Switzerland", "SUI",
		                       "Syria", "SYR", "Taiwan", "TWN", "Tajikistan", "TAJ", "Tanzania", "TAN", "Thailand", "THA", "Togo", "TOG",
		                       "Tonga", "TON", "Trinidad and Tobago", "TTO", "Tunisia", "TUN", "Turkey", "TUR", "Turkmenistan", "TKM", "Tuvalu", "TUV",
		                       "Uganda", "UGA", "Ukraine", "UKR", "United Arab Emirates", "UAE", "United Kingdom", "UK", "United States", "USA", "Uruguay", "URU",
		                       "Uzbekistan", "UZB", "Vanuatu", "VAN", "Vatican City", "VAT", "Venezuela", "VEN", "Vietnam", "VIE", "Yemen", "YEM",
		                       "Zambia", "ZAM", "Zimbabwe", "ZIM"
		                      };

		topics["bible_heros"] = {"Adam", "Eve", "Noah", "Abraham", "Sarah", "Isaac", "Jacob", "Joseph", "Moses", "Aaron", "Joshua", "Deborah",
		                         "Gideon", "Samson", "Ruth", "Samuel", "David", "Solomon", "Elijah", "Elisha", "Esther", "Job", "Nehemiah",
		                         "Daniel", "Mary", "Joseph", "John the Baptist", "Peter", "Paul", "John", "James", "Stephen", "Philip",
		                         "Barnabas", "Timothy", "Luke", "Mary Magdalene", "Martha", "Lazarus", "Priscilla", "Aquila"
		                        };

		topics["real_estate"] = {"single-family home", "multi-family home", "apartment", "condominium", "townhouse",
		                         "duplex", "triplex", "quadplex", "penthouse", "villa", "mansion", "cottage", "bungalow", "farmhouse", "mobile home", "manufactured home",
		                         "tiny house", "vacation home", "office building", "retail space", "warehouse", "industrial facility", "hotel", "restaurant",
		                         "mixed-use building", "co-working space", "manufacturing plant", "distribution center", "storage facility", "data center",
		                         "research and development lab", "residential land", "commercial land", "agricultural land", "industrial land", "recreational land",
		                         "forest land", "undeveloped land", "school", "hospital", "religious building", "government building", "sports facility",
		                         "entertainment venue", "waterfront property", "urban loft", "private island", "long-term rental", "short-term rental",
		                         "student housing", "corporate housing", "ski chalet", "beach house", "golf course property", "cabin", "farm", "ranch", "vineyard",
		                         "orchard", "retirement home", "assisted living facility", "nursing home", "subsidized housing", "social housing",
		                         "low-income housing", "green building", "solar-powered home", "sustainable development"
		                        };

		topics["football_clubs"] = {"Bayern Munich", "Liverpool", "Manchester United", "Real Madrid", "Barcelona", "Paris Saint-Germain",
		                            "Juventus", "Chelsea", "Arsenal", "Manchester City", "Tottenham Hotspur", "AC Milan", "Inter Milan", "Napoli", "Atletico Madrid",
		                            "Borussia Dortmund", "RB Leipzig", "Sevilla", "AS Roma", "Ajax Amsterdam", "Benfica", "Porto", "Sporting Lisbon", "Lazio",
		                            "Shakhtar Donetsk", "Zenit St. Petersburg", "Celtic", "Rangers", "Galatasaray", "FenerbahC'e", "Besiktas", "Olympique Lyon",
		                            "Olympique Marseille", "Monaco", "Valencia", "Villarreal", "PSV Eindhoven", "Red Star Belgrade", "Dynamo Kyiv",
		                            "Club Brugge", "Flamengo", "Palmeiras", "River Plate", "Boca Juniors", "Santos FC"
		                           };

		topics["body_parts"] = {"Head", "Neck", "Shoulder", "Arm", "Elbow", "Forearm", "Wrist", "Hand", "Palm", "Fingers", "Thumb",
		                        "Chest", "Back", "Abdomen", "Waist", "Hip", "Buttocks", "Thigh", "Knee", "Leg", "Shin", "Calf", "Ankle", "Foot", "Toes",
		                        "Heel", "Skull", "Brain", "Heart", "Lungs", "Liver", "Stomach", "Kidneys", "Bladder", "Pancreas", "Intestines", "Spleen",
		                        "Esophagus", "Trachea", "Ears", "Eyes", "Nose", "Mouth", "Lips", "Teeth", "Tongue", "Jaw", "Skin", "Hair"
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
		vector<string> topicsList = {"animal", "fruit", "vehicle", "plant", "month_name", "bible_heros", "programming_language",
		                             "vehicle", "real_estate", "countries", "football_clubs", "body_parts", "Periodic_Table_of_Metals",
									 "food_names"
		                            };
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