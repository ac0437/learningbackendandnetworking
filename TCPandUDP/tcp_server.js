const net = require("net")

const server = net.createServer()
server.on('connection', socket => {
  console.log('Hello')
  socket.write("hello!")
  socket.on('data', data => {
    console.log(data.toString())
  })
})

server.listen(8081);