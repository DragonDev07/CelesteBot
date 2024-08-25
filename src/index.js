const { Client, GatewayIntentBits } = require("discord.js");
const { config } = require("dotenv");
const eventHandler = require("./handlers/eventHandler");

// Load `.env` variables
config();

// Declare bot client and intents
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

// Login with `TOKEN` value from `.env` file
client.login(process.env.TOKEN);

eventHandler(client);
