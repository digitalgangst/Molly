const sed = require("./commands/sed");
const onFire = require("./commands/on-fire");
const echo = require("./commands/echo");
const TelegramBot = require("node-telegram-bot-api");
require("dotenv").config();

const TOKEN = process.env.BOT_TOKEN;

const bot = new TelegramBot(TOKEN, { polling: true });

// on text event trigger
[sed, onFire, echo].forEach((x) => {
  const cmd = x(bot);
  bot.onText(cmd.pattern, cmd.command);
});
