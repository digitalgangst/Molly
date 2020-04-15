const ytdl = require('ytdl-core');
const fs = require('fs');

module.exports = (bot) => ({
    pattern: /\/ytconvert (.+)/,
    command: async (msg, match) => {
      const [, ytlink] = match;
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
     
      stream.pipe(filestream);
      bot.sendMessage(id, `Video: ${title}\nDownloading...`);
      stream.on('end', () => {
            bot.sendAudio(id, filename, {}, fileOptions);
            fs.unlinkSync(filename);
      });

    },
  });
  