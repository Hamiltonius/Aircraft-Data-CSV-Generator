import csv
from faker import Faker
import random
import os

fake = Faker()

ranks = ['Airman', 'Sergeant', 'Staff Sergeant', 'Lieutenant', 'Captain', 'Major']
bases = ['Elmendorf AFB', 'Pease Air FB']
statuses = ['Initiated', 'In Progress', 'Completed', 'Cancelled']
aircraft_types = ['F105', 'F111']  # Updated aircraft types

data_list = []  # List to store each entry as a dictionary

def generate_data(aircraft_type, num_entries):
    global aircraft_id_start
    for _ in range(num_entries):
        origin_base = random.choice(bases)
        destination_bases = list(set(bases) - {origin_base})
        destination_base = random.choice(destination_bases)
        entry = {
            "name": fake.name(),
            "rank": random.choice(ranks),
            "ssn": fake.ssn(),
            "service_number": str(random.randint(10000, 99999)),
            "dates_of_service": f"{random.randint(1967, 1972)}-{random.randint(1967, 1972)}",
            "home_of_record": fake.address(),
            "aircraft_id": f"BUNO {aircraft_id_start}",
            "aircraft_type": aircraft_type,
            "origin_base": origin_base,
            "destination_base": destination_base,
            "transfer_status": random.choice(statuses),
            "initiation_date": f"{random.randint(1967, 1972)}-01-01",
            "completion_date": f"{random.randint(1967, 1972)}-12-31"
        }
        # Adjust dates logic
        start_year, end_year = map(int, entry['dates_of_service'].split('-'))
        entry['dates_of_service'] = f"{min(start_year, end_year)}-{max(start_year, end_year)}"

        data_list.append(entry)
        aircraft_id_start += 1

aircraft_id_start = 80608  # Start ID for aircraft

# Generate data for each aircraft type
for aircraft_type in aircraft_types:
    generate_data(aircraft_type, 10)

# Define the directory on the desktop
desktop_path = os.path.join(os.path.expanduser("~/Desktop"), "AircraftData")
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Path for the CSV file
csv_file_path = os.path.join(desktop_path, 'aircraft_data.csv')

# Save the data to a CSV file
keys = data_list[0].keys()  # Get the fieldnames from the dictionary
with open(csv_file_path, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_list)

print(f"Data generation complete and saved to {csv_file_path}")
