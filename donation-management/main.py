import json
from pathlib import Path


class DonationManager:
    FILE_PATH = Path("donations.json")

    def __init__(self):
        self.donations = {}
        self.load_data()

    def load_data(self):
        if not self.FILE_PATH.exists():
            return

        try:
            with self.FILE_PATH.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.donations = data

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load donation data.")

    def save_data(self):
        try:
            with self.FILE_PATH.open("w", encoding="utf-8") as file:
                json.dump(
                    self.donations,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
        except OSError:
            print("Error: Could not save donation data.")

    @staticmethod
    def get_amount():
        while True:
            try:
                amount = float(input("Enter donation amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                return amount

            except ValueError:
                print("Please enter a valid number.")

    def add_donation(self):
        name = input("Enter person's name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        amount = self.get_amount()

        self.donations[name] = self.donations.get(name, 0) + amount

        self.save_data()
        print("Donation added successfully!")

    def show_donations(self):
        if not self.donations:
            print("No donations registered.")
            return

        print("\n========== DONATIONS ==========")

        for name, amount in self.donations.items():
            print(f"{name}: {amount:,.2f}")

    def analyze_donations(self):
        if not self.donations:
            print("No data available for analysis.")
            return

        total = sum(self.donations.values())
        count = len(self.donations)
        average = total / count

        max_person = max(self.donations, key=self.donations.get)
        min_person = min(self.donations, key=self.donations.get)

        print("\n========== DONATION ANALYSIS ==========")
        print(f"Total donations: {total:,.2f}")
        print(f"Number of donors: {count}")
        print(f"Average donation: {average:,.2f}")
        print(
            f"Highest donation: {max_person} "
            f"({self.donations[max_person]:,.2f})"
        )
        print(
            f"Lowest donation: {min_person} "
            f"({self.donations[min_person]:,.2f})"
        )

    def sort_donations(self):
        if not self.donations:
            print("No donations to sort.")
            return

        sorted_donations = sorted(
            self.donations.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n========== RANKING ==========")

        for rank, (name, amount) in enumerate(sorted_donations, start=1):
            print(f"{rank}. {name}: {amount:,.2f}")

    def search_donor(self):
        name = input("Enter name to search: ").strip().casefold()

        for donor, amount in self.donations.items():
            if donor.casefold() == name:
                print(f"{donor}: {amount:,.2f}")
                return

        print("Donor not found.")

    def delete_donation(self):
        name = input("Enter name to delete: ").strip().casefold()

        for donor in list(self.donations):
            if donor.casefold() == name:
                del self.donations[donor]
                self.save_data()
                print("Donation deleted successfully!")
                return

        print("Donor not found.")


def main():
    manager = DonationManager()

    while True:
        print("\n========== DONATION MANAGEMENT ==========")
        print("1. Add Donation")
        print("2. Show Donations")
        print("3. Analyze Donations")
        print("4. Sort Donations")
        print("5. Search Donor")
        print("6. Delete Donation")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_donation()

        elif choice == "2":
            manager.show_donations()

        elif choice == "3":
            manager.analyze_donations()

        elif choice == "4":
            manager.sort_donations()

        elif choice == "5":
            manager.search_donor()

        elif choice == "6":
            manager.delete_donation()

        elif choice == "7":
            print("Thank you for using Donation Management System!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

