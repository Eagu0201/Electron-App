const {app, BrowserWindow, ipcMain} = require('electron')
const path = require('path')
const url = require('url')
const fs = require('fs')


function createWindow () {
    window = new BrowserWindow({width: 1400, height: 1000, 
      title: 'Main Menu', 
      "webPreferences":{
      "webSecurity":false
    }})
    window.loadFile('index.html')

}

function createBoardWindow () {
  boardWindow = new BrowserWindow({width: 1400, height: 1000, 
    title: 'Databoard', 
    "webPreferences":{
    "webSecurity":false
  }})
  boardWindow.loadFile('./engine/templates/hello2.html');

  boardWindow.on('close', function(){
    app.quit()
});
}

function inyectarDatosEdit(type, postNum){
  //Buscar en JSON por ID del req, leerlo e inyectar los datos en el HTML.
  document.getElementById(postNum).value = count();

}


ipcMain.on('goToDataboard', function(){
  createBoardWindow();
  window.close();
});

ipcMain.on('createPost', function(){
  createAddPostWindow();
});

ipcMain.on('addPost', function(e, requirement){
  boardWindow.webContents.send('addPost', requirement);
  addWindow.close();
});

ipcMain.on('postClick', function(type, postNum){
  editPostWindow(type, postNum);
});


function createAddPostWindow () {
  addWindow = new BrowserWindow({
    width: 500,
    height: 350,
    title: 'Agrega un nuevo post',
    "webPreferences":{
    "webSecurity":false
  }})

  addWindow.loadFile(`./engine/templates/addWindow.html`);

  addWindow.on('close', function(){
    addWindow = null;
});
}

function editPostWindow (type, postNum) {
  editWindow = new BrowserWindow({
    width: 500,
    height: 350,
    title: 'Editar este post',
    "webPreferences":{
    "webSecurity":false
  }})

  editWindow.loadFile(`./engine/templates/addWindow.html?type=${type}&postNum=${postNum}`)

  editWindow.on('did-finish-load', inyectarDatosEdit());

  editWindow.on('close', function(){
    editWindow = null;
});
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  fs.writeFileSync('./engine/data/boardJson.json', fs.readFileSync('./engine/data/boardJsonBlank.json', 'utf8'), (err) => {
    if (err) console.log(err);
  }); 
    if (process.platform !== 'darwin') {
      app.quit()
    }
})

