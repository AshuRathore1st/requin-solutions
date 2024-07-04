


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv(r"C:\Users\OM BANNA JI\Desktop\corona.csv")
df.head()


# In[4]:


# Count the occurrences of each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Create a pie chart
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()


# In[41]:


# Convert 'TweetAt' to datetime
df['TweetAt'] = pd.to_datetime(df['TweetAt'], format='%d-%m-%Y')

# Group by 'TweetAt' and 'Sentiment' and count occurrences
date_sentiment_counts = df.groupby(['TweetAt', 'Sentiment']).size().unstack().fillna(0)

# Plot the sentiment distribution over time as a stacked bar chart
date_sentiment_counts.plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Distribution of Sentiments Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
plt.show()

# Print the total number of each sentiment
total_sentiments = df['Sentiment'].value_counts()
print(total_sentiments)


# In[46]:


# Convert the 'TweetAt' column to datetime format
df['TweetAt'] = pd.to_datetime(df['TweetAt'], dayfirst=True)

# Create a complete date range from the earliest to the latest date in the data
date_range = pd.date_range(start=df['TweetAt'].min(), end=df['TweetAt'].max())

# Group the data by 'TweetAt' and 'Sentiment', and count the occurrences of each sentiment on each date
sentiment_counts = df.groupby(['TweetAt', 'Sentiment']).size().reset_index(name='Count')

# Pivot the data to create separate columns for each sentiment, ensuring all dates are included
pivoted_data = sentiment_counts.pivot(index='TweetAt', columns='Sentiment', values='Count').reindex(date_range).fillna(0)
pivoted_data.index.name = 'TweetAt'
pivoted_data = pivoted_data.reset_index()

# Create a line plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot and annotate each sentiment
sentiments = ['Extremely Negative', 'Negative', 'Neutral', 'Positive', 'Extremely Positive']
colors = ['red', 'orange', 'gray', 'skyblue', 'green']

for sentiment, color in zip(sentiments, colors):
    ax.plot(pivoted_data['TweetAt'], pivoted_data.get(sentiment, pd.Series(0, index=pivoted_data.index)), 
            label=sentiment, linestyle='-', color=color, linewidth=2)
    for i, j in zip(pivoted_data['TweetAt'], pivoted_data.get(sentiment, pd.Series(0, index=pivoted_data.index))):
        if j > 0:
            ax.annotate(str(int(j)), xy=(i, j), xytext=(-10, 10), textcoords='offset points', fontsize=10, color=color)

# Format the x-axis labels
date_formatter = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_formatter)

# Rotate the x-axis labels
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.2)  # Adjust bottom margin to fit rotated labels

# Set the title and labels
ax.set_title('Sentiment Distribution over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Count', fontsize=14)

# Legend with adjusted spacing and font size
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1))

# Grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Tight layout
plt.tight_layout()

# Show the plot
plt.show()


# In[44]:


# Convert the 'TweetAt' column to datetime format
df['TweetAt'] = pd.to_datetime(df['TweetAt'], dayfirst=True)

# Create a complete date range from the earliest to the latest date in the data
date_range = pd.date_range(start=df['TweetAt'].min(), end=df['TweetAt'].max())

# Group the data by 'TweetAt' and 'Sentiment', and count the occurrences of each sentiment on each date
sentiment_counts = df.groupby(['TweetAt', 'Sentiment']).size().reset_index(name='Count')

# Pivot the data to ensure all dates are included, even if there are no sentiments recorded
pivoted_data = sentiment_counts.pivot(index='TweetAt', columns='Sentiment', values='Count').reindex(date_range).fillna(0).reset_index().rename(columns={'index': 'TweetAt'})

# Print the total number of each sentiment on each date
for _, row in pivoted_data.iterrows():
    print(f"Date: {row['TweetAt'].strftime('%Y-%m-%d')}")
    for sentiment in pivoted_data.columns[1:]:
        print(f"  {sentiment}: {int(row[sentiment])}")
    print()


# In[50]:


# Convert 'TweetAt' to datetime
df['TweetAt'] = pd.to_datetime(df['TweetAt'], format='%d-%m-%Y')

# Count the number of tweets per day
tweets_per_day = df['TweetAt'].value_counts().sort_index()

# Plot the number of tweets over time
plt.figure(figsize=(14, 7))
tweets_per_day.plot(kind='line', marker='o', linestyle='-')
plt.title('Number of Tweets Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.grid(True)
plt.show()


# In[52]:


# Convert 'TweetAt' to datetime
df['TweetAt'] = pd.to_datetime(df['TweetAt'], format='%d-%m-%Y')

# Group by 'TweetAt' and 'Sentiment' and count occurrences
date_sentiment_counts = df.groupby(['TweetAt', 'Sentiment']).size().unstack().fillna(0)

# Find the maximum and minimum values for each sentiment along with dates
max_sentiment_counts = date_sentiment_counts.idxmax()
min_sentiment_counts = date_sentiment_counts.idxmin()

max_values = date_sentiment_counts.max()
min_values = date_sentiment_counts.min()

# Plot the maximum and minimum sentiment counts with dates
fig, ax = plt.subplots(figsize=(14, 7))

# Plotting maximum values
max_values.plot(kind='bar', color='lightgreen', ax=ax, position=0, width=0.4, label='Maximum Count')

# Annotate the maximum values with the corresponding dates
for i, v in enumerate(max_values):
    ax.text(i - 0.2, v + 10, f'{v}\n{max_sentiment_counts[i].date()}', color='black', ha='center')

# Plotting minimum values
min_values.plot(kind='bar', color='salmon', ax=ax, position=1, width=0.4, label='Minimum Count')

# Annotate the minimum values with the corresponding dates
for i, v in enumerate(min_values):
    ax.text(i + 0.2, v + 10, f'{v}\n{min_sentiment_counts[i].date()}', color='black', ha='center')

plt.title('Maximum and Minimum Sentiment Counts Over Time with Dates')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.legend()
plt.show()


# In[37]:


# Convert 'TweetAt' to datetime
df['TweetAt'] = pd.to_datetime(df['TweetAt'], format='%d-%m-%Y')

# Handle missing values in the 'Location' column
df = df.dropna(subset=['Location'])

# Group by 'Location' and 'Sentiment' and count occurrences
location_sentiment_counts = df.groupby(['Location', 'Sentiment']).size().unstack().fillna(0)

# Filter top locations by the total number of tweets
top_locations = location_sentiment_counts.sum(axis=1).sort_values(ascending=False).head(10).index
location_sentiment_counts_top = location_sentiment_counts.loc[top_locations]

# Plot sentiment distribution for top locations
location_sentiment_counts_top.plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Sentiment Analysis by Location (Top 10 Locations)')
plt.xlabel('Location')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
plt.show()

