
import pandas as pd
import os

def load_excel_files(folder_path):
    """
    Load all Excel files from a folder into a single DataFrame.

    Parameters:
    folder_path (str): Path to the folder containing Excel files.

    Returns:
    pandas.DataFrame: Concatenated DataFrame containing data from all Excel files.
    """
    # Initialize an empty list to store DataFrames
    dfs = []
    
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file in files:
        # Check if the file is an Excel file
        if file.endswith('.xlsx') or file.endswith('.xls'):
            # Construct the full file path
            file_path = os.path.join(folder_path, file)
            # Load Excel file into a DataFrame
            df = pd.read_excel(file_path)
            # Append the DataFrame to the list
            dfs.append(df)
    
    # Concatenate all DataFrames in the list into a single DataFrame
    concatenated_df = pd.concat(dfs, ignore_index=True)
    
    return concatenated_df

# Example usage:
folder_path = "/Users/nicobykhovsky/Desktop/HUDsearch/excelFiles"
combined_df = load_excel_files(folder_path)
