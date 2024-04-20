import speedtest
from time import sleep
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")

st = speedtest.Speedtest()

st.get_best_server()  
for i in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
    sleep(0.05)

st.download()  
for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed"):
    sleep(0.05)

st.upload()  
for i in tqdm(range(10), colour="red", desc="Getting Upload Speed"):
    sleep(0.05)

res_dict = st.results.dict()

dwnl = str(res_dict['download'])[:2] + "." + \
    str(res_dict['download'])[2:4]

upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]

print("")

print(Fore.MAGENTA + "="*80)
print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))
print(Fore.MAGENTA + "="*80)
print(Fore.YELLOW +
      f"Download: {dwnl}mbps({float(dwnl)*0.125:.2f}MBs) | Upload:{upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(80))
print(Fore.MAGENTA + "-"*80)
print(Fore.CYAN +
      f"HOST:{res_dict['server']['host']} | SPONSOR:{res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}".center(80))
print(Fore.MAGENTA + "-"*80)