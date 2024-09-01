# CelesteBot

A starry discord bot!

---

## Commands!

| Command      | Options                                                                                      | Description                                                                     |
| ------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `/help`      | N/A                                                                                          | Replies with an embed containing commands and how to use them.                  |
| `/ping`      | N/A                                                                                          | Replies with `Pong!` and the ping duration in ms                                |
| `/userinfo`  | \* `member` (required): Member to get information of                                         | Gets a members information                                                      |
| `/kick`      | \* `member` (required): Member to kick <br/> \* `reason` (optional): Reason for kicking user | Kicks user from guild                                                           |
| `/ban`       | \* `member` (required): Member to ban <br/> \* `reason` (optional): Reason for banning user  | Bans user from guild                                                            |
| `/clear`     | \* `amount` (required): Number of messages to purge                                          | Clears a given number of messages from the channel                              |
| `/loadcog`   | \* `cogname` (required): Name of the cog to load -> See `/help`                              | Loads a given cog (BOT OWNER ONLY)                                              |
| `/unloadcog` | \* `cogname` (required): Name of the cog to unload -> See `/help`                            | Unloads a given cog (BOT OWNER ONLY)                                            |
| `/volume`    | \* `volume` (optional): Percent to set volume to (eg. `50`)                                  | Gets or sets the volume based on whether or not the `percent` value is provided |
| `/play`      | \* `url` (required): YouTube URL to play from                                                | Plays audio from a given YouTube URL                                            |
| `/reload`    | N/A                                                                                          | Re-Registers all application commands                                           |
| `/join`      | N/A                                                                                          | Makes the bot join your current VC                                              |
| `/leave`     | N/A                                                                                          | Makes the bot leave its active VC                                               |
| `/pause`     | N/A                                                                                          | Pauses currently playing audio                                                  |
| `/resume`    | N/A                                                                                          | Resumes audio                                                                   |
| `/skip`      | N/A                                                                                          | Skips to the next song in the queue                                             |
| `/stop`      | N/A                                                                                          | Stops any playing audio and clears the queue                                    |

## Usage

### Add to Your Server

- Coming soon, dont have hosting.

### Running Yourself

1. Clone the repository & Enter the directory:

```
git clone https://github.com/DragonDev07/CelesteBot/
cd CelesteBot
```

2. Install all python requirements

```
pip install -r requirements.txt
```

3. Put your token in a .env file, like so:

```
TOKEN = <YOUR TOKEN HERE>
```

4. Run `main.py`!

```
python main.py
```

## Roadmap

- [ ] Fix `ping` command to return ping duration in ms
- [ ] User join guild event
- [ ] Queueing for audio
- [x] `clear` command to clear number of messages from discord chat
- [x] `userinfo` command to get a user's information
- [x] `help` command
- [x] Permission managing for each command
- [x] OnReady event
- [x] Media commands (play youtube audio, etc.)
- [x] Replace all replies with Embeds
