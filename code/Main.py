"""
script.py - an example script with help text and a test suite

usage: python3 main.py [options]

OPTIONS:
  -d  --dump  on crash, dump stack = False
  -g  --go    start-up action      = data
  -h  --help  show help            = False
  -s  --seed  random number seed   = 937162211
"""
import re,sys,getopt
import TestEngine

def coerce(s):
  "coerce a string to some type"
  s=s.strip()
  if s=="False": 
    return False
  elif s=="True":  
    return True
  try: 
    return int(s)
  except:
      try: return float(s)
      except: return s

def get_default():
  '''
  Get default values of arguments from doc string
  '''
  global the
  p=r"\n[\s]+-[\S]+[\s]+--([\S]+)[^\n]+= ([\S]+)"
  for k,v in re.findall(p,__doc__):
    the[k]=coerce(v)
  #return t

def update(opts,t):
  '''
  Update arguments from commandline
  '''
  for opt, arg in opts:
    if opt in ("-d", "--dump"):
      t['dump'] = coerce(arg)
    if opt in ("-g", "--go"):
      t['go'] = coerce(arg)
    if opt in ("-h", "--help"):
      t['help'] = coerce(arg)
    if opt in ("-s", "--seed"):
      t['seed'] = coerce(arg)
  return t


# Stores arguments in the variable
# use python3 Main.py --[options]
the={}
if __name__ == "__main__":
    get_default()
    argv = sys.argv[1:]
    try:
      opts, args = getopt.getopt(argv, ":dghs", ["dump=","go=","help=","seed="])
    except getopt.GetoptError:
      print('Please provide appropriate arguments')
      sys.exit(2)
    the=update(opts,the)
    if the['help']:
      print(__doc__)
      sys.exit(2)
    TestEngine.run(the)
    
