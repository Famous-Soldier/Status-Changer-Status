import requests, time

# Famous Soldier | https://github.com/Famous-Soldier

token = ""
u_header = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

red = "dnd" # Red
idle = "idle" # idle
green = "online" # Green
offline = "invisible"


requests.patch('https://discord.com/api/v8/users/@me/settings', headers=u_header, json={"status":green})













