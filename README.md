# Aircraft-Data-CSV-Generator

# Operation LUSTY Aircraft Data Generator

This Python script simulates the movement of military aircraft and service members between bases during the Vietnam War, as part of a fictional operation named **Operation LUSTY**, inspired by historical events following World War II.

The data generated includes details like service members' names, ranks, SSNs, service numbers, and aircraft types. The data can be exported into a CSV file, which can be used for various purposes such as manual backups or for inserting into databases like **Redis**, **MongoDB**, or **DynamoDB**.

## Features

- Generates detailed information for **fictional service members** and **aircraft transfers** between military bases.
- Output includes fields such as **rank**, **service number**, **aircraft type**, **origin and destination bases**, and **transfer status**.
- Data generated is entirely fictional but based on historical wartime operations, making it ideal for simulating wartime scenarios.
- The script outputs data as a CSV file, ready for use in **Excel** or other data manipulation tools.
- Data can be piped into **cloud databases** such as **Redis**, **MongoDB**, or **DynamoDB**.

## Historical Reference

**Operation LUSTY** was a real post-World War II mission aimed at recovering German aircraft technology. This script, however, fictionalizes a Vietnam War-era operation under the same codename. The data generated mimics the movement of aircraft and personnel between bases during wartime scenarios, with a specific focus on the Vietnam War.

## Requirements

This script requires Python 3.x and the following Python libraries:

- `Faker` for generating realistic names, ranks, addresses, and other personal data.
- If extending the functionality to connect to cloud databases, install:
  - `redis` for Redis database
  - `pymongo` for MongoDB
  - `boto3` for DynamoDB

You can install all dependencies by running:

```bash
pip install -r requirements.txt
