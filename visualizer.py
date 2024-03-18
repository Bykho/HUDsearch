from dataLoader import load_excel_files

# Call the load_excel_files function with the folder path
folder_path = "/Users/nicobykhovsky/Desktop/HUDsearch/excelFiles"
combined_df = load_excel_files(folder_path)

# Now you can use the combined_df DataFrame for further processing
print(combined_df.head())  # For example, print the first few rows of the DataFrame
