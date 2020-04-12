module.exports = (bot) => ({
  pattern: /\/echo (.+)/,
  command: (msg, match) => {
    const { id } = msg.chat;
    const [, echo] = match;
    bot.sendMessage(id, echo);
  },
});
