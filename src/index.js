const { Client, GatewayIntentBits } = require("discord.js");
const { config } = require("dotenv");
const { CommandKit } = require("commandkit");
const path = require("path");

// Load all variables from `.env` file
config();

// Declare discord bot client
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildMessages,
  ],
});

new CommandKit({
  client,
  commandsPath: path.join(__dirname, "commands"),
  eventsPath: path.join(__dirname, "events"),
  devGuildIds: ["1041478593257160744"],
  devUserIds: ["635175805261054004"],
  bulkRegister: true,
});

// Log client in with `TOKEN` value from `.env` file
client.login(process.env.TOKEN);
