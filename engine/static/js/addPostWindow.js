const electron = require('electron')
const path = require('path')
const url = require('url')
const BrowserWindow = electron.remote.BrowserWindow;

function createAddPostWindow () {
    addWindow = new BrowserWindow({
      width: 300,
      height: 200,
      title: 'Agrega un nuevo post:',
      "webPreferences":{
      "webSecurity":false
    }})
  
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, '../../templates/addWindow.html'),
        protocol:'file:',
        slashes: true
    }));
  

    addWindow.on('close', function(){
      addWindow = null;
  });
}