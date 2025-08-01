import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as col
from textblob_de import TextBlobDE as TextBlob
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


import nltk

nltk.download('stopwords')



# import data file
# import .csv files (change file path as appropriat)
final_dataset = pd.read_csv("/home/melanie/Documents/oral_exams/final_dataset.csv")
total_length = len(final_dataset.index)

print(final_dataset.head())

# define my colour scheme (same as for my entire thesis)
fullcolors = ['#008ac5', '#dc0a2e', '#04a777','#f9e900', '#3d2b3d']
pastelcolors = ['#c2edff', '#fcc5ce', '#c3fdec', '#fffbc2','#e6dbe6']

# # count posts per subreddit
medizinstudium =   sum(final_dataset["Subreddit"].str.contains("Medizinstudium"))

medizin = total_length - medizinstudium

values = [medizin, medizinstudium]
names = 'r/Medizin', 'r/Medizinstudium'

plt.pie(values, labels = names,  wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=pastelcolors, autopct='%1.1f%%');

# plt.show();

plt.savefig("subreddit.png")

plt.close()

# count submissions  vs comments


posts =   sum(final_dataset["Type"].str.contains("submission"))
comments = total_length-posts 


values = [posts, comments]
names = 'Post', 'Kommentar'

plt.pie(values, labels = names,  wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, colors=pastelcolors, autopct='%1.1f%%');

# plt.show();

plt.savefig("type.png")

plt.close()



# count contributions per user 


contributionsPerAuthor = Counter(final_dataset["Author"])

print(contributionsPerAuthor)

contributions = list(contributionsPerAuthor.values())

plt.hist(contributions, color=fullcolors[0], align='left')
plt.xlabel('Beiträge pro User*in')
plt.savefig("beitraege_pro_person.png")
plt.close()



# word cloud


allPosts = "".join(final_dataset["Body"]) 


# exclude stop words
stopWords = set(stopwords.words('german'))

# Remove stopwords
posts = word_tokenize(allPosts)
filteredPosts = " ".join([word for word in posts if word not in stopWords])


print(filteredPosts)

# wordcloud = WordCloud(width=480, height=480, margin=0, background_color='white').generate(filteredPosts)

cmap = col.ListedColormap(fullcolors)
wordcloud = WordCloud(width=480, height=480, margin=0, background_color='white', colormap=cmap, max_words=50).generate(filteredPosts)


# plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.savefig("wortwolke.png")
plt.close()







# Sentiment analysis


polarities = ["NA"] * len(final_dataset.index)


for i in range(0,len(final_dataset)):
    blob = TextBlob(final_dataset.Body[i])
    polarities[i] =  blob.sentiment.polarity #11
    
final_dataset ['polarity'] = polarities


print(final_dataset.head())



stimmung = sns.boxplot(y='polarity', data=final_dataset, color=fullcolors[0], widths=0.5)
 
# Add jitter with the swarmplot function
stimmung = sns.swarmplot(y='polarity', data=final_dataset, color=fullcolors[4])


plt.ylabel('Stimmung')
plt.savefig("stimmung.png")



# Useful resources
# https://machine-learning-blog.de/2019/06/03/stimmungsanalyse-sentiment-analysis-auf-deutsch-mit-python/
# https://stackoverflow.com/questions/79113723/textblob-de-missing-deprecated-module-textblob-translatepo
# https://python-graph-gallery.com/#
# https://pythonexamples.org/python-matplotlib-pie-chart-show-percentage/
# https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item#comment55095870_23909767
# https://stackoverflow.com/questions/23246125/how-to-center-labels-in-histogram-plot
# https://www.geeksforgeeks.org/nlp/removing-stop-words-nltk-python/
# cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
