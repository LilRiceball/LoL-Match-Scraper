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

2. Create a folder and download main.py and place it inside.
3. Create your RIOT_API_KEY.txt and urls.txt in this same folder, place your API key inside RIOT_API_KEY.txt.
4. Find the match(es) that you want to grab data for and place them inside urls.txt, one url per line:
![image](https://user-images.githubusercontent.com/46391291/125381059-41c9a900-e361-11eb-97b4-c9b359305fe6.png)
![image](https://user-images.githubusercontent.com/46391291/125381133-5f970e00-e361-11eb-80f9-71ef307bd89f.png)
![image](https://user-images.githubusercontent.com/46391291/125381054-3d04f500-e361-11eb-8ebd-78a5c90e2915.png)

4. Now, just run main.py and output.csv will be created with the requested information. This can be opened with your preferred program such as Excel or Google Sheets:
![image](https://user-images.githubusercontent.com/46391291/125381523-0ed3e500-e362-11eb-9362-bce6b9cda773.png)
# Uses For This Program
This allows you to gather interesting information for competitions, such as PSU LCS, and display the data in a fun way for players to see:
![image](https://user-images.githubusercontent.com/46391291/125382327-7dfe0900-e363-11eb-8bdb-2d18a3e3703e.png)
# Future Updates
This can be further updated by including other data such as objective damage, turret damage, dragon and baron kill counts, and game time just to name a few.
