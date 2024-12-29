#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <algorithm>

// Define the possible game types
enum GameType {
    VIETNAMESE_POKER,
    THIRTEEN,
    INVALID
};

// Define the Card structure
struct Card {
    int rank;  // 1-13 (Ace to King)
    char suit; // 'H' for Hearts, 'D' for Diamonds, 'C' for Clubs, 'S' for Spades
};

// Function to get the full name of the suit based on the single letter (H, D, C, S)
std::string getSuitName(char suit) {
    switch (suit) {
        case 'H': return "Hearts";
        case 'D': return "Diamonds";
        case 'C': return "Clubs";
        case 'S': return "Spades";
        default: return "Unknown Suit";
    }
}

// Function to get the full name of the rank (Ace, Jack, Queen, King)
std::string getRankName(int rank) {
    switch (rank) {
        case 1: return "A";  // Ace
        case 11: return "J"; // Jack
        case 12: return "Q"; // Queen
        case 13: return "K"; // King
        default: return std::to_string(rank); // For 2 to 10, just return the number
    }
}

// Function to calculate the value of a hand in Thirteen (Blackjack)
int calculateHandValue(const std::vector<Card>& hand) {
    int value = 0;
    int aces = 0;

    for (const Card& card : hand) {
        if (card.rank > 10) {
            value += 10; // Face cards count as 10
        } else if (card.rank == 1) {
            value += 11; // Ace counts as 11
            aces++;
        } else {
            value += card.rank; // Number cards
        }
    }

    // Adjust for Aces if value exceeds 21
    while (value > 21 && aces > 0) {
        value -= 10; // Count Ace as 1 instead of 11
        aces--;
    }

    return value;
}

// Function to play Thirteen (Blackjack)
void playThirteen(std::vector<Card>& deck) {
    std::vector<Card> hand;
    hand.push_back(deck.back()); deck.pop_back(); // Draw 1st card
    hand.push_back(deck.back()); deck.pop_back(); // Draw 2nd card

    std::cout << "Your hand: " << getRankName(hand[0].rank) << " of " << getSuitName(hand[0].suit) << " and " 
              << getRankName(hand[1].rank) << " of " << getSuitName(hand[1].suit) << std::endl;

    int handValue = calculateHandValue(hand);
    std::cout << "Hand value: " << handValue << std::endl;

    char choice;
    while (handValue < 21) {
        std::cout << "Do you want to (h)it or (s)tand? ";
        std::cin >> choice;
        if (choice == 'h' || choice == 'H') {
            hand.push_back(deck.back());
            deck.pop_back();
            std::cout << "You drew a " << getRankName(hand.back().rank) << " of " << getSuitName(hand.back().suit) << std::endl;
            handValue = calculateHandValue(hand);
            std::cout << "New hand value: " << handValue << std::endl;
        } else if (choice == 's' || choice == 'S') {
            break;
        }
    }

    if (handValue > 21) {
        std::cout << "You busted! Hand value: " << handValue << std::endl;
    } else {
        std::cout << "You stand with hand value: " << handValue << std::endl;
    }
}

// Function to ask the user which game they want to play
GameType chooseGame() {
    int choice;
    std::cout << "Welcome to the Card Game!\n";
    std::cout << "1. Vietnamese Poker\n";
    std::cout << "2. Thirteen\n";
    std::cout << "Please choose a game (1 or 2): ";
    std::cin >> choice;

    if (choice == 1) {
        return VIETNAMESE_POKER;
    } else if (choice == 2) {
        return THIRTEEN;
    } else {
        return INVALID;
    }
}

// Function to create a deck of 52 cards
std::vector<Card> createDeck() {
    std::vector<Card> deck;
    char suits[] = {'H', 'D', 'C', 'S'};
    for (char suit : suits) {
        for (int rank = 1; rank <= 13; ++rank) {
            deck.push_back(Card{rank, suit});
        }
    }
    return deck;
}

// Function to shuffle the deck
void shuffleDeck(std::vector<Card>& deck) {
    std::srand(std::time(0)); // Seed the random number generator
    for (int i = deck.size() - 1; i > 0; --i) {
        int j = std::rand() % (i + 1);
        std::swap(deck[i], deck[j]);
    }
}

// Function to compare two cards for Vietnamese Poker (Tiến Lên)
bool isHigherCard(const Card& card1, const Card& card2) {
    // The higher card is determined by rank (with 2 being the highest)
    if (card1.rank == 2 && card2.rank != 2) return true;  // 2 is always the highest
    if (card2.rank == 2 && card1.rank != 2) return false;
    return card1.rank > card2.rank;
}

// Function to compare pairs (two cards of the same rank)
bool isHigherPair(const std::vector<Card>& pair1, const std::vector<Card>& pair2) {
    return isHigherCard(pair1[0], pair2[0]);
}

// Function to compare triples (three cards of the same rank)
bool isHigherTriple(const std::vector<Card>& triple1, const std::vector<Card>& triple2) {
    return isHigherCard(triple1[0], triple2[0]);
}

// Function to play Vietnamese Poker (Tiến Lên)
void playVietnamesePoker(std::vector<Card>& deck) {
    std::vector<Card> player1_hand, player2_hand;
    player1_hand.push_back(deck.back()); deck.pop_back(); // Draw for player 1
    player1_hand.push_back(deck.back()); deck.pop_back();
    player2_hand.push_back(deck.back()); deck.pop_back(); // Draw for player 2
    player2_hand.push_back(deck.back()); deck.pop_back();

    // Display initial hands
    std::cout << "Player 1's hand: " << getRankName(player1_hand[0].rank) << " of " << getSuitName(player1_hand[0].suit) << ", " 
              << getRankName(player1_hand[1].rank) << " of " << getSuitName(player1_hand[1].suit) << "\n";
    std::cout << "Player 2's hand: " << getRankName(player2_hand[0].rank) << " of " << getSuitName(player2_hand[0].suit) << ", " 
              << getRankName(player2_hand[1].rank) << " of " << getSuitName(player2_hand[1].suit) << "\n";

    bool gameOver = false;
    bool player1Passed = false, player2Passed = false;
    while (!gameOver) {
        std::cout << "\nPlayer 1's turn:\n";
        std::cout << "1. Play a card\n";
        std::cout << "2. Pass\n";
        int choice;
        std::cin >> choice;

        if (choice == 1) {
            // Player 1 plays a card
            std::cout << "Player 1 plays: " << getRankName(player1_hand[0].rank) << " of " << getSuitName(player1_hand[0].suit) << std::endl;
            player1_hand.clear();  // Remove the played card
        } else if (choice == 2) {
            player1Passed = true;
            std::cout << "Player 1 passes.\n";
        }

        // Check if game over (both players passed)
        if (player1Passed && player2Passed) {
            std::cout << "Both players passed, game over.\n";
            gameOver = true;
        }

        std::cout << "\nPlayer 2's turn:\n";
        std::cout << "1. Play a card\n";
        std::cout << "2. Pass\n";
        std::cin >> choice;

        if (choice == 1) {
            // Player 2 plays a card
            std::cout << "Player 2 plays: " << getRankName(player2_hand[0].rank) << " of " << getSuitName(player2_hand[0].suit) << std::endl;
            player2_hand.clear();  // Remove the played card
        } else if (choice == 2) {
            player2Passed = true;
            std::cout << "Player 2 passes.\n";
        }

        // Check if game over (both players passed)
        if (player1Passed && player2Passed) {
            std::cout << "Both players passed, game over.\n";
            gameOver = true;
        }
    }
}

int main() {
    GameType game = chooseGame();

    if (game == INVALID) {
        std::cout << "Invalid choice. Exiting game.\n";
        return 0;
    }

    // Create and shuffle the deck
    std::vector<Card> deck = createDeck();
    shuffleDeck(deck);

    if (game == THIRTEEN) {
        playThirteen(deck);
    } else if (game == VIETNAMESE_POKER) {
        playVietnamesePoker(deck);
    }

    return 0;
}