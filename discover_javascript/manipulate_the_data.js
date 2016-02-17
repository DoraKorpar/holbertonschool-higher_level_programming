var https = require('https')
fs = require('fs')

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token b803a2d7adb8b4ff31d4e5a6789cdec0c32f63b7'
    }
};

var req = https.request(options, function(res) {
    streamToString(res, callback);
});

req.end();

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
        chunks.push(chunk);
    });
    stream.on('end', () => {
        cb(chunks.join(''));
    });
};

var callback = function(jsonString) {
    obj = JSON.parse(jsonString);
    for (i = 0; i < obj.items.length; i++) {
	console.log(obj.items[i].full_name);
    }
};


req.on('error', function(e) {
    console.error(e);
});
    
    
