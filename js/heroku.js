import http from 'http'
import process from 'process'
import './surf.js'
http.createServer().listen(process.env.PORT)
