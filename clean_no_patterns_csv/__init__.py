import pandas as pd

# Read the CSV file
csv_file_path = 'csv_file.csv'
data_frame = pd.read_csv(csv_file_path, header=None)

# Numeric index of the column to be modified
column_to_modify_index = 3  # Change this to the correct numeric index

# tags to remove
words_to_remove =  ['GmbH', 'gmbh','Multi', 'Social',
                        'Wertschöpfung mit Google Ads',
                        'The Social First Agency', 'Wertschöpfung mit Google Ads'
                        'App Marketing Experts','Pay-Per-Performance Paid',
                        "we're hiring!", 'Ihr', 'Partner'
                        'BRAND AGENCY', 'Advertising',
                        'Gesellschaft', 'Markenerlebnisse', 'mbH',
                        'Media', ' Influencer', 'influencer marketing platform',
                        ' Agency', ' Marketing', ' &','  &',
                        'Agentur', 'für', ' Kreativagentur'
                        ' E-Commerce', ' International', 
                        'AG', 'Group', 'Hamburg', 
                        ' Consulting', ' Creative', ' Communications',
                        'Online', 'Amazon', 'PPC', 'Tool',
                        'Webdesign', 'SEO', 'Agentur', 'Sprache',
                        'Digital', 'Desk', ' - ', ' -', ' / ',
                        'Online', 'App', 'Experts', '--'
                        ' | ', ' |','Growth Consultancy', 'We are hiring!',
                        '& CO KG', 'Creative', '& Event',
                        'Pay-Per-Performance Paid Social', ' Communication', ':',
                        '& Co. KG', 'Full Service  in Essen', 'Pahnke und Schwieger']

# Function to remove words from a string
def clean_value(string):
    for word in words_to_remove:
        string = string.replace(word, '')
    return string.strip()

# Apply the function to the specified column by its index
data_frame.iloc[:, column_to_modify_index] = data_frame.iloc[:, column_to_modify_index].apply(clean_value)

# Save the modified file
modified_file_path = 'modified_file.csv'
data_frame.to_csv(modified_file_path, index=False)
