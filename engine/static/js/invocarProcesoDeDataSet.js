var automl_result = `{`;
var counter = 0;
var score_helper = ``;
const pyshell = require("python-shell");

async function readJson(){
    const fs = require('fs')

    try {
        var rawJson = fs.readFileSync('./engine/static/data/boardJson.json', 'utf8')
        console.log(rawJson)
    } catch (err) {
        console.error(err)
    }
    return rawJson;
}

async function convertJsonToCSV(){
    var rawJson = await readJson();
    var dataProcess = new pyshell('./engine/dataProcess.py', { args: [rawJson] }, function (err, results) {
        if (err) console.log(err);
    });

    dataProcess.on('message', function (message) {
        console.log(message);
    })
}


async function processDataset(){
    const fs = require('fs');
    await convertJsonToCSV();

    setTimeout(() => { try {
        var dataSet = fs.readFileSync('./datasets/empty.csv', 'utf8');
        console.log(dataSet);
    
        var summon_autoML = new pyshell('./engine/summon_autoML.py', { args: [dataSet] }, function (err, results) {
            if (err) console.log(err);
        });

        summon_autoML.on('message', function (message) {
            counter ++;
            console.log(message);
            console.log(counter);
            
            
            if ((counter == 3) || (counter == 9) || (counter == 15) || (counter == 21) || (counter == 27) || (counter == 33) || (counter == 39))
            score_helper = message.replace(/\D/g,'');
            if ((counter == 5) || (counter == 11) || (counter == 17) || (counter == 23) || (counter == 29) || (counter == 35)){
                var subString = message.substring(
                message.lastIndexOf(":") + 2
                );
                automl_result = automl_result + subString + `: "` + score_helper + `", `;
            }
            if (counter == 41){
                var subString = message.substring(
                message.lastIndexOf(":") + 2
                );
            automl_result = automl_result + subString + `: "` + score_helper + `"}`;
                }
        });
        
        summon_autoML.on('close', function (results) {
            console.log(automl_result);
            sendOutputToExcel(automl_result);
        });
        

    } catch (err) {
        console.error(err)
    }}, 2600);

}

    async function sendOutputToExcel(automl_result){
        setTimeout(() => {
        
        var pipExcel = new pyshell('./engine/pipExcel.py', { args: [automl_result] }, function (err, results) {
            if (err) console.log(err);
        });
    
        pipExcel.on('message', function (message) {
            console.log(message);

        });
    }, 3000);
}
