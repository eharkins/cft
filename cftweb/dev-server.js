var path = require("path");
var express = require("express");
var webpack = require("webpack");
/* very hacky way of passing arguments to webpack.config.dev.js */
global.dataLocal = process.argv.indexOf("local") !== -1 ? true : false;
var config = require("./webpack.config.dev");
var request = require("request");

var app = express();
var compiler = webpack(config);

app.set('port', 4000);

app.use('/data', express.static('data'))

app.use(require("webpack-dev-middleware")(compiler, {
  noInfo: true,
  publicPath: config.output.publicPath
}));

app.use(require("webpack-hot-middleware")(compiler));

app.get("/favicon.png", function(req, res) {
  res.sendFile(path.join(__dirname, "favicon.png"));
});

app.get("*", function(req, res) {
  res.sendFile(path.join(__dirname, "auspice/index.html"));
});

// Listen for requests
var server = app.listen(app.get('port'), function() {
  var port = server.address().port;
  console.log('Listening on port ' + port);
});
