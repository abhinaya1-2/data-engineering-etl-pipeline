import pandas as pd


def validate_data(file_path):
    data = pd.read_csv(file_path)

    print("Running data validation checks...\n")

    print("Total rows:", len(data))
    print("Total columns:", len(data.columns))

    print("\nMissing values:")
    print(data.isnull().sum())

    print("\nDuplicate rows:")
    print(data.duplicated().sum())

    print("\nChecking total_amount calculation:")
    data["expected_total"] = data["quantity"] * data["price"]
    errors = data[data["total_amount"] != data["expected_total"]]

    if len(errors) == 0:
        print("All total_amount values are correct.")
    else:
        print("Errors found in total_amount:")
        print(errors)

    print("\nValidation completed.")


if __name__ == "__main__":
    validate_data("cleaned_sales_data.csv")
