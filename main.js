const electron = require('electron')
const http = require('http')

const {app, BrowserWindow} = electron

app.on('ready', () => {

    let mainWindow = new BrowserWindow({width:800, height: 600})
    mainWindow.loadURL('file://' + __dirname + '/templates/login.html')
    mainWindow.webContents.openDevTools()

    // TODO: Add conditions to check if the user is already logged in. If not ask to login.
    const loginButton = document.getElementById('login__submit')
    loginButton.onclick = LoginUser()
})


function LoginUser() {
    // Login and authentication condition here
    // let options = {
    //     host: 'localhost',
    //     port: '3000',
    //     path: '/users/',
    //     method: 'POST'
    // }
    // let requestObject = http.request(options, (res) => {
    //     res.setEncoding('utf8')
    //     res.on('data', (body) => {
    //         console.log('Response Body is : ', body)
    //     })
    // })
    // requestObject.on('error', (err) => {
    //     console.log('Failed to make request!\nError -> ', err)
    // })
    // let emailAddress = document.getElementById('login__username')
    // let passwordEntered = document.getElementById('login__password')
    // requestObject.write(JSON.stringify({
    //     password: passwordEntered,
    //     email: emailAddress
    // }))
    // requestObject.end()
}