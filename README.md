# Aktif Bilgi Toplama Nedir?
Aktif keşif, hedef hakkında sisteme özgü bilgileri toplamak için doğrudan bir bilgisayar sistemiyle etkileşime girdiğiniz zamandır. Kamuya açık bilgilere dayanan pasif bilgi toplamanın aksine, aktif bilgi toplama, bilgisayara farklı türde istekler gönderecek araçlara dayanır. Amaç, o cihaz veya ona aynı ağ üzerinde bağlı olan diğer cihazlar hakkında bilgi toplamaktır. Aktif keşif, açık/kapalı bağlantı noktaları, bir makinenin işletim sistemi, çalışan hizmetler, afiş kapma, yeni ana bilgisayarlar keşfetme veya bir ana bilgisayardaki savunmasız uygulamaları bulma gibi bilgileri bulmak için kullanılabilir. Pasif keşifle karşılaştırıldığında aktif keşif yapmanın ana dezavantajı, ana bilgisayarla doğrudan etkileşimin sistem IDS/IPS'yi tetikleme ve insanları faaliyetiniz konusunda uyarma şansına sahip olmasıdır.

# WINFO
## Özellikleri
- Whois<br>
- HTTP Banner Grab<br>
- Traceroute<br>
- Subdomain Finder<br>
- DNS Lookup<br>
- Port Scan<br>

## Kullanılan Kütüphaneler
- argparse<br>
- requests<br>
- DateTime<br>
- whois<br>
- arg<br>
- sys<br>
- os<br>

## Kurulum
`git clone https://github.com/wolk4n/winfo`

`cd winfo`

`chmod +x install.sh`

`./install.sh`

`python3 winfo.py`

## Aracın içinden görüntüler
<img src="https://github.com/wolk4n/winfo/blob/main/img/main.png">

<img src="https://github.com/wolk4n/winfo/blob/main/img/whois.png">

<img src="https://github.com/wolk4n/winfo/blob/main/img/subs.png">
