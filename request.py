import sys
import requests


if len(sys.argv)>1:
	r = requests.get(sys.argv[1], auth=('ruilazarev', 'm0iParol'))
	print(r.json())

#wget  --header="Authorization: Basic cnVpbGF6YXJldjptMGlQYXJvbA==" --header="Content-Type: application/json" https://ruilazarev:m0iParol@jira.harman.com/jira/rest/api/2/issue/PSADEV-596 