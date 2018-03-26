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

  python.on('close', (code) => {        
    console.log(`child process exited with code ${code}`);
  });
}



app.post("/StartPython", (req, res) =>
{
  runPythonScript('UR5test.py')
})

//Stop child process (the flip motion) halt or wait script
app.post("/StopPython", (req, res) =>
{
  console.log("should kill")
  const killPython = spawn('sh', ['test.sh']);
  //enter code here to tell ur5 to stop
  // runPythonScript('')
})

//litsening to webpage localhost:3000
app.listen(3000, () => console.log("Server running."))