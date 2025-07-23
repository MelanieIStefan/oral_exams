import pandas as pd

# import manually pre-filtered file; 
# it should have a column titled "Keep?" that has entries "yes" or "no", depending on whether researchers thought it should be included
# import .csv files (change file path as appropriat)
data_post_manual_filter = pd.read_csv("/home/melanie/Documents/oral_exams/data_combined_manually_filtered.csv")

# filter by whether to include the post
mask =   data_post_manual_filter["Keep?"].str.contains("no")

print(sum(mask))

# included_quotes = data_post_manual_filter[mask]

# print(included_quotes.head())
# print(str(len(included_quotes.index)))


