import pandas as pd
from faker import Faker
import pandas as pd
import random
from random import randint
import kaggle
import os
import nltk
from nltk.corpus import wordnet
fake = Faker()


# Serching from web
def generate_custom_data(num_rows):
    data = {
        "DATE": pd.date_range(start='1/1/2021', periods=num_rows, freq='D'),
        "ITEM CODE": [f'{randint(100000, 999999)}' for _ in range(num_rows)],  # 6-digit item codes
        "actual sales": [randint(1, 1000) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)
    

def search_and_download_datasets():
    search_term = input("Enter your search term (e.g., medical equipment sales): ")
    
    # Searching for datasets on Kaggle
    search_result = kaggle.api.dataset_list(search=search_term)
    
    if search_result:
        print("Datasets found:")
        i=0
        j=0
        for i, dataset in enumerate(search_result[:5]):  # Display first 5 datasets found
            print(f"{i+1}. {dataset.ref} - {dataset.title}")
            i=i+1
        
        j=i+1
        print(f"{j}. Download a custom dataset ")
            
        choice=input("Which dataset you want to download(enter the number)")
        choice =int(choice)
        
        if choice == j:
            fake_df= generate_custom_data(100)
            fake_df.to_csv('C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads/dataset.csv', index=False)     
            print("Custom dataset saved")
        else:

            dataset_to_download = search_result[choice-1].ref  
            kaggle.api.dataset_download_files(dataset_to_download, path='Downloads', unzip=True)
            print(f"Downloaded {dataset_to_download}")
#             # Example: Download the first dataset found (be mindful of the dataset size and terms)
    else:
        print("No datasets found. Try refining your search term.")
        print("Generaing a custom dataset")
        fake_df2= generate_custom_data(100)
        fake_df2.to_csv('C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads/dataset.csv', index=False)     
        print("dataset saved")


# handling multiple file 
def handle_multiple_files():
    import os
    import glob
    import pandas as pd  # Make sure to import pandas

    # Define a placeholder for the generate_custom_data function if it's not defined
    # You should replace this with your actual function definition
    def generate_custom_data(n):
        print(f"Generating a custom dataset with {n} entries.")

    downloads_folder = 'C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads'
    output_file_path = os.path.join(downloads_folder, "output.csv")  # It's good to specify the complete path including the file name for clarity

    files = glob.glob(os.path.join(downloads_folder, '*'))
    files = [f for f in files if os.path.isfile(f)]

    if len(files) == 0:
        print("The folder is empty.")
        generate_custom_data(100)
    elif len(files) == 1:
        print("There is a single file in the folder.")
    else:
        print(f"There are {len(files)} files in the folder.")
        all_files = glob.glob(os.path.join(downloads_folder, "*.csv"))

        li = []

        try:
            for filename in all_files:
                df = pd.read_csv(filename, index_col=None, header=0, sep=';')
                li.append(df)

            frame = pd.concat(li, axis=0, ignore_index=True)
            # Assuming you want to save the concatenated DataFrame to a file
            frame.to_csv(output_file_path, index=False, sep=';')
            print(f"All files have been concatenated into {output_file_path}.")
        except Exception as e:
            print("There are multiple datasets which cannot be concatenated into one due to the following error:", e)
            print("Generating custom dataset.")
            df=generate_custom_data(100)


#renaming it to test.csv

def renaming_to_test_file():
    # import os
    # import shutil

    # # Path to the Downloads directory where the file to rename is located
    # downloads_path = 'C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads'

    # # List all files in the Downloads directory
    # downloaded_files = os.listdir(downloads_path)

    # # Assuming there is only one file in the directory or you're only interested in the first .csv file
    # for file in downloaded_files:
    #     if file.endswith('.csv'):
    #         original_file_path = os.path.join(downloads_path, file)
    #         new_file_name = 'test.csv'
    #         new_file_path = os.path.join(downloads_path, new_file_name)
    #         try:
    #             # Rename the file
    #             os.rename(original_file_path, new_file_path)
    #             print(f"File {file} has been renamed to {new_file_name}")
    #             break  # If the renaming is done, exit the loop
    #         except FileNotFoundError:
    #             print(f"The file {original_file_path} does not exist.")
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #         break  # Exit the loop after trying to rename the first .csv file found
    # else:
    #     # If no .csv files were found in the loop
    #     print("No .csv files found in the directory.")

    import os

    # Path to the Downloads directory where the files to rename are located
    downloads_path = 'C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads'

    # List all files in the Downloads directory
    downloaded_files = os.listdir(downloads_path)

    # New file names we want to use if they're not already taken
    new_csv_file_name = 'test.csv'
    new_excel_file_name = 'test.xlsx'

    # Paths to the new files
    new_csv_file_path = os.path.join(downloads_path, new_csv_file_name)
    new_excel_file_path = os.path.join(downloads_path, new_excel_file_name)

    # Check if 'test.csv' already exists
    if os.path.exists(new_csv_file_path):
        print(f"A file named {new_csv_file_name} already exists.")
    else:
        # Rename the first .csv file found
        for file in downloaded_files:
            if file.endswith('.csv'):
                original_file_path = os.path.join(downloads_path, file)
                try:
                    os.rename(original_file_path, new_csv_file_path)
                    print(f"File {file} has been renamed to {new_csv_file_name}")
                    break
                except FileNotFoundError:
                    print(f"The file {original_file_path} does not exist.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                break

    # Now check if 'test.xlsx' already exists
    if os.path.exists(new_excel_file_path):
        print(f"A file named {new_excel_file_name} already exists.")
    else:
        # Rename the first .xls or .xlsx file found
        for file in downloaded_files:
            if file.endswith('.xls') or file.endswith('.xlsx'):
                original_file_path = os.path.join(downloads_path, file)
                try:
                    os.rename(original_file_path, new_excel_file_path)
                    print(f"File {file} has been renamed to {new_excel_file_name}")
                    break
                except FileNotFoundError:
                    print(f"The file {original_file_path} does not exist.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                break


#reading the test file
def reading_the_test_file():
#     def generate_custom_data(num_rows):
#         data = {
#             "DATE": pd.date_range(start='1/1/2021', periods=num_rows, freq='D'),
#             "ITEM CODE": [f'{randint(100000, 999999)}' for _ in range(num_rows)],  # 6-digit item codes
#             "actual sales": [randint(1, 1000) for _ in range(num_rows)]
#         }
#         return pd.DataFrame(data)

    # Define the path to the folder containing the files
    folder_path = 'C:/Users/proshan/OneDrive - SymphonyAI RETAIL CPG/Desktop/Projects/csv dataset generator/Downloads'

    # Define your custom function here (or make sure it's imported if defined elsewhere)


    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Check each file's extension and read it accordingly
    for file in files:
        try:  # Use a try block to catch any kind of error
            file_path = os.path.join(folder_path, file)
            if file.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path, encoding='utf-8')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='latin1')
                # Do something with the CSV file
            elif file.endswith('.xlsx'):
                df = pd.read_excel(file_path)
                # Do something with the Excel file
            else:
                print(f"Unsupported file format: {file}")
                print("Reading the test file which is generated")
        except Exception as e:  # Catch any other exception that occurs
            print(f"Reading the csv file generated")
            df=generate_custom_data(100)  # Call your custom error-handling function


def sales_column_check():

    if 'sales' in df.columns and 'price' in df.columns:
        df=df.drop('price',axis=1)




def nlp_tokenisation():
    
    import re

    def find_synonyms(words):
        synonyms = set()
        for word in words:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    # Add synonyms, replacing underscores with spaces
                    synonyms.add(lemma.name().replace('_', ' '))
        return synonyms

    # Find synonyms of "sale" and "price"
    words_to_find_synonyms_for = ["sale", "price"]
    combined_synonyms = find_synonyms(words_to_find_synonyms_for)

    # Ensure 'sales' is included in the synonyms
    combined_synonyms.add('sales')

    def is_related(column_name):
        # Define patterns to exclude specific column names
        excluded_patterns = [
            '^retail.*',  # Starts with 'retail'
            '^wholesale.*',  # Starts with 'wholesale'
            '.*_price$',  # Ends with '_price'
            # Additional patterns can be added as needed
        ]

        # Convert column name to lowercase and replace underscores with spaces
        column_name = column_name.lower().replace('_', ' ')

        # Check for excluded patterns first
        for pattern in excluded_patterns:
            if re.match(pattern, column_name):
                return False

        # Check if the column name contains terms or synonyms related to "sale" or "price"
        related_terms = ['sale', 'sales', 'price', 'amount'] + list(combined_synonyms)
        if any(term in column_name for term in related_terms):
            return True

        return False

    # Prepare the dictionary for renaming columns based on the related criteria
    columns_to_rename = {}
    for col in df.columns:
        if is_related(col):
            columns_to_rename[col] = 'actual sales'

    # Rename columns in the DataFrame as per the dictionary
    df.rename(columns=columns_to_rename, inplace=True)

    # Assuming you want to see the first few rows of the modified DataFrame
    print(df.head())

if __name__ == "__main__":
    search_and_download_datasets()
    handle_multiple_files()
    renaming_to_test_file()
    reading_the_test_file()
    sales_column_check()
    nlp_tokenisation()