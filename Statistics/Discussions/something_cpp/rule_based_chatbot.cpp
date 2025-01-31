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
           lowerInput.find("mushroom_soup") != std::string::npos ||           
           lowerInput.find("chicken_fries") != std::string::npos ||
           lowerInput.find("hamburger") != std::string::npos ||           
           lowerInput.find("french_fries") != std::string::npos ||
           lowerInput.find("snack") != std::string::npos ||
           lowerInput.find("lasagna") != std::string::npos ||
           lowerInput.find("fried_rice") != std::string::npos ||
           lowerInput.find("tacos") != std::string::npos ||
           lowerInput.find("hot_dog") != std::string::npos ||
           lowerInput.find("kebab") != std::string::npos ||
           lowerInput.find("ramen") != std::string::npos ||
           lowerInput.find("dim_sum") != std::string::npos ||
           lowerInput.find("burrito") != std::string::npos ||
           lowerInput.find("samosa") != std::string::npos ||
           lowerInput.find("steak") != std::string::npos ||
           lowerInput.find("cheeseburger") != std::string::npos ||
           lowerInput.find("chow_mein") != std::string::npos ||
           lowerInput.find("grilled_cheese") != std::string::npos ||
           lowerInput.find("eggrolls") != std::string::npos ||
           lowerInput.find("risotto") != std::string::npos ||
           lowerInput.find("nachos") != std::string::npos ||
           lowerInput.find("paella") != std::string::npos ||
           lowerInput.find("falafel") != std::string::npos ||
           lowerInput.find("ceviche") != std::string::npos ||
           lowerInput.find("quiche") != std::string::npos ||
           lowerInput.find("goulash") != std::string::npos ||
           lowerInput.find("clams") != std::string::npos ||
           lowerInput.find("pizza_pasta") != std::string::npos ||
           lowerInput.find("moussaka") != std::string::npos ||
           lowerInput.find("beef_tacos") != std::string::npos ||
           lowerInput.find("bangers_and_mash") != std::string::npos ||
           lowerInput.find("chicken_wings") != std::string::npos ||
           lowerInput.find("eggplant_parmesan") != std::string::npos ||
           lowerInput.find("coq_au_vin") != std::string::npos ||
           lowerInput.find("tuna_sashimi") != std::string::npos ||
           lowerInput.find("stuffed_peppers") != std::string::npos ||
           lowerInput.find("maki_rolls") != std::string::npos ||
           lowerInput.find("poutine") != std::string::npos ||
           lowerInput.find("baked_ziti") != std::string::npos ||
           lowerInput.find("eggplant_rollatini") != std::string::npos ||
           lowerInput.find("shakshuka") != std::string::npos ||
           lowerInput.find("tom_yum_soup") != std::string::npos ||
           lowerInput.find("hummus") != std::string::npos ||
           lowerInput.find("curry") != std::string::npos ||
           lowerInput.find("tandoori_chicken") != std::string::npos;
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

// Function to check if the input is a drink query
bool isDrinkQuery(const std::string& input) {
    std::string lowerInput = toLowerCase(input);
    return lowerInput.find("red wine") != std::string::npos ||
           lowerInput.find("champagne") != std::string::npos ||
           lowerInput.find("cocktail") != std::string::npos ||
           lowerInput.find("johny walker") != std::string::npos ||
           lowerInput.find("whiskey") != std::string::npos ||
           lowerInput.find("vodka") != std::string::npos ||
           lowerInput.find("beer") != std::string::npos ||
           lowerInput.find("rum") != std::string::npos;
}

// Function to handle drink orders
void handleDrinkOrder(const std::string& input) {
    std::string lowerInput = toLowerCase(input);
    std::cout << "Bot: You want to order a drink. ";
    
    if (lowerInput.find("red wine") != std::string::npos) {
        std::cout << "How about a nice glass of red wine?" << std::endl;
    }
    else if (lowerInput.find("champagne") != std::string::npos) {
        std::cout << "Champagne, perfect for a celebration!" << std::endl;
    }
    else if (lowerInput.find("cocktail") != std::string::npos) {
        std::cout << "A cocktail coming right up! What type of cocktail would you like?" << std::endl;
    }
    else if (lowerInput.find("johny walker") != std::string::npos) {
        std::cout << "A glass of Johnny Walker, excellent choice!" << std::endl;
    }
    else if (lowerInput.find("whiskey") != std::string::npos) {
        std::cout << "Would you like a shot of whiskey?" << std::endl;
    }
    else if (lowerInput.find("vodka") != std::string::npos) {
        std::cout << "A vodka-based drink sounds great!" << std::endl;
    }
    else if (lowerInput.find("beer") != std::string::npos) {
        std::cout << "A cold beer coming your way!" << std::endl;
    }
    else if (lowerInput.find("rum") != std::string::npos) {
        std::cout << "Rum! Would you like it straight or in a cocktail?" << std::endl;
    }
    else {
        std::cout << "I didn't quite catch that. What kind of drink would you like to order?" << std::endl;
    }
}

// Function to extract meal details from a sentence using regex
bool extractMealDetails(const std::string& input, std::vector<std::string>& meals, int& numPeople, std::string& mealTime, std::string& mealType) {
    std::regex mealPattern("(sushi|pho|pad_thai|beefsteak|burger|pizza|french_fries|pasta|snack|doner_kabab|peking_duck|carbonara|hamburger|chicken_fries|mushroom_soup)", 
                            std::regex::icase);
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

    if (!mealList.empty()) {
        meals = mealList;
    }
    
    // Extract meal time
    if (std::regex_search(input, match, timePattern)) {
        mealTime = match.str(1);
    }

    // Extract meal type
    if (std::regex_search(input, match, typePattern)) {
        mealType = match.str(1);
    }

    return !meals.empty() || numPeople > 0 || !mealTime.empty() || !mealType.empty();
}

// Function to introduce the bot
void introduceBot() {
    std::cout << "Bot: Hello! I'm your personal assistant." << std::endl;
    std::cout << "I can help you with the following:" << std::endl;
    std::cout << "1. Meal suggestions: I can help you choose meals like breakfast, lunch, dinner, or snacks." << std::endl;
    std::cout << "2. Meal quantity: Let me know how many people you're ordering for." << std::endl;
    std::cout << "3. Meal timing: I can help you schedule the meal time." << std::endl;
    std::cout << "4. Farewell: If you're done, just say goodbye!" << std::endl;
    std::cout << "You can type 'exit' to end the conversation." << std::endl;
    std::cout << "What would you like to do?" << std::endl;
}

// Function to generate a response based on user input
void generateResponse(const std::string& input) {
    if (isGreeting(input)) {
        introduceBot();
    } 
    else if (isFarewell(input)) {
        std::cout << "Bot: Goodbye! Have a good meal!" << std::endl;
    }
    else if (isMealQuery(input)) {
        std::vector<std::string> meals;
        int numPeople = 0;
        std::string mealTime, mealType;
        if (extractMealDetails(input, meals, numPeople, mealTime, mealType)) {
            std::cout << "Bot: I can suggest the following meals: ";
            for (const auto& meal : meals) {
                std::cout << meal << ", ";
            }
            std::cout << std::endl;
            if (numPeople > 0) {
                std::cout << "Bot: For " << numPeople << " people." << std::endl;
            }
            if (!mealTime.empty()) {
                std::cout << "Bot: How about having the meal at " << mealTime << "?" << std::endl;
            }
            if (!mealType.empty()) {
                std::cout << "Bot: I suggest having it for " << mealType << "." << std::endl;
            }
        } 
        else {
            std::cout << "Bot: I'm not sure what you're asking for, can you clarify?" << std::endl;
        }
    }
    else if (isDrinkQuery(input)) {
        handleDrinkOrder(input);
    }
    else {
        std::cout << "Bot: I'm not sure how to respond to that. Can you clarify?" << std::endl;
    }
}

int main() {
    std::string userInput;
    
    // Start conversation
    std::cout << "Bot: Hello! How can I help you today?" << std::endl;
    while (true) {
        std::cout << "You: ";
        std::getline(std::cin, userInput);
        if (userInput == "exit") {
            std::cout << "Bot: Goodbye! Have a good meal!" << std::endl;
            break;
        }
        generateResponse(userInput);
    }
    
    return 0;
}