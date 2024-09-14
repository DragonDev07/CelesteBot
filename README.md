# CelesteBot

A starry discord bot!

---

## Commands!

### Developer Cog (Can Only be run by the bot owner)

| **Command**  | **Options**                                                       | **Description**                       |
| ------------ | ----------------------------------------------------------------- | ------------------------------------- |
| `/loadcog`   | \* `cogname` (required): Name of the cog to load -> See `/help`   | Loads a given cog                     |
| `/unloadcog` | \* `cogname` (required): Name of the cog to unload -> See `/help` | Unloads a given cog                   |
| `/reload`    | N/A                                                               | Re-Registers all application commands |

### Help Cog

| **Command** | **Options** | **Description**                                                |
| ----------- | ----------- | -------------------------------------------------------------- |
| `/help`     | N/A         | Replies with an embed containing commands and how to use them. |

### Media Cog

| **Command** | **Options**                                                 | **Description**                                                                 |
| ----------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `/join`     | N/A                                                         | Makes the bot join your current VC                                              |
| `/leave`    | N/A                                                         | Makes the bot leave its active VC                                               |
| `/volume`   | \* `volume` (optional): Percent to set volume to (eg. `50`) | Gets or sets the volume based on whether or not the `percent` value is provided |
| `/pause`    | N/A                                                         | Pauses currently playing audio                                                  |
| `/resume`   | N/A                                                         | Resumes audio                                                                   |
| `/skip`     | N/A                                                         | Skips to the next song in the queue                                             |
| `/stop`     | N/A                                                         | Stops any playing audio and clears the queue                                    |
| `/play`     | \* `url` (required): YouTube URL to play from               | Plays audio from a given YouTube URL                                            |

### Moderation Cog

| **Command** | **Options**                                                                                  | **Description**                                    |
| ----------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `/kick`     | \* `member` (required): Member to kick <br/> \* `reason` (optional): Reason for kicking user | Kicks user from guild                              |
| `/ban`      | \* `member` (required): Member to ban <br/> \* `reason` (optional): Reason for banning user  | Bans user from guild                               |
| `/clear`    | \* `amount` (required): Number of messages to purge                                          | Clears a given number of messages from the channel |

### Utility Cog

| **Command**   | **Options**                                          | **Description**                                  |
| ------------- | ---------------------------------------------------- | ------------------------------------------------ |
| `/userinfo`   | \* `member` (required): Member to get information of | Gets a members information                       |
| `/serverinfo` | N/A                                                  | Gets information about the server                |
| `/ping`       | N/A                                                  | Replies with `Pong!` and the bot's latency in ms |

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

- [x] Fix `ping` command to return ping duration in ms
- [x] User join guild event
- [x] Queueing for audio
- [x] `clear` command to clear number of messages from discord chat
- [x] `userinfo` command to get a user's information
- [x] `help` command
- [x] Permission managing for each command
- [x] OnReady event
- [x] Media commands (play youtube audio, etc.)
- [x] Replace all replies with Embeds
- [ ] Poll command
- [x] Fix logging to follow format of `[<TIME>] [Guild: <GUILD>]: <COG> - <COMMAND/EVENT> - <USER> - <OPTIONS>`
  - [ ] Make logging work with systemd
- [ ] Proper bot permissions
- [ ] Bot invite link
- [ ] `/queue` command to get media queue
- [ ] Update bot icon & make custom banner
- [ ] (maybe) Dynamically generate help command
- [ ] (maybe) Figure out a way to only register Developer commands in a specific server
