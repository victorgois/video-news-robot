var conn = new Socket;

var host =  "https://cdn.oantagonista.net/uploads/2017/12/embraer-1.png";

var cmd = "GET /index.html HTTP/1.1\r\nHost:"+host+"\r\n\r\n";

var reply='';

conn.timeout = 100;

if (conn.open (host +':80', 'BINARY')) {

        conn.write (cmd);

        while (conn.connected && ! conn.eof) {

           reply += conn.read(1024) + "\n";

        }

        conn.close();

        alert(reply);

}