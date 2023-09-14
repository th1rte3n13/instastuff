import instaloader

L = instaloader.Instaloader()

username = ''
passwd = ''

L.context.username = username
L.context.password = passwd
L.context.login(username, passwd)

profile_name = 'profile_name'
profile = instaloader.Profile.from_username(L.context, profile_name)

for post in profile.get_posts():
    L.download_post(post, target=f"{profile_name}")
