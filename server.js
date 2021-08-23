//For express, we need:
//npm init
//npm install express

//Part1: Express Web Server
var express = require('express');
var app = express();
var port = 3000;
app.listen(port, function () {
    console.log(`server running on http://localhost:${port}`);
    console.log(`Try Getting Aggregated COVID19 data at http://localhost:${port}/covid_19_timeseries?numberOfCountries=3&aggregationInterval=W`);
})
//Part2: Express Get Request for Covid-19 Time Series data
app.get('/covid_19_timeseries', function (req, res) {
    var spawn = require('child_process').spawn;
    var process = spawn('python', ['./covid19aggregator.py',
        req.query.numberOfCountries,  // for example ~ 3
        req.query.aggregationInterval // for example ~ W for Week
    ]
    );
    process.stdout.on('data', function (data) {
        res.send(data.toString());
    });
});