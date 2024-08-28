# CelesteBot

A starry discord bot!

---

## Commands!

| Command      | Options                                                                                      | Description                                                    |
| ------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `/help`      | N/A                                                                                          | Replies with an embed containing commands and how to use them. |
| `/ping`      | N/A                                                                                          | Replies with `Pong!` and the ping duration in ms               |
| `/userinfo`  | \* `member` (required): Member to get information of                                         | Gets a members information                                     |
| `/kick`      | \* `member` (required): Member to kick <br/> \* `reason` (optional): Reason for kicking user | Kicks user from guild                                          |
| `/ban`       | \* `member` (required): Member to ban <br/> \* `reason` (optional): Reason for banning user  | Bans user from guild                                           |
| `/clear`     | \* `amount` (required): Number of messages to purge                                          | Clears a given number of messages from the channel             |
| `/loadcog`   | \* `cogname` (required): Name of the cog to load -> See `/help`                              | Loads a given cog (BOT OWNER ONLY)                             |
| `/unloadcog` | \* `cogname` (required): Name of the cog to unload -> See `/help`                            | Unloads a given cog (BOT OWNER ONLY)                           |

## Roadmap

- [ ] Fix `ping` command to return ping duration in ms
- [x] `clear` command to clear number of messages from discord chat
- [x] `userinfo` command to get a user's information
- [x] `help` command
- [x] Permission managing for each command
- [ ] User join guild event
- [x] OnReady event
- [ ] Media commands (play youtube audio, etc.)
- [x] Replace all replies with Embeds
