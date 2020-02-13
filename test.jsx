//IMPORT JSON

function readJSONFile(file){
    file.open('r');
    var data = file.read();
    file.close();
    data = JSON.parse(data);
    for (var i in data){
        alert(data['articles'])
    }
}

//var jsonFile = File('./data/output.json');

//readJSONFile(jsonFile)

//PARSE JSON TO EACH LAYER IN EACH COMPOSITION

//CHECK PROPERTIES AND APPLY LAYOUT SETTINGS

//LOAD IMAGES
var folder = new Folder;

folder = Folder('./images/')

var files = folder.getFiles();

//files = filterFiles(files, '.png');

importFiles(files);

function importFiles(files){
    app.beginSuppressDialogs();
    for(var i = 0; i<files.length; i++){
        //alert(files[i].name)
        app.project.importFile(new ImportOptions(File(files[i])));
    }
    app.endSuppressDialogs(false);
} 

function filterFiles(files, extension){
    var filtered = [];
    for (var i =0; i<files.length; i++){
        if(files[i].name.indexOf(extension) == -1){
            filtered.push(files[i]);
        }
    }
    return filtered;
}

//Title
var data = footage("output.json").sourceData;

var title = data.articles[0].title;

n = 15;
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
outStr;

//Date
var data = footage("output.json").sourceData;
var date = data.articles[0].publishedAt;

var newDate = new Date(date);

date

