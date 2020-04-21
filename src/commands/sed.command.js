module.exports = (bot) => ({
    pattern: /s\/(.*?)\/(.*?)\/?$/,
    command: (msg, match) => {
        const replyMsg = msg.reply_to_message;
        if (!replyMsg) {
            return;
        }
        const [, find, replace] = match;
        const { id } = msg.chat;
        const regex = new RegExp(find, "g");
        const newMessage = replyMsg.text.replace(regex, replace);
        const opts = {
            reply_to_message_id: replyMsg.message_id,
            parse_mode: "Markdown",
        };
        bot.sendMessage(id, `*Você quis dizer:*\n"${newMessage}"`, opts);
    },
});
