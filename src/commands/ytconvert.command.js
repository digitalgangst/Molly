const ytdl = require('ytdl-core');
const fs = require('fs');

module.exports = (bot) => ({
    pattern: /\/ytconvert (.+)/,
    command: async (msg, match) => {
      const [, ytlink] = match;
      const {message_id} = msg;
      const { id } = msg.chat;

      const songInfo = await  ytdl.getInfo(ytlink, {downloadURL: true});
      const {video_id, title} = songInfo;
      const filestream = fs.createWriteStream(`${video_id}.mp3`);
      const filename = filestream.path;
      const stream = ytdl.downloadFromInfo(songInfo, {filter: "audioonly"});
      const fileOptions = {
        // Explicitly specify the file name.
        filename: `${title}.mp3`,
        // Explicitly specify the MIME type.
        contentType: 'audio/mpeg',
        
      };
      const replyMsgOption = {
        reply_to_message_id: message_id,
        parse_mode: "Markdown",
      };
      stream.pipe(filestream);
      bot.sendMessage(id, `\`${title}\` foi adicionado a lista de downloads...\n`, replyMsgOption);
      stream.on('end', () => {
            bot.sendAudio(id, filename, replyMsgOption, fileOptions);
            fs.unlinkSync(filename);
      });

    },
  });
  