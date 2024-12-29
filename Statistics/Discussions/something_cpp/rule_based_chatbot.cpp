#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <regex>

// Function to convert a string to lowercase for easy comparison
std::string toLowerCase(const std::string& str) {
    std::string lowerStr = str;
    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
    return lowerStr;
}

// Function to check if the input is a greeting
bool isGreeting(const std::string& input) {
    std::string lowerInput = toLowerCase(input);
    return lowerInput.find("hi") != std::string::npos || 
           lowerInput.find("hello") != std::string::npos || 
           lowerInput.find("hey") != std::string::npos ||
           lowerInput.find("alo") != std::string::npos ||
           lowerInput.find("haiz") != std::string::npos ||
           lowerInput.find("bonjour") != std::string::npos ||
           lowerInput.find("hallo") != std::string::npos ||
           lowerInput.find("good morning") != std::string::npos ||
           lowerInput.find("guten morgen") != std::string::npos ||
           lowerInput.find("ohio") != std::string::npos ||
           lowerInput.find("ciao") != std::string::npos || 
           lowerInput.find("xin chao") != std::string::npos ||
           lowerInput.find("xin chào") != std::string::npos ||                  
           lowerInput.find("konichiwa") != std::string::npos;
}

// Function to check if the input asks about a meal
bool isMealQuery(const std::string& input) {
    std::string lowerInput = toLowerCase(input);
    return lowerInput.find("meal") != std::string::npos || 
           lowerInput.find("eat") != std::string::npos || 
           lowerInput.find("food") != std::string::npos ||
           lowerInput.find("beefsteak") != std::string::npos ||
           lowerInput.find("doner_kabab") != std::string::npos ||
           lowerInput.find("peking_duck") != std::string::npos ||
           lowerInput.find("carbonara") != std::string::npos ||
           lowerInput.find("sushi") != std::string::npos ||
           lowerInput.find("pho") != std::string::npos ||
           lowerInput.find("pad_thai") != std::string::npos ||
           lowerInput.find("burger") != std::string::npos ||
           lowerInput.find("pasta") != std::string::npos ||
           lowerInput.find("pizza") != std::string::npos ||
           lowerInput.find("snack") != std::string::npos;
}

// Function to check if the input is a farewell
bool isFarewell(const std::string& input) {
    std::string lowerInput = toLowerCase(input);
    return lowerInput.find("bye") != std::string::npos || 
           lowerInput.find("goodbye") != std::string::npos ||
           lowerInput.find("good night") != std::string::npos ||
           lowerInput.find("thank for your help") != std::string::npos ||
           lowerInput.find("merci") != std::string::npos ||
           lowerInput.find("thanks") != std::string::npos ||
           lowerInput.find("thank you so much") != std::string::npos ||
           lowerInput.find("cảm ơn") != std::string::npos ||
           lowerInput.find("schone danke") != std::string::npos ||           
           lowerInput.find("danke") != std::string::npos ||
           lowerInput.find("ni hao") != std::string::npos;
}


// Function to extract meal details from a sentence using regex
bool extractMealDetails(const std::string& input, std::vector<std::string>& meals, int& numPeople, std::string& mealTime, std::string& mealType) {
    std::regex mealPattern("(sushi|pho|pad_thai|beefsteak|burger|pizza|pasta|snack|doner_kabab|peking_duck|carbonara)", std::regex::icase);
    std::regex quantityPattern("(\\d+)\\s?([a-zA-Z]+)");
    std::regex peoplePattern("(\\d+)\\s?people");
    std::regex timePattern("(\\d+\\s?am|pm|noon|midnight)");
    std::regex typePattern("(breakfast|lunch|dinner|snack)", std::regex::icase);
    
    std::smatch match;
    std::vector<std::string> mealList;
    numPeople = 0;
    
    // Extract number of people
    if (std::regex_search(input, match, peoplePattern)) {
        numPeople = std::stoi(match.str(1));
    }

    // Extract meal types
    std::sregex_iterator iter(input.begin(), input.end(), mealPattern);
    std::sregex_iterator end;
    while (iter != end) {
        mealList.push_back(iter->str());
        ++iter;
    }
    
    // Extract meal timing (e.g., "12 am", "noon")
    if (std::regex_search(input, match, timePattern)) {
        mealTime = match.str(1);
    }
    
    // Extract meal type (e.g., "lunch", "dinner")
    if (std::regex_search(input, match, typePattern)) {
        mealType = match.str(1);
    }

    if (!mealList.empty() && numPeople > 0 && !mealTime.empty() && !mealType.empty()) {
        meals = mealList;
        return true;
    }

    return false;
}

// Function to handle detailed meal queries and additional information
void askForMealDetails() {
    std::string mealType, quantity, timeOfMeal;

    std::cout << "Bot: What type of meal would you like? (e.g., breakfast, lunch, dinner, snack)" << std::endl;
    std::getline(std::cin, mealType);

    std::cout << "Bot: How many people are you ordering for?" << std::endl;
    std::getline(std::cin, quantity);

    std::cout << "Bot: When would you like to have the meal? (e.g., 12 AM, noon, or specific time)" << std::endl;
    std::getline(std::cin, timeOfMeal);

    std::cout << "Bot: Great! You want " << mealType << " for " << quantity << " people at " << timeOfMeal << ". Anything else I can help with?" << std::endl;
}

// Function to introduce the bot's capabilities and provide options
void introduceBot() {
    std::cout << "Bot: Hello! I'm your personal assistant." << std::endl;
    std::cout << "I can help you with the following:" << std::endl;
    std::cout << "1. Meal suggestions: I can help you choose meals like breakfast, lunch, dinner, or snacks." << std::endl;
    std::cout << "2. Meal quantity: Let me know how many people you're ordering for." << std::endl;
    std::cout << "3. Meal timing: I can help you schedule the meal time." << std::endl;
    std::cout << "4. Farewell: If you're done, just say goodbye!" << std::endl;
    std::cout << "You can type 'exit' to end the conversation." << std::endl;
}

// Function to generate a response based on the user's input
void generateResponse(const std::string& input) {
    static std::vector<std::string> meals;
    static int numPeople = 0;
    static std::string mealTime;
    static std::string mealType;

    if (isGreeting(input)) {
        std::cout << "Bot: Hello! How can I assist you today?" << std::endl;
        introduceBot();  // Provide bot introduction and options after greeting
    } 
    else if (isMealQuery(input)) {
        // If meal details are mentioned in a single input, extract and process them
        if (extractMealDetails(input, meals, numPeople, mealTime, mealType)) {
            std::cout << "Bot: Great! You want ";
            for (const auto& meal : meals) {
                std::cout << meal << " ";
            }
            std::cout << "for " << numPeople << " people at " << mealTime << " for " << mealType << ". Anything else I can help with?" << std::endl;
        } else {
            std::cout << "Bot: What would you like to have for a meal? I can suggest some options!" << std::endl;
            std::cout << "Bot: What type of meal would you like? (e.g., breakfast, lunch, dinner, snack)" << std::endl;
        }
    } 
    else if (isFarewell(input)) {
        std::cout << "Bot: Goodbye! Have a great day!" << std::endl;
        std::cout << "Bot: Thank you for chatting! Goodbye!" << std::endl;
        exit(0);  // Exit the conversation
    }
    else {
        std::cout << "Bot: Sorry, I didn't quite get that. Could you please ask something else?" << std::endl;
    }
}

int main() {
    std::string userInput;

    std::cout << "Welcome to the rule-based chatbot!" << std::endl;

    while (true) {
        std::cout << "You: ";
        std::getline(std::cin, userInput);  // Get user input

        if (toLowerCase(userInput) == "exit") {
            std::cout << "Bot: Thank you for chatting, have a good meal! Goodbye and see you soon!" << std::endl;
            break;
        }

        // Generate response based on user input
        generateResponse(userInput);
    }

    return 0;
}