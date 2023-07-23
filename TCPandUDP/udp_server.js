const dgram = require('dgram')
const socket = dgram.createSocket('udp4')
const HOST = '127.0.0.1'
socket.on('message', (msg, rinfo) => {
  console.log(`server got: ${msg} from ${rinfo.adress}:${rinfo.port}`);
});

socket.bind(8082, HOST, () => {
  console.log('Testin UDP connection');
});