module.exports = (bot) => ({
    pattern: /.*teste?/,
    command: (msg) => {
        const replyMsg = msg.message_id;
        if (!replyMsg) {
            return;
        }
        const { id } = msg.chat;
        bot.sendDocument(id, "./data/gif.gif", {
            reply_to_message_id: replyMsg,
            parse_mode: "Markdown",
        });
    },
});
