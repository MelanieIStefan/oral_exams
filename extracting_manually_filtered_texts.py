import pandas as pd

# import manually pre-filtered file; 
# it should have a column titled "Keep?" that has entries "yes" or "no", depending on whether researchers thought it should be included
# import .csv files (change file path as appropriat)
data_post_manual_filter = pd.read_csv("/home/melanie/Documents/oral_exams/data_combined_manually_filtered.csv")


# filter by whether to include the post
mask =   data_post_manual_filter["Keep?"].str.contains("yes")


included_data = data_post_manual_filter[mask]
included_quotes = data_post_manual_filter[mask].Body



# check that this worked, and count remaining rows
print(included_quotes.head())
print(str(len(included_quotes.index)))

# save to .txt file for thematic analysis

included_quotes.to_csv("data_for_thematic_analysis.txt",sep="\n")

included_data.to_csv("final_dataset.csv")



