#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

class Item {
public:
    int id;
    string name;
    int quantity;
   
    void display() {
        cout << "ID: " << id << "\tName: " << name << "\tQuantity: " << quantity << endl;
    }
};

vector<Item> inventory;

void saveToFile() {
    ofstream file("inventory.txt");
    for(Item item : inventory) {
        file << item.id << " " << item.name << " " << item.quantity << "\n";
    }
    file.close();
    cout << "Inventory saved!\n";
}

void loadFromFile() {
    ifstream file("inventory.txt");
    Item temp;
    while(file >> temp.id >> temp.name >> temp.quantity) {
        inventory.push_back(temp);
    }
    file.close();
    cout << "Inventory loaded!\n";
}

int main() {
    int choice;
    loadFromFile();

    do {
        cout << "\n=== Inventory System ===\n";
        cout << "1. Add Item\n2. List Items\n3. Update Quantity\n4. Save & Exit\nChoice: ";
        cin >> choice;

        switch(choice) {
            case 1: {
                Item newItem;
                cout << "Enter ID: ";
                cin >> newItem.id;
                cout << "Enter name: ";
                cin >> newItem.name;
                cout << "Enter quantity: ";
                cin >> newItem.quantity;
                inventory.push_back(newItem);
                break;
            }
            case 2:
                cout << "\nCurrent Inventory:\n";
                for(Item item : inventory) item.display();
                break;
            case 3: {
                int searchId, newQty;
                cout << "Enter item ID to update: ";
                cin >> searchId;
                for(Item &item : inventory) {
                    if(item.id == searchId) {
                        cout << "New quantity: ";
                        cin >> newQty;
                        item.quantity = newQty;
                        return 0;
                    }
                }
                cout << "Item not found!\n";
                break;
            }
            case 4:
                saveToFile();
                break;
        }
    } while(choice != 4);

    return 0;
}