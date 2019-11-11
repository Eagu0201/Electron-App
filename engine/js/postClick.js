const electron = require('electron');
const {ipcRenderer} = electron;

function postClick(type){
    ipcRenderer.send('postClick', type);
}

// function sendAddWindowData(type, item)