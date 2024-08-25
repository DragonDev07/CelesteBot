module.exports = {
  data: {
    name: "help",
    description: "Prints information about bot commands",
  },

  run: ({ interaction, client }) => {
    interaction.reply("This command is not ready yet!");
  },
};
