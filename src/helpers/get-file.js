const fs = require("fs");
module.exports = (file, parse = true) =>
    parse
        ? JSON.parse(fs.readFileSync(file, { encoding: "utf-8" }))
        : fs.readFileSync(file, { encoding: "utf-8" });
