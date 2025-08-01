Discourse analysis of reddit posts to learn about students' experience with oral examinations in their medical degree

Files:

data_gathering.py: Uses Reddit API to gather data from specific subreddits: Gather all posts containing keywords from a list of keywords, and all comments relating to those posts

data_preparation.py: Filter out incomplete entries, use key words to only retain relevant comments

extracting_manually_filtered_texts.py: This step is for *after* manual inspection of the dataset. The idea is that the person inspecting the data set added a column called "Keep?" with yes/no entries. This script extracts the content of included posts and comments into a text file that can be used for thematic analysis.

summarise_data.py: Summary stats, word cloud and sentiment analysis
