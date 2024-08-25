module.exports = {
  name: "Ping",
  description: "Pong!",
  // devOnly: Boolean,
  // testOnly: Boolean,
  // options: Object[],

  callback: (client, interaction) => {
    interaction.reply(`Pong! ${client.ws.ping}ms`);
  },
};
