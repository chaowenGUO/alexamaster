
import http from 'http'
import process from 'process'
http.createServer((req, res) =>
{
    res.write('Hello World!')
    res.end()
}).listen(process.env.PORT)
