const gif = "https://media0.giphy.com/media/xTiTnoHt2NwerFMsCI/giphy.gif";

module.exports = (bot) => ({
  pattern: /\/onfire (.+)/,
  command: (msg, match) => {
    const [, user] = match;
    const { id } = msg.chat;
    bot.sendMessage(id, `${user} *IS ON FIRE !!!*`, {
      parse_mode: "Markdown",
    });
    bot.sendDocument(id, gif);
  },
});
