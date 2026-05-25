import kagglehub
import shutil
import os

# Download dataset
path = kagglehub.dataset_download("blastchar/telco-customer-churn")

print("Dataset downloaded at:", path)

# Find CSV file
files = os.listdir(path)

for file in files:
    if file.endswith(".csv"):

        source_path = os.path.join(path, file)

        # Create data folder if not exists
        os.makedirs("data", exist_ok=True)

        destination_path = os.path.join("data", "telco_churn.csv")

        shutil.copy(source_path, destination_path)

        print("CSV copied to:", destination_path)