import sqlite3



vt = sqlite3.connect("ruyatabiri.db")
imlec = vt.cursor()

gelenveri = imlec.execute("""SELECT link,baslik,icerik1,icerik2,icerik3,icerik4 FROM ruyatabirleri WHERE 1 """)
veriler1000 = gelenveri.fetchall()
vt.commit()
vt.close()
for veri in veriler1000:
    link = veri[0]
    baslik = veri[1]
    icerik1 = veri[2]
    icerik2 = veri[3]
    icerik3 = veri[4]
    anahtarkelime = baslik.replace(" ",",")
    anahtarkelime = anahtarkelime.lower()
    metacont = icerik1[0:170]
    headline = baslik+" tabiri, yorumu"
    json = "{"+""" "description":"{}","url":"https://ruya-tabiri.github.io/{}","@type":"WebSite","headline":"{}","name":"{}","@context":"https://schema.org" """.format(metacont,link,headline,baslik)+"}"
    sayfa = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
<title>{} | Rüya tabiri</title>
<meta property="og:title" content="{}" />
<meta name="description" content="{}" />
<meta property="og:description" content="{}" />
<meta name="keywords" content="{}">
<script type="application/ld+json">
{}</script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#157878">
    <link rel="stylesheet" href="/assets/css/style.css">
	
  </head>
  <body>
    <section class="page-header">
      <h1 class="project-name">{}</h1>
      <h2 class="project-tagline">Rüya tabiri Rüya yorumu</h2>      
    </section>
    <section class="main-content">
      <h2>{} tabiri</h2>
<p>{}</p>
<h2>Dini olarak {} tabiri</h2>
<p>{}</p>
<h2>Psikolojik olarak {} yorumu</h2>
<p>{}</p>
<h3 id="support-or-contact">Arama</h3>
<p>Rüya tabiri arayabilirsiniz.</p>
<p><script async src="https://cse.google.com/cse.js?cx=f06af576ee2079108"></script>
<div class="gcse-search"></div></p>
      <footer class="site-footer">        
        <span class="site-footer-credits">Sitemizde yer alan rüya tabirleri size sadece fikir sunmak içindir.</span>
      </footer>
    </section>    
  </body>
</html>
""".format(baslik,baslik,metacont,metacont,anahtarkelime,json,baslik,baslik,icerik1,baslik.lower(),icerik2,baslik.lower(),icerik3)
    dosya1 = open("ekle/"+link,"w",encoding="utf-8")
    dosya1.write(sayfa)
    dosya1.close()
