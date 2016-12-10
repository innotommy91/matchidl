import psycopg2,os,fnmatch,re
from idl_parser import parser

parser_ = parser.IDLParser()
global_module = parser_.parse_idl('/Users/innotommy91/qwer/src/third_party/WebKit/Source/modules/webaudio/AnalyserNode.idl')
my_module = global_module.module_by_name('AnalyserNode')
dataGetter = my_module.interface_by_name('AnalyserNode')


Pathchromium = '/Users/innotommy91/qwer/src/'
Pattern ='*.idl'

def connessione():
	conn = psycopg2.connect("dbname=crawl_data user=snyderp")

	cur = conn.cursor()
	print "eseguo query"
	cur.execute("SELECT * FROM standards WHERE id=1;")
	print "solo una"
	x=cur.fetchone()
	print len(x)
	return "done"

def filesearch(pattern, path):
    result = []
    print "start searching file that match pattern: "+ pattern +" in that directory: "+path
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#find('*.idl', '/Users/innotommy91/qwer/src/third_party/WebKit')

def directorysearch(head_dir,search):
   result = []
   print "start searching directory that match:"+ search +"\nstarting from directory: "+ head_dir
   for root, dirs, files in os.walk(head_dir):
        for d in dirs:
            if d==search:
                result.append(os.path.join(root, d))
   print "i have finded "+str(len(result))+ " directory match:"
   for i in range(len(result)):
   		print result[i]
   return result

"""
directorysearch(Pathchromium, 'webaudio')
"""

def startresearch(feature,standard):
	name = standard.replace(' ', '')
	print "start searcing for "+feature+" "+name
	resultdir = []
	resultfile = []
	featurefile = []
	resultdir = directorysearch(Pathchromium,name)#receive directory that match the standard
	for i in range(len(resultdir)):
		resultfile = filesearch(Pattern,resultdir[i])
		for j in range(len(resultfile)):
			tup =(feature,standard,resultfile[j])
			featurefile.append(tup)
	print"research finished founded "+str(len(featurefile))+" file that match standard and patter for the "+feature
	for i in range(len(featurefile)):
		print featurefile[i]
		print i
		print "\n"
"""
startresearch('feature test',"web audio")
"""





