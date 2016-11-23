# SongRequests

A sample project using Revlo's API to trigger Nightbot's !songs command.

## Install Instructions

* Open your terminal or Powershell and clone the project
```
git clone git://github.com/teamrevlo/revlo_client.git
```
* Retrieve your Revlo API Key by going to [Revlo](https://revlo.co) Dashboard > Settings > API Key
* Find the reward\_id that belongs to your song request.
```
curl -H "--x-api-key: $REVLO_API_KEY" https://api.revlo.co/1/rewards
```
* Deploy [Nightbot](https://beta.nightbot.tv) on your channel.
* Enable the `!songs` command on Nightbot
* Retrieve your OAuth token. You can generate one with [Twitch](https://twitchapps.com/).
* Make a copy of config.sample.ini in the same folder with the filename `config.ini`. Your config.ini file should look something like this:
```
[revlo]
api_key=$REVLO_API_KEY
reward_id=$SONG_REQUEST_REWARD_ID

[twitch]
password=oauth:$OAUTH_TOKEN
channel=$YOUR_TWITCH_USERNAME
username=$YOUR_TWITCH_USERNAME
server=irc.chat.twitch.tv
port=6667
```

## Run instructions

* In your Terminal/Powershell, enter this command
```
cd revlo_client/examples/songrequests
python song_requests.py
```
