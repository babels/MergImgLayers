from os import path, listdir, rename
from sys import argv
from subprocess import Popen, PIPE
from time import sleep

join  = path.join
exist = path.exists


def dlog( log ):

  try:
     log = str( log ).encode('utf-8')
     print("%s" % log)

  except:
     return

def Usage():
  dlog("Usage")


def proc( cmd ):

  cmd     =  str( cmd ).encode('utf-8')
  dlog("[+] CMD:  %s" % cmd)

  ps      =  Popen( cmd, shell=True )
  o, err  =  ps.communicate()

  if( o ):
     dlog( o )

def joinmaps(argc, argv):
  mpgory    =  [ 'Base', 'Metallic', 'Roughness', 'Normal' ]
  #mpgory    = [ 'BaseColor' ]
  wdr       =  argv[1]

  dlog(wdr)

  if not( exist( wdr ) ):
     Usage()
     return

  maps      =  listdir( wdr )

  for cat in mpgory:
     cat    =  str( cat )
     ofp    =  str( "%s.png" % cat )
     tfp    =  str( "%s.tmp.png" % cat )
     i      = 0
     mapsin    =  []

     for map in maps:
       if cat in map:
          mapsin.append( map )

     lnmin  =  len( mapsin )

     for min in mapsin:

       min  =  str( min )
       k    =  i + 1

       mp1 = mapsin[i]                          # first map
       mp2 = ""                                 # second map

       if( i > 0 ):
         mp2 = ofp

       else:
         mp2 = mapsin[k]

       dlog( "we gots  %s  and  %s" % (mp1, mp2) )

       #cmd = str("composite -blend 50 %s %s %s" % (mp1, mp2, tfp) )
       cmd = str("convert %s %s -composite %s" % (mp1, mp2, tfp) )
       proc(cmd)

       print("Moving  %s  to  %s" % (tfp, ofp) )
       sleep(5)
       #return
       rename(tfp, ofp)

       if( k == int( lnmin ) ):
          i = 0
          break

       else:
          i =  i +1


  print("hello %d" % argc)



if __name__ == "__main__":

   argc = len( argv )

   if( argc < 1 ):
     Usage()

   else:
     joinmaps(argc, argv)
