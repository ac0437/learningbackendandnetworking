<!-- @format -->

# learningbackendandnetworking

## Creating

Started with: https://youtu.be/qqRYkcta6IE

Tutorial was kinda old and I was getting an error: error: read econnreset

Ended with: https://youtu.be/1udhpRy_N6A
that avoided the error.

## Testing

I did not have telnet on my windows device and wasn't looking to install that are any netcat command. Also, wasn't looking to write a powershell script as that was beyond the scope of what I wanted to learn. I was still able to test or see that the servers were up by uing the following powershell commands:

TCP server connection check:
Test-NetConnectionUDP 127.0.0.1 -p 8081

UDP server connection check:
GET-NetUDPEndpoint -LocalAddress 127.0.0.1 -LocalPort 8082
