import csv
import praw


reddit = praw.Reddit(client_id='EBohoWcmdN-cPi8HTOIUSw',
                     client_secret='tWUMO3InJO1KrY8d5iJ7DasBoUQy4w',
                     username="Automatic-Bid4538",
                     password="X890TNzsJj93",
                     user_agent="bda_sentimentv1")

subreddit = reddit.subreddit('RussiaUkraineWar2022')
# ukraine
# RussiaUkraineWar2022

hot_ukraine = subreddit.top(limit=1000)

with open('./ukraine_title_data.csv', 'w') as f:
    headers = ['ID', 'Date_utc', 'Title',
               'Number of Comments', 'Score', 'Author', 'Link', 'Flair']
    writer = csv.DictWriter(f, fieldnames=headers,
                            extrasaction='ignore', dialect='excel')
    writer.writeheader()
    for post in hot_ukraine:
        if not post.stickied:
            data = {
                'ID': post.id,
                'Date_utc': post.created_utc,
                'Title': post.title,
                'Number of Comments': post.num_comments,
                'Score': post.score,
                'Author': post.author,
                'Link': post.permalink,
                'Flair': post.link_flair_text

            }
            writer.writerow(data)
    f.close()
