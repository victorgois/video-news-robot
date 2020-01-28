var data = footage("output.json").sourceData;

var title = data.articles[0].description;

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
outStr;