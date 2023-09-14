import instaloader
from datetime import datetime, timedelta

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Define the start and end date for the week
end_date = datetime.now().date()
start_date = end_date - timedelta(days=7)

# Define a list to store the posts and their like counts
most_liked_posts = []

# Iterate over the posts from the past week and add them to the list
for post in L.get_hashtag_posts('week'):
    post_date = datetime.fromtimestamp(post.date).date()
    if post_date >= start_date and post_date <= end_date:
        most_liked_posts.append((post, post.likes))

# Sort the list in descending order of like count and print the top 10 most liked posts
most_liked_posts.sort(key=lambda x: x[1], reverse=True)
print("Top 10 Most Liked Posts of the Week:")
for i, (post, likes) in enumerate(most_liked_posts[:10]):
    print(f"{i+1}. {post.owner_username}: {post.caption} ({likes} likes)")