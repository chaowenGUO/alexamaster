import http from 'http'
import process from 'process'
http.createServer((req, res) => res.end()).listen(process.env.PORT)
import './surf.js'
