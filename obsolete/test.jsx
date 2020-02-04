
include "json2.js";

var file = new File;

function openUrl(){
    reply = "";
    conn = new Socket;
    // access Adobe’s home page
    if (conn.open ("https://cdn.oantagonista.net/uploads/2017/12/embraer-1.png:80")) {
        // send a HTTP GET request  
        conn.write ("GET /images/embraer-1.png HTTP/1.0\n\n");
    // and read the server’s reply
        reply = conn.read(999999);
    conn.close();
    }
    return reply;
}
function readJson(filePath){
    var currentLine;
    var jsonStuff = [];
    file.open("r");
    while(file.eof){
        currentLine = file.readln();
        jsonStuff.push(currentLine);
    }
    file.close();
    jsonStuff = jsonStuff.join("");
    var parsedJson = JSON.parse(jsonStuff);
    alert(parsedJson.)
    return parsedJson;
}

var myComp = app.project.activeItem;


var scriptFile = File("./data/output.json");

scriptFile.open('r');

var content = scriptFile.read();

//var data = footage("output.json").sourceData;

var content= data.articles[0].description;

myComp.layer("Content ").property("ADBE Text Properties").property("ADBE Text Document").setValue(content);

scriptFile.close();


//footage("output.json").dataValue([2,0,1])

/* var data = footage("output.json").sourceData;

var title = data.articles[0].title;

n = 30;
outStr = "";
newLine = ""
splt = title.split(" ")
for (i = 0; i < splt.length; i++){ if ((newLine + " " + splt[i]).length > n){
if (outStr != "") outStr += "\r";
outStr += newLine;
newLine = splt[i];
}else{
if (newLine != "") newLine += " ";
newLine += splt[i];
}
}
if (newLine != ""){
if (outStr != "") outStr += "\r";
outStr += newLine;
}
outStr; */