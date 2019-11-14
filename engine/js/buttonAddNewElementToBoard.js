var counter = 0;

function agregarElemento(type, newGoal) {

    const fs = require('fs')

    try {
        var rawJson = fs.readFileSync('./engine/data/boardJson.json', 'utf8')
        console.log(rawJson)
    } catch (err) {
        console.error(err)
    }

    // rawJson = require("./boardJson.json");
    var boardJson = JSON.parse(rawJson);

    if (newGoal != "" && newGoal != null) {

        function add() {

            counter++;

            var content = '';

            content += '<li onclick="createPost(' + type + ', '+ counter +')><a><p>' + newGoal + '</p></a></li>\n';

            $('.grid-' + type + ' > ul').append(content);
        }


        if (data) {
            add();

            $('.grid-container').css('display', 'grid');

            $('.loading').css('display', 'none');
        }
        else {
            $('.loading').css('background-color', 'red');

            $('.loading span')
                .css('color', 'black')
            [0].innerHTML = "Cannot load data.json file!";
        }

        switch (type) {
            case "goals":
                boardJson.goals.push(newGoal);
                break;
            case "users":
                boardJson.users.push(newGoal);
                break;
            case "concepts":
                boardJson.concepts.push(newGoal);
                break;
            case "sources":
                boardJson.sources.push(newGoal);
                break;
            case "indicators":
                boardJson.indicators.push(newGoal);
                break;
            case "conceptGen":
                boardJson.conceptGen.push(newGoal);
                break;
            case "indicatorGen":
                boardJson.indicatorGen.push(newGoal);
                break;
            case "visualization":
                boardJson.visualization.push(newGoal);
                break;
            case "environment":
                boardJson.environment.push(newGoal);
                break;
        }

        console.log(boardJson);

        fs.writeFileSync('./engine/data/boardJson.json', JSON.stringify(boardJson), (err) => {
            if (err) console.log(err);
            console.log("Successfully Written to File.");
        });
    }


}