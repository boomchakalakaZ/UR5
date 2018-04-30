const fs = require('fs')
const express = require('express')

const app = express()
const bodyParser = require('body-parser');

const spawn = require('child_process').spawn;

//location of html
app.use(express.static('public'))
app.use("/", express.static("public/index.html"))

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); 


function runPythonScript(script)
{
  //to call code :: spawn('path to programming language .exe', [name of code])
  const python = spawn('C:/Program Files/Python36/python.exe', [script]);

    //printing to cmder console
  python.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
      
  python.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  });
 
  return python
}


function killRun(script)
{
  killPython().on('exit', () => runPythonScript(script))
}

function killPython()
{
  const killPython = spawn('sh', ['test.sh']);
  return killPython
}


app.post("/StartButton", (req, res) =>
{
  console.log("Starting Grill Program")
  killRun('Grill.py')
})

//Stop child process (the flip motion) halt or wait script
app.post("/StopButton", (req, res) =>
{
  console.log("Stopping Robot")
  killRun('StopRobot.py')
})

app.post("/HomeButton", (req, res) =>
{
  console.log("Moving to home position")
  killRun('HomePosition.py')
})

app.post("/SwapToolsButton", (req, res) =>
{
  killRun('SwapTools.py')
})

//litsening to webpage localhost:3000
app.listen(3000, () => console.log("Server running."))