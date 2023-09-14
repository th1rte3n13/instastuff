import instaloader
from datetime import datetime, timedelta

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Define the start and end date for trending posts
end_date = datetime.now().date()
start_date = end_date - timedelta(days=7)

# Define a dictionary to store the post count for each hashtag
trending_posts = {}

# Iterate over the posts with the hashtag of the week and increment the count in the dictionary
for post in L.get_hashtag_posts('week'):
    post_date = datetime.fromtimestamp(post.date).date()
    if post_date >= start_date and post_date <= end_date:
        for hashtag in post.caption_hashtags:
            if hashtag in trending_posts:
                trending_posts[hashtag] += 1
            else:
                trending_posts[hashtag] = 1

# Sort the dictionary in descending order of count and print the top 10 trending hashtags
trending_posts = {k: v for k, v in sorted(trending_posts.items(), key=lambda item: item[1], reverse=True)}
print("Top 10 Trending Hashtags of the Week:")
for i, (hashtag, count) in enumerate(trending_posts.items()):
    if i < 10:
        print(f"{i+1}. {hashtag}: {count}")
    else:
        break