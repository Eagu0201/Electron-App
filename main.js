const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')
const fs = require('fs')

function createWindow () {
    window = new BrowserWindow({width: 1400, height: 1000, "webPreferences":{
      "webSecurity":false
    }})
    window.loadFile('index.html')

  var pyshell =  require('python-shell');
  pyshell.run('./engine/hello.py', {args: ['4']},  function  (err, results)  {
   if  (err)  console.log(err);
  });  	
    
}



app.on('ready', createWindow)

app.on('window-all-closed', () => {
  fs.writeFileSync('./engine/static/data/boardJson.json', fs.readFileSync('./engine/static/data/boardJsonBlank.json', 'utf8'), (err) => {
    if (err) console.log(err);
  }); 
    if (process.platform !== 'darwin') {
      app.quit()
    }
})

