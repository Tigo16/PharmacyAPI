import requests
import random
import time

# URL API
BASE_URL = "http://localhost:8000"  # URL вашего FastAPI приложения

# Примерные данные для добавления лекарств
DRUGS = [
    {"name": "Paracetamol", "manufacturer": "Pharma Inc.", "dosage": "500mg", "indications": "Pain, fever",
     "contraindications": "Allergy"},
    {"name": "Aspirin", "manufacturer": "Health Co.", "dosage": "300mg", "indications": "Pain, inflammation",
     "contraindications": "Stomach ulcers"},
    {"name": "Ibuprofen", "manufacturer": "MedLife", "dosage": "200mg", "indications": "Pain, inflammation",
     "contraindications": "Liver issues"},
]

# Примерные данные для добавления аптек
PHARMACIES = [
    {"name": "Pharmacy #1", "address": "10 Lenin St.", "phone": "+7 123 456 7890", "specialization": "General"},
    {"name": "Pharmacy #2", "address": "25 Mira St.", "phone": "+7 987 654 3210", "specialization": "Pediatrics"},
    {"name": "Pharmacy #3", "address": "5 Pobeda Ave.", "phone": "+7 555 123 4567", "specialization": "Herbal"},
]


# Функция для добавления лекарств
def create_drugs():
    print("Adding drugs...")
    drug_ids = []
    for drug in DRUGS:
        try:
            response = requests.post(f"{BASE_URL}/drugs/", json=drug)
            if response.status_code == 201:
                print(f"Added drug: {drug['name']}")
                drug_ids.append(response.json()['id'])  # Сохраняем ID добавленного лекарства
            else:
                print(f"Error adding drug: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
    return drug_ids


# Функция для добавления аптек
def create_pharmacies():
    print("Adding pharmacies...")
    pharmacy_ids = []
    for pharmacy in PHARMACIES:
        try:
            response = requests.post(f"{BASE_URL}/pharmacies/", json=pharmacy)
            if response.status_code == 201:
                print(f"Added pharmacy: {pharmacy['name']}")
                pharmacy_ids.append(response.json()['id'])  # Сохраняем ID добавленной аптеки
            else:
                print(f"Error adding pharmacy: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
    return pharmacy_ids


# Функция для добавления инвентаря
def create_inventory(drug_ids, pharmacy_ids):
    print("Adding inventory...")
    for _ in range(50):  # Создаем 50 записей инвентаря
        try:
            drug_id = random.choice(drug_ids)  # Выбираем существующий ID лекарства
            pharmacy_id = random.choice(pharmacy_ids)  # Выбираем существующий ID аптеки
            inventory = {
                "drug_id": drug_id,
                "pharmacy_id": pharmacy_id,
                "quantity": random.randint(1, 100),
                "price": round(random.uniform(10, 100), 2),
                "expiry_date": f"2025-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            }
            response = requests.post(f"{BASE_URL}/inventory/", json=inventory)
            if response.status_code == 201:
                print(f"Added inventory record: {inventory}")
            else:
                print(f"Error adding inventory record: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")


if __name__ == "__main__":
    start_time = time.time()

    # Добавляем данные
    drug_ids = create_drugs()
    pharmacy_ids = create_pharmacies()

    # Проверяем, что есть данные для создания инвентаря
    if drug_ids and pharmacy_ids:
        create_inventory(drug_ids, pharmacy_ids)
    else:
        print("Drugs or pharmacies data is missing. Skipping inventory creation.")

    print(f"Database population completed in {time.time() - start_time:.2f} seconds.")