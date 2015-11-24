# Author: Jayden Navarro
# Date: 11/24/2015
#!/usr/bin/python

import socket
import json
import threading
import os

delim = '.,.'

def encode( data ):
   return json.dumps( data ) + delim

def decode( data ):
   stringBuffer = data[:-3]
   return [ json.loads( x ) for x in stringBuffer.split( delim ) ]

def smartDecode( D_BUFFER, data ):
   stringBuffer = D_BUFFER.decode( 'utf-8' )
   if stringBuffer[-3:] == delim:
      stringBuffer = stringBuffer[:-3]
      output = ""
      if delim in stringBuffer:
         bufferList = [ json.loads( x)
                        for x in stringBuffer.split( delim ) ]
         data.extend( bufferList )
         for line in bufferList:
            output += line
      else:
         output = json.loads( stringBuffer )
         data.append( output )
      return( b"", output )
   else:
      return( D_BUFFER, "" )

class TcpClient:
   def __init__( self, ip, port, buf ):
      self.TCP_IP = ip
      self.TCP_PORT = port
      self.BUFFER_SIZE = buf
      
   def connect( self ):
      self.s = socket.socket()
      self.s.connect((self.TCP_IP, self.TCP_PORT))
      
   def start( self, user ):
      print( "Waiting for remote connection..." )
      print
      while True:
         try:
            self.connect()
            break
         except:
            pass
      print
      print( "CONNECTED" )
      print
      prevData = "0"
      print
      while True:
         data = raw_input( "" )
         if data == "" and prevData == "": break
         self.send( user + ': ' + data )
         prevData = data
         print
      self.close()
      print( "CONNECTION CLOSED" )
      os._exit(0)
      
   def send( self, data ):
      self.s.send( encode( data ) )

   def close( self ):
      self.s.close()
      
class TcpServer:
   def __init__( self, ip, port, buf ):
      self.TCP_IP = ip
      self.TCP_PORT = port
      self.BUFFER_SIZE = buf
      self.data = []
      
   def start( self ):
      self.s = socket.socket()
      self.s.bind((self.TCP_IP, self.TCP_PORT))
      self.s.listen(1)
      self.conn, self.addr = self.s.accept()
      D_BUFFER = b""
      while True:
         CURRENT = self.conn.recv(self.BUFFER_SIZE)
         if not CURRENT: break
         D_BUFFER += CURRENT
         D_BUFFER, out = smartDecode( D_BUFFER, self.data )
         if out != "" and len( out ) != 3:
            print( out )
            print
      print( "CONNECTION REMOTELY CLOSED" )
      os._exit(0)

class TcpP2P:
   def __init__( self, user, ip, cPort, sPort, cBuf, sBuf ):
      self.USER = user
      self.TCP_IP = ip
      self.C_TCP_PORT = cPort
      self.S_TCP_PORT = sPort
      self.C_BUFFER_SIZE = cBuf
      self.S_BUFFER_SIZE = sBuf
      self.data = []

   def start( self ):
      server = TcpServer( '', self.S_TCP_PORT, self.S_BUFFER_SIZE )
      client = TcpClient( self.TCP_IP, self.C_TCP_PORT,
                          self.C_BUFFER_SIZE )

      serverThread = threading.Thread( target=server.start )
      clientThread = threading.Thread( target=client.start,
                                       args=( self.USER, ) )
      
      serverThread.start()
      clientThread.start()
