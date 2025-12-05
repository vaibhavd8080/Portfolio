#include <iostream>
#include <vector>
#include <string>

using namespace std;

// --- Smart Parking Management System ---
// Features: Park Car, Remove Car, Check Availability

class ParkingSystem {
    int totalSlots;
    int availableSlots;
    vector<int> parkingSlots; // 0 means empty, 1 means occupied

public:
    // Constructor to initialize the parking lot
    ParkingSystem(int size) {
        totalSlots = size;
        availableSlots = size;
        parkingSlots.assign(size, 0); // Initialize all slots to 0 (Empty)
    }

    // Function to park a vehicle
    void parkVehicle() {
        if (availableSlots == 0) {
            cout << "Sorry, Parking is Full!" << endl;
            return;
        }

        for (int i = 0; i < totalSlots; i++) {
            if (parkingSlots[i] == 0) {
                parkingSlots[i] = 1; // Mark as occupied
                availableSlots--;
                cout << "Vehicle Parked at Slot Number: " << (i + 1) << endl;
                return;
            }
        }
    }

    // Function to remove a vehicle
    void removeVehicle() {
        int slotNum;
        cout << "Enter Slot Number to Empty: ";
        cin >> slotNum;

        if (slotNum < 1 || slotNum > totalSlots) {
            cout << "Invalid Slot Number!" << endl;
        } else if (parkingSlots[slotNum - 1] == 0) {
            cout << "Slot is already empty." << endl;
        } else {
            parkingSlots[slotNum - 1] = 0; // Mark as empty
            availableSlots++;
            cout << "Vehicle Removed. Thank you!" << endl;
            // Simple logic: Charge 20 rupees per hour (assuming 1 hour fixed for demo)
            cout << "Parking Fee: 20 Rupees." << endl;
        }
    }

    // Show status
    void showStatus() {
        cout << "\n--- Parking Status ---" << endl;
        cout << "Available Slots: " << availableSlots << " / " << totalSlots << endl;
    }
};

int main() {
    // Create a parking lot with 5 slots
    ParkingSystem myParking(5);
    int choice;

    do {
        cout << "\n1. Park Vehicle\n2. Remove Vehicle\n3. Show Status\n4. Exit\nChoose: ";
        cin >> choice;

        switch(choice) {
            case 1: myParking.parkVehicle(); break;
            case 2: myParking.removeVehicle(); break;
            case 3: myParking.showStatus(); break;
            case 4: cout << "Exiting System..." << endl; break;
            default: cout << "Invalid Choice" << endl;
        }
    } while (choice != 4);

    return 0;
}
