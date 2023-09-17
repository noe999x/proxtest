######## Do not remove ########
welcome = "Code by Bagasekaapr"
"""
All elements in this code have valid sources,
and I do not advise you to obtain anything through illegal means.

Do not being an idiot, greetz y'all.
"""
######## Do not remove ########

class mommy_kafka:
    def __init__(self):
        self.live, self.dead, self.unknown, self.loop = [], [], [], 0
        self.github = "https://raw.githubusercontent.com"
        self.menu()

    def ask(self):
        while True:
            ask = input('SOCKS4 OR SOCKS5 ? (4/5): ')
            if ask == "4" or ask == "5":
                num = int(ask)
                return num
            else:
                print('Invalid input. Please enter 4 or 5.')

    def menu(self):
        os.system('clear');print(welcome)
        print('''
(1) Dump - github.com/prxchk     [SOCKS4-SOCKS5]  (Updated true 5min)
(2) Dump - github.com/casals-ar  [SOCKS4-SOCKS5]  (Updated true 5min)
(3) Dump - github.com/Zaeem20    [SOCKS4-SOCKS5]  (Updated true 10min)
(4) Dump - github.com/monosans   [SOCKS4-SOCKS5]  (Updated true 30min)
(5) Dump - github.com/monosans   [anon proxy]     (Updated true 30min)
(6) Dump - github.com/hookzof    [SOCKS5]         (Updated true 10min)
(7) Dump - github.com/ALIILAPRO  [SOCKS4-SOCKS5]  (Updated true 60min)
(8) Dump - github.com/sunny9577  [SOCKS4-SOCKS5]  (Updated true 3hours)
(9) Dump - github.com/yemixzy    [SOCKS4-SOCKS5]  (Updated true 2hours)
(0) Tested proxy
-usage: 0=>9\n''')
        ask = input('Your choice?: ')
        if ask == "1":
            num = self.ask()
            url = f"{self.github}/prxchk/proxy-list/main/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "2":
            num = self.ask()
            url = f"{self.github}/casals-ar/proxy.casals.ar/main/socks{num}"
            self.dumper(url, num)
        elif ask == "3":
            num = self.ask()
            url = f"{self.github}/Zaeem20/FREE_PROXIES_LIST/master/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "4":
            num = self.ask()
            url = f"{self.github}/monosans/proxy-list/main/proxies/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "5":
            num = self.ask()
            url = f"{self.github}/monosans/proxy-list/main/proxies_anonymous/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "6":
            num = None
            url = f"{self.github}/hookzof/socks5_list/master/proxy.txt"
            self.dumper(url, num)
        elif ask == "7":
            num = self.ask()
            url = f"{self.github}/ALIILAPRO/Proxy/main/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "8":
            num = self.ask()
            url = f"{self.github}/sunny9577/proxy-scraper/master/generated/socks{num}_proxies.txt"
            self.dumper(url, num)
        elif ask == "9":
            num = self.ask()
            url = f"{self.github}/yemixzy/proxy-list/main/proxies/socks{num}.txt"
            self.dumper(url, num)
        elif ask == "0":
            self.test_proxy()
        else:
            sys.exit('Wrong choice!')

    def dumper(self, url, ashdasdhakjsdhakjshdkjashdbasdmandklasdjOCNOIEWNh9H98hoiH8h8h9UUIHSV56FB86gu6bguhHHY3LSSMDUYS9SHGDSUSIDJPOSDPOJSDFGJSGUsibkKJsbuusd):
        if ashdasdhakjsdhakjshdkjashdbasdmandklasdjOCNOIEWNh9H98hoiH8h8h9UUIHSV56FB86gu6bguhHHY3LSSMDUYS9SHGDSUSIDJPOSDPOJSDFGJSGUsibkKJsbuusd is None:num = 5
        else:num = ashdasdhakjsdhakjshdkjashdbasdmandklasdjOCNOIEWNh9H98hoiH8h8h9UUIHSV56FB86gu6bguhHHY3LSSMDUYS9SHGDSUSIDJPOSDPOJSDFGJSGUsibkKJsbuusd
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                proxy_list = response.text.split('\n')
                print(f'Proxy available: {len(proxy_list)}')
                #print(response.text)
                save = input('Save list? (y/n): ')
                if save == "y":
                    with open(f'DATA/SOCKS{num}.txt', 'a') as file:
                        for proxy in proxy_list:
                            file.write(f'{proxy}\n')
                        print(f'List saved in: DATA/SOCKS{num}.txt')
                    ask = input('\nDo you wanna test the proxy? (y/n): ')
                    if ask == "y":self.test_proxy()
                    else:sys.exit('See you!')
                else:sys.exit('See you!')
            else:sys.exit('Failed to fetch proxy list.')
        except Exception as e:
            sys.exit(f'There is an error: {M}{str(e)}{P}\nMake sure you save the file in the DATA folder')

    def test_proxy(self):
        ask1 = input('Select the proxy to be tested:\nSOCKS4 -usage: 4\nSOCKS5 -usage: 5\nYour choice ? (4/5): ')
        if ask1 == "4" or ask1 == "5":num = (int(ask1))
        else:sys.exit('Wrong choice!')
        ask2 = input('\nm.facebook.com -usage: 1\nmbasic.facebook.com -usage: 2\nWhich URL will you tested? (1/2): ')
        if ask2 == "1": link = "m.facebook.com"
        elif ask2 == "2":link = "mbasic.facebook.com"
        else:sys.exit('Wrong choice!')
        try:
            with open(f'DATA/SOCKS{num}.txt', 'r') as file:
                proxy_list = file.readlines()
        except FileNotFoundError as e:
            print(f'errno: {M}{e}{P}');sys.exit("You don't have any proxies to test. Please save some proxies first before testing.")
        print(f'\nTrying connected your proxy to {K}{link}{P}')
        for proxy_address in proxy_list:
            proxy = {
                'http': f'socks{num}://' + proxy_address.strip(),
                'https': f'socks{num}://' + proxy_address.strip(),
            }
            sys.stdout.write(f'\r{P}Connecting to server [{K}{self.loop}/{len(proxy_list)}{P}] {H}LIVE : {len(self.live)}{P} -  {M}DEAD : {len(self.dead)}{P} - UNKNOWN : {len(self.unknown)}')
            sys.stdout.flush()
            try:
                url = f"https://{link}"
                response = requests.get(url, proxies=proxy, timeout=10)
                response.raise_for_status()
                if response.status_code == 200:
                    print(f'\r Try with: {H}{proxy_address.strip()}{P} Success connected!                     ')
                    with open(f'LIVE/LIVE_SOCKS{num}_{link}.txt', 'a') as live_file:
                        live_file.write(proxy_address.strip() + '\n')
                        self.live.append(proxy_address.strip())
                else:
                    print(f"\r Try with: {M}{proxy_address.strip()}{P} Unavailable.                     ")
                    self.dead.append(proxy_address.strip())
            except requests.exceptions.RequestException as e:
                print(f"\r Try with: {K}{proxy_address.strip()}{P} Failed to connect!                     ")
                self.unknown.append(proxy_address.strip())
            self.loop += 1
        print('                                 ')
        print(f'Finished.. your {H}LIVE{P} results save in LIVE/LIVE_SOCKS{num}_{link}.txt')
        ask = input('Do you wanna delete the dumped file? (y/n): ')
        if ask == "y":
           try:
               os.remove(f'DATA/SOCKS{num}.txt')
               print('Files has deleted.')
               sys.exit('See you!')
           except Exception as e:
               print(f'errno: {M}{e}{P}')
        else:
           sys.exit('See you!')

try:
    if __name__=='__main__':
        import requests, os, sys
        try:os.mkdir('DATA')
        except:pass
        try:os.mkdir('LIVE')
        except:pass
        M = '\x1b[1;91m'  # MERAH
        H = '\x1b[1;92m'  # HIJAU
        K = '\x1b[1;93m'  # KUNING
        P = '\x1b[0;00m'  # DEFAULT
        mommy_kafka()
except Exception as e:
    with open('log.json', 'a') as f:
        f.write('errno: '  + str(e))
