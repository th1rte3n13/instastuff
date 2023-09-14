import requests

url = "https://instagram-data1.p.rapidapi.com/hashtag/feed/reels"

querystring = {"hashtag":"python"}

headers = {
	"X-RapidAPI-Key": "85a8907e00msh53935433004c404p11793fjsn11c4a87c2534",
	"X-RapidAPI-Host": "instagram-data1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)