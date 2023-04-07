import requests, json, random, string, os, base64, time
from pydash import omit
from datetime import datetime
from requests_toolbelt import MultipartEncoder
from bs4 import BeautifulSoup
from rich import print as printer
from rich.panel import Panel
from rich.align import Align
import gspread
from oauth2client.service_account import ServiceAccountCredentials


DIR = os.path.dirname(os.path.abspath(__file__))


###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu


LIST__ = [
"Kemajuan Utama",
"Bersama Sejahtera",
"Citra Cinta",
"Damai Investama",
"Damar Membara",
"Bara Kahuripan",
"Gempita Cahaya",
"Makmur Abadijaya",
"Warna Warni",
"Keuntungan Bersama",
"Bumi sejahtera Abadi",
"Amanda Anak Mantu Damai Abadi",
"Bahagia Sejahtera",
"Sentosa Abadi",
"Cahaya Terang",
"Sederhana Industri Makmur",
"Indah Citrabdi",
"Nagatama Sundalaya",
"Mega Cerah",
"Kencana Ceria",
"Rasa Cinta",
"Bahagia Sentosa",
"Boga Rasa Mandiri",
"Tata Citra Sejahtera",
"Cerita Rasa",
"Nikmat Industri",
"Abadi Rasa",
"Lidah Bercitra",
"Sentosa Boga Indonesia",
"Cinta Citrasa",
"Jaya Abadi",
"Mekar Laksana",
"Citra Sentosa",
"Sentosa Sejahtera",
"Bahagia Bangunjaya",
"Jawa Jayadi",
"Permai Indah Sentosa",
"Pandau Permai",
"Griya Lestari",
"Sentosa Bahagia Jayadi",
"Tambangjaya",
"Makmur Minyak",
"Istana Jaya",
"Solusi Sentosatama",
"Sumbertama Cahaya",
"Cahaya Daya Alam",
"Alam Mahkota",
"Mahkota Intan Permata",
"Abani Andalus",
"Borneo Indahtama"
]

class RandomPt:
    def __init__(self):
        self.ran = f"{random.choice(['PT.', 'CV.', 'TOKO'])} {random.choice(LIST__).split()[0]} {random.choice(LIST__).split()[0]}"
    
    def random__(self):
        return self.ran

def clear_layar():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

@staticmethod
def number__(jum) -> str:
  ch = string.digits
  return ''.join([random.choice(ch) for x in range(jum)])


class TempekMail:
    def __init__(self) -> None:
        pass
    
    def create_email(self, nama):
        email = f'{nama}{number__(3)}@lasagna.email'
        return email.lower()

    def get_mail(self, email):
        with requests.Session() as session:
            
            base_mail = session.get(
            'https://lasagna.email/api/inbox/%s' % email
          )
            return base_mail.json()['emails']

class Shorlink:
    def short(url):
        sample_string_bytes = url.encode("ascii")
        base64_bytes        = base64.b64encode(sample_string_bytes)
        base64_string       = base64_bytes.decode("ascii")
    
        fields = {
            "Content-Disposition": "form-data",
            "name": "longUrl",
            "Content-Disposition": "form-data",
            "name": "shortKey",
            "longUrl": base64_string
            }
        
        boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        m = MultipartEncoder(fields=fields, boundary=boundary)
        
        headers = {
            'authority': 'suo.yt',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': f'multipart/form-data; boundary={boundary}',
            'origin': 'https://suo.yt',
            'referer': 'https://suo.yt/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }
        
        res = requests.post(
            "https://suo.yt/short",
            headers=headers,
            data=m
        )
        return res.json()['ShortUrl']

# LOGIN EMAIL
class GetAuth:
    def __init__(self) -> None:
        pass
    
    def login__(self, email, sandi):
        headers = {
            'content-type':'application/json; charset=utf-8',
            'INGRESSCOOKIE':'cfda8846bc7be3bb28fdb63987c9c3ea|15c4a256545252d8d9c6fbf36d3467c6; Path=/; Secure; HttpOnly',
            'access-control-allow-origin':'http://localhost',
            'etag':'W/"44-mPTbBrZpvWCI9OOcqUINEogywEs"'
        }

        res = requests.post(
            url = 'https://api.paper.id/api/v1/auth/paper-chain-status',
            headers = headers,
            json ={"email":email}
        )
        INGRESS = headers['INGRESSCOOKIE']
        headers = {
            "Host": "api.paper.id",
            "accept": "application/json, text/plain, */*",
            "authorization": "null",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; POCO F2 Pro Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "http://localhost",
            "x-requested-with": "id.paper.invoicer",
            "referer": "http://localhost/auth/login",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        res = requests.post(
            url = "https://api.paper.id/api/v1/auth/login",
            headers = headers,
            json = {"email":email,"password":sandi,"ttl":31104000}
        )
        data = res.json()
        auth = data['id']
        with open(f'{DIR}/data/auth.json', 'w') as f:
            f.write(json.dumps(
                {
                    "auth": auth,
                    "headers": headers,
                },
                indent=4
            ))

#PATNER
class Patner:
    def __init__(self) -> None:
        self.file    = json.load(open(f'{DIR}/data/auth.json'))
        self.auth    = self.file['auth']
        self.headers = self.file['headers']
    
    def cek_patner(self):
        headers = omit(
            self.headers, 
            "authorization",
            "referer"
            )
        headers.update({
            "authorization": self.auth,
            "referer": "http://localhost/client"
        })
        res = requests.post(
            url="https://api.paper.id/api/v1/invoicer/partners/all",
            headers=headers,
            json={
                "filters":
                    {
                        "number":{"matchMode":"undefined","value":""},
                        "name":{"matchMode":"undefined","value":""},
                        "global":{"matchMode":"undefined","value":""},
                        "email":{"matchMode":"undefined","value":""},
                        "type":{"matchMode":"undefined","value":""},
                        "phone":{"matchMode":"undefined","value":""},
                        "country":{"matchMode":"undefined","value":""}
                    },
                "first":0,
                "rows":8,
                "sortOrder":-1,
                "sortField":"created_at"
                }
        )
        data = res.json()
        #print(json.dumps(data, indent=4))
        jum_patner   = data["total_records"]
        create_nomer = str(int(jum_patner) + 1).zfill(4)
        return {
            "jumlah": str(jum_patner).zfill(4),
            "create": create_nomer,
            "patner": data["partners"],
            "headers": headers,
        }
    
    def create_patner(self, email):
        data = self.cek_patner()
        headers = data['headers']
        headers = omit(headers, "referer")
        headers.update({"referer": "http://localhost/client/create?is_edit=false"})
        return requests.post(
                url="https://api.paper.id/api/v1/invoicer/partners",
                headers=headers,
                json={
                    "number":"0100",
                    "name":"PT. LAKNAT TRALALA",
                    "email": email,
                    "phone":"085785234267",
                    "mobile":"085785234267",
                    "city": "null",
                    "state": "null",
                    "type": "Client",
                    "bank_accounts": "null"
                    }
            ).json()
    
    def edit_patner(self):
        nomer_hp = "0857" + number__(8)
        toko = RandomPt().random__()
        data = self.cek_patner()
        patner = data['patner']
        headers = data['headers']
        
        nama_email = ''.join(toko.split()[1:3])
        email = TempekMail().create_email(nama=nama_email)
 
        cek_number = [x['number'] for x in patner if x['number'] == '0100']
        hasilku = []
        if '[]' == str(cek_number):
            hasil = self.create_patner(email=email)
            hasilku.append(hasil)
        else:
            pat = self.cek_patner()['patner']
            patz = [x for x in pat if '0100' == x['number']]
            patx = patz[0]
            
            # EDIT PATNER
            headers = omit(headers, "referer")
            headers.update({
                "referer": f"http://localhost/client/edit/{patx['uuid']}"
            })
            json__ = {
                    "uuid": patx['uuid'],
                    "name": toko,
                    "phone": nomer_hp,
                    "email": email,
                    "number": "0100",
                    "mobile": nomer_hp,
                    "address1": "surabaya",
                    "address2": "surabaya",
                    "city": "surabaya",
                    "state": "surabaya",
                    "postal_code": "64567",
                    "country": "Indonesia",
                    "website": f"www.{toko.split()[-1].lower()}.com",
                    "notes": toko,
                    "bank_accounts": [],
                    "type":"Client",
                    }
            res = requests.put(
                url = f"https://api.paper.id/api/v1/invoicer/partners/{patx['uuid']}",
                headers = headers,
                json=json__
                )
            hasil = res.json()
            hasilku.append(hasil)
        return hasilku[0]

    def create_product(self):
        data = self.cek_patner()
        headers = data['headers']
        
        headers = omit(headers, "referer")
        headers.update({
            "referer": "http://localhost/product/create"
        })
        res = requests.post(
            url="https://api.paper.id/api/v1/invoicer/products",
            headers=headers,
            json={
                "name":"GEDANG GORENG",
                "code":"SKU5000",
                "track_stock":0,
                "uom_id":"05429f81-f62e-41cd-ba00-2c4245c060e7",
                "sales_price":"10000",
                "purchase_price": "10000",
                "description":"Produk sangat kenyal",
                "uom_name":"Piece"
            }
            )
        return res.json()
    
    def cek_product(self):
        data = self.cek_patner()
        headers = data['headers']
        
        headers = omit(headers, "referer")
        headers.update({
            "referer": "http://localhost/product/select-product"
        })
        res = requests.post(
            url="https://api.paper.id/api/v1/inventory/products/all",
            headers=headers,
            json={
                "filters":{
                    "category_name":{
                        "matchMode":"undefined",
                        "value":""
                        },
                    "code":{
                        "matchMode":"undefined",
                        "value":""
                        },
                    "global":{
                        "matchMode":"undefined",
                        "value":""
                        },
                    "name":{
                        "matchMode":"undefined",
                        "value":""
                        },
                    "purchase_price":{
                        "matchMode":"undefined","value":""
                        },
                    "sales_price":{
                        "matchMode":"undefined",
                        "value":""
                        },
                    "track_stock":{
                        "matchMode":"undefined",
                        "value":""},
                    "uom_name":{
                        "matchMode":"undefined",
                        "value":""
                        }
                    },
                "first":0,
                "rows":8,
                "sortOrder":-1,
                "sortField":"category_name"
                }
        )
        hasilku = []
        datax = res.json()
        data  = datax['products']
        cek__ = [pro for pro in data if 'SKU5000' in pro['code']]
        if '[]' in str(cek__):
            hasil = self.create_product()
            hasilku.append(hasil)
        else:
            hasil = cek__[0]
            hasilku.append(hasil)
        return hasilku[0]


class Invoice:
    def __init__(self) -> None:
        self.file    = json.load(open(f'{DIR}/data/auth.json'))
        self.auth    = self.file['auth']
        self.headers = self.file['headers']
    
    def uploud_file(self, harga):
        #if os.path.exists(f'{DIR}/data/paper.xlsx'):
        #    os.remove(f'{DIR}/data/paper.xlsx')
        
        now            = datetime.now()
        tanggal        = now.strftime("%d/%m/%Y")
        no_invoce      = f'INV/{now.strftime("%Y")}/{number__(5)}'
        patner         = Patner().edit_patner()['partner']
        nama_patner    = patner['name']
        email_patner   = patner['email']
        nomer_hp       = patner['phone']
        

        #df = pd.DataFrame([[nama_patner, nomer_hp, email_patner, no_invoce, tanggal, tanggal, '',
        #                    'SKU5000','GEDANG GORENG','Produk sangat kenyal', '1', harga, 0, '', 0, '', '', '']]
        #          ,columns=['*Client Name', '*Partner Telephone Number', 'Email',
        #                    '*No. Invoice', '*Date', '*Due Date', 'Salesperson',
        #                    'Product SKU', '*Item Name', '*Item Description', '*Qty',
        #                    '*Price', 'Discount (%) per Line', 'Nama Pajak', 'Diskon Total',
        #                    'Syarat dan Ketentuan', 'Keterangan', 'Biaya Ongkir'])
        #df.to_excel(f'{DIR}/data/paper.xlsx', sheet_name='format_bulk', index=False)
        
        scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(f'{DIR}/data/api_sheet.json', scope)

        gc = gspread.authorize(credentials)
        sheet = gc.open('paper').sheet1


        sheet.update('A2', nama_patner)
        sheet.update('B2', nomer_hp)
        sheet.update('C2', email_patner)
        sheet.update('D2', no_invoce)
        sheet.update('E2', tanggal)
        sheet.update('F2', tanggal)
        sheet.update('H2', 'SKU5000')
        sheet.update('I2', 'GEDANG GORENG')
        sheet.update('J2', 'Produk sangat kenyal')
        sheet.update('K2', 1)
        sheet.update('L2', harga)


        spreadsheet_id = "1YfAOnSGVpW2SDRvL98r0ad_TJFnEcbcOO426O3jsTM8"
        access_token = credentials.create_delegated(credentials._service_account_email).get_access_token().access_token
        url = "https://www.googleapis.com/drive/v3/files/" + spreadsheet_id + "/export?mimeType=application%2Fvnd.openxmlformats-officedocument.spreadsheetml.sheet"
        res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

        with open(f"{DIR}/data/paper.xlsx", 'wb') as f:
            f.write(res.content)        


        # UPLOUD FILE XLSX
        fields = {
            "Content-Disposition": "form-data",
            "name": "file",
            "filename": "paper.xlsx",
            "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "file": ("paper.xlsx", open(f'{DIR}/data/paper.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        }
        boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        m = MultipartEncoder(fields=fields, boundary=boundary)
        headers = {
                "Host": "api.paper.id",
                "accept": "application/json, text/plain, */*",
                "authorization": self.auth,
                "user-agent": "Mozilla/5.0 (Linux; Android 10; POCO F2 Pro Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36",
                "content-type": f'multipart/form-data; boundary={boundary}',
                "origin": "https://www.paper.id",
                "referer": "https://www.paper.id/",
                "accept-encoding": "gzip, deflate",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",

            }
        res = requests.post(
            url="https://api.paper.id/api/v1/import-data/invoice/upload",
            headers=headers,
            data=m
        )
        batch_id = res.json()['arango_batch_id']
        headers = omit(headers, "content-type")
        headers.update({
           "content-type":"application/json"
        })
        data = {
          "arango_batch_id": batch_id,
          "room": "16808051444487163"
        }
        requests.post(
            "https://api.paper.id/api/v1/import-data/invoice/save",
            headers=headers,
            json=data
        )
        
        # CEK ALL INVOICE 
        data = {
            "filters": {
                    "number": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "global": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "client_name": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "partner_id": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "status": {
                      "matchMode": "undefined",
                      "value": []
                    },
                    "invoice_total": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "send_status": {
                      "matchMode": "undefined",
                      "value": []
                    },
                    "start_invoice_date": {
                      "matchMode": "undefined",
                      "value": ""
                    },
                    "end_invoice_date": {
                      "matchMode": "undefined",
                      "value": ""
                    }
                  },
                  "first": 0,
                  "rows": 8,
                  "sortOrder": -1,
                  "sortField": "created_at",
                  "file_type": "csv"
        }
        res = requests.post(
            "https://api.paper.id/api/v1/invoicer/sales-invoices/all",
            headers=headers,
            json=data
        )
        inv = res.json()['invoices']
        for x in inv:
            if nama_patner in x['name']:
                hasil = x
                break
        return {
            "headers": headers,
            "invoice": hasil
        }
        
    def send_invoice(self, harga):
        create   = self.uploud_file(harga=harga)
        headers  = create['headers']
        hasil    = create["invoice"]
        email    = hasil['email']
        phone    = hasil['phone']
        inv_uuid = hasil['uuid']
        data = {
                "invoices": [
                        {
                            "partner_email": email,
                            "partner_phone": phone,
                            "send_methods": [
                              "email"
                            ],
                            "uuid": inv_uuid
                        }
                    ],
                "room": "16808068990286118"
            }
        
        res = requests.post(
            "https://api.paper.id/api/v1/import-data/invoice/send",
            headers=headers,
            json=data
        )
        return email
        

class KodeBayar:
    def __init__(self, harga) -> None:
        self.email = Invoice().send_invoice(harga=harga)
    
    def get_kode(self):
        while True:
            try:
                body = TempekMail().get_mail(self.email)[0]["Body"]
                break
            except:continue
            
        token   = []
        soup    = BeautifulSoup(body, 'html.parser') #lxml
        
        for l in soup.find_all('a'):
            link = l.get("href")
            if 'https://payment.paper.id' in link:
                tokex = link.split('=')[1].split('&')[0]
                token.append(tokex)
                ling = Shorlink.short(link)
                break
            
        headers = {
            "accept":"application/json, text/plain, */*",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9",
            "content-type":"application/json",
            "host":"api.paper.id",
            "origin":"https://payment.paper.id",
            "referer":"https://payment.paper.id/",
            "token":"null",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        }

        res = requests.post(
            "https://api.paper.id/api/v1/payper-api/authorization",
            headers= headers,
            json={
                "ParaRes": token[0]
            }
        )
        
        bes     = res.json()
        datax   = bes['golang_data']
        data    = bes['data']
        headers = omit(headers, "token")
        headers.update({"token": data})
        
        res = requests.post(
                "https://api.paper.id/api/v1/payper-api/single-invoice",
                headers=headers,
                json={
                  "data": datax,
                  "link_source": "email",
                  "parares": data
                }   
        )
        
        data  = res.json()['full_invoice']['data']
        id__  = data['_id']
        key__ = data['_key']
        res   = requests.post(
          "https://api.paper.id/api/v1/payper-api/single-invoice/payment-method-all",
          headers=headers,
            json={
              "data": datax,
              "link_source": "email",
              "parares": data
          }   
        )
        
        body    = res.json()['body']
        sup_id  = body['company_id']
        buyer_id= body['partner_company_id']
        res     = requests.post(
            "https://api.paper.id/api/v1/payper-api/payment-request/create",
            headers=headers,
            json={
              "supplier_id": sup_id,
              "buyer_id": buyer_id,
              "invoices": [
                  {
                  "invoice_id": id__
                }
              ],
              "source": "payper"
            }
        )
        rekues      = res.json()['data']['payment_request']
        paper_chain = rekues['_id']
        paper_key   = rekues['_key']
        res = requests.post(
          "https://api.paper.id/api/v1/payper-api/payment-request/payment-method/choose",
          headers=headers,
          json={
            "promotion_id": "",
            "payment_method": "mitra_pembayaran_digital",
            "payment_provider": "blibli",
            "payment_request_key": paper_key,
            "paper_customer_id": buyer_id
          }
        )
        data = res.json()['data']
        """kode_bayar = data['external_id']
        print(kode_bayar)"""
        res = requests.get(
          f"https://api.paper.id/api/v1/payper-api/payment-request/key/{paper_key}", 
          headers=headers
        )
        kode__ = res.json()['data']["external_id"]
        return {"link":ling, "kode": kode__}





class Menu:
    def menu__():
        clear_layar()
        if os.path.exists(f'kode.txt'):
            os.remove('kode.txt')
        if not os.path.exists(f'{DIR}/data/auth.json'):
            sts = Align.center(f"{P2}LOGIN PAPER")
            printer(Panel(sts,width=54,style="#FF8F00", subtitle=f"{P2}• {M2}{P2} •", subtitle_align="center"))
            email = input(f"{J}  • {P}Email: {J}")
            sandi = input(f"{J}  • {P}Sandi: {J}")
            GetAuth().login__(email=email.strip(), sandi=sandi.strip())
            time.sleep(2)
            clear_layar()
            
        harga = input(f"{J}  • {P}Harga: {J}")
        gawe = input(f"{J}  • {P}Gawe piro: {J}")
        clear_layar()
        jum = 0
        datak = []
        
        sts     = Align.center(f"{J2} • {P2}KODE PAPER {J2}•")
        printer(Panel(sts,width=54,style="#FF8F00"))
        for _ in range(int(gawe)):
            jum+=1
            info    = KodeBayar(harga=harga).get_kode()
            link    = info['link']
            kodeb   = info['kode']
            sts     = Align.left(f"{J2} • {P2}Link{J2} • {P2}{link}\n{J2} • {P2}Kode{J2} • {P2}{kodeb}")
            printer(Panel(sts,width=54,style="#FF8F00", title=f"[{P2} {str(jum).zfill(2)}{J2} ]", title_align="left", padding=(1, 2)))
            with open('kode.txt', 'a') as f:
                f.write(f'{kodeb} | {link}\n')
       
   
if __name__ == '__main__':
    Menu.menu__()