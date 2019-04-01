var Validator = require('output.json').Validator;
var v = new Validator();

var addressSchema = {Status:
"status": "ok",
"totalResults": "number",
-"articles": [

-"source": {
"id": "string",
"name": "string"
},
"author": "boolean",
"title": "string",
"description": "string",
"url": "string",
"urlToImage": "string",
"publishedAt": "date",
"content": "string"
