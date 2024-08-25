import { Client, GatewayIntentBits } from "discord.js";
import { config } from "dotenv";

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

// Log when bot is online
client.on("ready", (c) => {
  console.log(`${c.user.tag} is now online.`);
});
