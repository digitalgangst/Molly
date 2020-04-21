const TelegramBot = require("node-telegram-bot-api");
const { join } = require("path");
const glob = require("glob");
const Document = require("./domain/document");

require("dotenv").config();

const TOKEN = process.env.BOT_TOKEN;

const bot = new TelegramBot(TOKEN, { polling: true });

const COMMANDS = join(process.cwd(), "src", "commands", "*.command.js");

/*
    Command files
*/
glob(COMMANDS, (_, files) => {
    files.map((file) => {
        const func = require(file);
        const cmd = func(bot);
        bot.onText(cmd.pattern, cmd.command);
    });
});

/*
    Custom commands without onText trigger\
 */
bot.on("document", (msg) => {
    const message = new Document(msg);
    const { id } = msg.chat;
    bot.sendDocument(id, message.fileId, {
        parse_mode: "Markdown",
        caption: message.filename,
    });
});
