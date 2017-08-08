// Dump the web page at the given URL
// We use phantomjs to evaluate JS before dumping the content

var system = require('system');
var webpage = require('webpage');

if (system.args.length !== 2) {
    console.log('Usage: phantomjs scrape.js <URL>');
    phantom.exit(1);
}
var url = system.args[1];

var page = webpage.create();
page.open(url, function () {
    console.log(page.content);
    phantom.exit();
});
// Ignore errors - PhantomJS will just output a blank webpage

