signature = ""                     # AWS secret access key
accesskey = ""                     #AWSaccesskeyID
sandbox   = True                   # if true, put on workersandbox.mturk.com
localhost = "http://localhost/"    # your local host
database  = "mysql://root@localhost/vatic" #server://user:pass@localhost/dbname
geolocation = ""                   # api key for ipinfodb.com
maxobjects  = 25;

# probably no need to mess below this line

import multiprocessing
sys.path.append(os.path.dirname(os.path.abspath(__file__)))