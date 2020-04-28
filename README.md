# Boon
<p align="center">
  <img width="600" height="758" src="https://i.imgur.com/RttMDJG.png">
</p>

## Program Description
A customizable Discord bot which interacts with single-target user mentions.

## Setup
### Dependencies 
- Python 3.8
- discord.py

### Steps
* Extract the files from this repository into some directory on your desktop
* Head over to the **Developer Portal** at <tt>https://discordapp.com/developers</tt> and sign in
* In **Applications**, create a **New Application** for your boon and select the application box
* Under **OAuth2 > SCOPES**, check off <tt>bot</tt>, then below, give it the permissions <tt>Send Messages</tt> and <tt>View Channels</tt>
* Copy the new URL right under **SCOPES**, paste it into your browser, select the servers for your boon to join
* **Substitute for <tt>token.txt</tt>:** under **Bot > Build-A-Bot**, copy your token and substitute the first line in the file with it
* **Customize your <tt>allowed_channels.txt</tt>:** head to a desired channel on the server, **Right-click > Copy ID** and paste the number into the file with each channel ID on separate lines (follow my example channel IDs!)
* **Customize your <tt>mentions_boon.txt</tt>:** each line will represent a different response from your boon for mentioning it
* **Customize your <tt>mentions_other.txt</tt>:** each line will represent a different response from your boon for mentioning other users
* Run your downloaded **<tt>boon.py</tt>**; for as long as the script is running, the bot will stay online and functional

**Note:** if you update any .txt file during runtime, you may have to restart the Python script in order to push changes!

## Changelog

(April 28, 2020)
* Released Boon-v1.0
