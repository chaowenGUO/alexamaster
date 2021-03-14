import http from 'http'
import process from 'process'
http.createServer((req, res) => res.end()).listen(process.env.PORT, '0.0.0.0')
