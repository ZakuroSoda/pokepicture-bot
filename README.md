## PokePicture-Bot
This is a discord bot supplying pictures of pokemon on request. <br><br>
<img src="https://img.shields.io/badge/Status-Completed-green">
<img src="https://img.shields.io/badge/Hosted%20on-Heroku-blueviolet">
<img src="https://img.shields.io/badge/Language-Python%203.10.0-yellow">

### Usage in Discord:

`!help` <br>
`![pokemonname]`

### Example Usage

<img src="/assets/help.png">
<br><br>
<img src="/assets/pikachu.png">

---

### How to Set Up

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on `create new application`
3. Give it a name
4. Go to `bot > add bot`
5. Press `reset token > show token`
6. Copy the token and paste in `token` variable in `main.py`
7. Navigate back to `OAuth2 > URL Generator`
8. Tick `bot > check all text permissions`
9. Open the generated URL and invite the bot to your server.

### How to Host on Heroku

1. Make sure `Procfile`, `main.py`, and `requirements.txt` are in the same directory.
2. Make sure `git` and `heroku cli` are downloaded.
3. Go to [Heroku Website](https://dashboard.heroku.com/) and create a new project.
4. Go to that `project > settings > buildpacks > add buildpacks > python`.
5. Navigate to your project folder in your shell `cd [path]`
6. Run `heroku login` and follow login steps
7. Run `heroku git:remote -a [NAME_OF_YOUR_HEROKU_APP]`
8. Run `git add .`
9. Run `git commit -m "Deployment commit"`
10. Run `git push heroku master`
11. Run `heroku ps:scale worker=1`

The Discord Bot should be online and running!

To troubleshoot, use `heroku logs --tail`

---

### Reflection

This project was more of a proof-of-concept kind of thing, for me to learn how to host a script online.

The python bot is really simple using just `requests` to call the PokeAPI and the standard `discord` library for interacting with the bot.

This was very fun because I learnt how to host ascript on my own!

<img src="https://1.bp.blogspot.com/-EHBItm2ov28/X7zMLiDUlnI/AAAAAAABcZg/Hn1EagLhVecSENp47dA46nL8wXAP4iChQCNcBGAsYHQ/s400/sweets_tarte_strawberry.png" width=100px>
Here's a strawberry tart!
