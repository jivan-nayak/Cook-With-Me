import urllib.request
# HTTP REQUEST of some address
def REQUEST(address):
    req = urllib.request.Request(address)
    req.add_header('User-Agent', 'NAME (Linux/MacOS; FROM, USA)')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')  # make sure its all text not binary
    print("REQUEST (ONLINE): " + address)
    return html

REQUEST("https://www.bigbasket.com/pd/40100521/fresho-signature-cheese-chevere-log-fresh-rindless-block-200-g/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")