# LoL-Match-Scraper
This program allows one to pull data for one or many matches for League of Legends. This is useful for compiling stats for one's own games or for tournaments such as Penn State University's PSU LCS competition.
# Getting Started
First, you will need to grab an API key from the Riot Games Developer Portal.
Next, pull this repository into a folder.
Then, in that same folder, create a file named RIOT_API_KEY.txt and place your API key inside.
Run these commands in your terminal:
```
pip install riotwatcher
pip install pandas
```
Now all you have to do is create a file named urls.txt and place your match links inside.

# Step-By-Step Demonstration
1. Head over to https://developer.riotgames.com/ to get your key, you'll find it on a page that looks like this:
![image](https://user-images.githubusercontent.com/46391291/125374677-7e8fa300-e355-11eb-9c4f-fe753f5e73c3.png)

2. Create a folder and download main.py and place it inside, you can also create your RIOT_API_KEY.txt and urls.txt in this same folder:
3. Find the match(es) that you want to grab data for and place them inside urls.txt, one url per line:

