import http from 'http'
import process from 'process'
import './surf.js'
http.createServer((req, res) => res.end()).listen(process.env.PORT)
