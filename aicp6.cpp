#include <iostream>
#include <iomanip>
#include <unordered_map>

const double COST_CEMENT = 3.0;
const double COST_GRAVEL = 2.0;
const double COST_SAND = 2.0;
const double DISCOUNT_PACK_PRICE = 10.0;


void checkSack(double weight, char contents) {
    bool accepted = false;

    
    if (contents == 'C' || contents == 'G' || contents == 'S') {
       
        if ((contents == 'C' && weight > 24.9 && weight < 25.1) ||
            ((contents == 'G' || contents == 'S') && weight > 49.9 && weight < 50.1)) {
            accepted = true;
        }
    }

    
    if (accepted) {
        std::cout << "Accepted: ";
    } else {
        std::cout << "Rejected: ";
    }

    std::cout << "Contents: " << contents << ", Weight: " << weight << " kg" << std::endl;
}


void checkOrder(std::unordered_map<char, int>& order, double& totalWeight, int& rejectedSacks) {
    for (const auto& pair : order) {
        char contents = pair.first;
        int quantity = pair.second;

        for (int i = 0; i < quantity; ++i) {
            double weight;
            std::cout << "Enter the weight for " << contents << " sack: ";
            std::cin >> weight;

            checkSack(weight, contents);

            if (contents == 'C' || contents == 'G' || contents == 'S') {
                totalWeight += weight;
            } else {
                ++rejectedSacks;
            }
        }
    }
}


double calculatePrice(const std::unordered_map<char, int>& order, int discountPacks) {
    double totalPrice = 0;

    for (const auto& pair : order) {
        char contents = pair.first;
        int quantity = pair.second;

        if (contents == 'C') {
            totalPrice += COST_CEMENT * quantity;
        } else if (contents == 'G') {
            totalPrice += COST_GRAVEL * quantity;
        } else if (contents == 'S') {
            totalPrice += COST_SAND * quantity;
        }
    }

   
    totalPrice -= discountPacks * DISCOUNT_PACK_PRICE;

    return totalPrice;
}

int main() {
    // Test Task 1
    double weight;
    char contents;
    std::cout << "Enter the weight for a sack: ";
    std::cin >> weight;
    std::cout << "Enter the contents for the sack (C/G/S): ";
    std::cin >> contents;
    checkSack(weight, contents);

    // Test Task 2
    std::unordered_map<char, int> order = {{'C', 2}, {'G', 3}, {'S', 4}};
    double totalWeight = 0;
    int rejectedSacks = 0;
    checkOrder(order, totalWeight, rejectedSacks);
    std::cout << "Total Weight of Order: " << totalWeight << " kg" << std::endl;
    std::cout << "Number of Rejected Sacks: " << rejectedSacks << std::endl;

    // Test Task 3
    int discountPacks = std::min({order['C'], order['G'] / 2, order['S'] / 2});
    double totalPrice = calculatePrice(order, discountPacks);
    
    std::cout << "Regular Price: $" << totalPrice << std::endl;

    if (discountPacks > 0) {
        double discountSaved = discountPacks * DISCOUNT_PACK_PRICE;
        std::cout << "Discount Price: $" << totalPrice - discountSaved
                  << " (Amount Saved: $" << discountSaved << ")" << std::endl;
    }

    return 0;
}
