const electron = require('electron');
const {ipcRenderer} = electron;

function createPost(){
ipcRenderer.send('createPost');
}

// function sendAddWindowData(type, item)