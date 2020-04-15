process.env.NTBA_FIX_319 = 1;
const TelegramBot = require("node-telegram-bot-api");
const fs = require('fs');
const glob = require('glob');
require("dotenv").config();

const TOKEN = process.env.BOT_TOKEN;

const bot = new TelegramBot(TOKEN, { polling: true });

options = {
  cwd: 'src/commands'
};

glob("*.command.js", options, (err, files) => {
  if(err) throw new Error(err);
  files.map(file => {
    const func = require(`./commands/${file}`);
    const cmd = func(bot);
    bot.onText(cmd.pattern, cmd.command);
  });
});

