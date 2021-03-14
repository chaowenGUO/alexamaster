import http from 'http'
import process from 'process'
http.createServer().listen(process.env.PORT, () => globalThis.console.log('jaja'))
