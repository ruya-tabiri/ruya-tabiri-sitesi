# Rüya Tabiri Sitesi
Python programlama ile rüya tabiri sitesi yapımı olacak bu bölümde aşama aşama nasıl rüya tabiri sitesi yapılır açıklayacağım. Sonraki aşamada ise python programlama ile yine wordpress tarzında bir rüya tabiri sitesi hazırlamayı göstereceğim. Takıldığınız bölümleri [issues](https://github.com/ruya-tabiri/ruya-tabiri-sitesi/issues) bölümünde sorabilirsiniz.

## Rüya tabiri sitesi için şablon hazırlığı

Kodumuzu hazırlamadan önce güzel bir web sitesi teması veya css i html şablonunu hazırlamamız gerekir. Sonuç olarak üreteceğimiz sitenin yapısı bu şablon veya temaya dayalı olarak görünecektir. Ben şimdilik css kısmını size bırakıyorum ve jekyll formatında bir şablon seçiyorum. Hatta doğrudan [rüya tabiri](https://ruya-tabiri.github.io) sitemizin şablonunu örnek olarak kullanayım.

Aşağıda kaynak kısmı görüntülenen basit bir şablon sunulmuştur.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
<title>Rüyada a görmek | Rüya tabiri</title>
<meta property="og:title" content="Rüyada a görmek" />
<meta name="description" content="Rüyada a görmek   toplum tarafından el üstünde tutulacağına,  yaşadığı yerden uzak kalacağına ve özlem çekeceğine,  bereket ve zenginliğe kavuşacağına,  kendi işini kurar" />
<meta property="og:description" content="Rüyada a görmek   toplum tarafından el üstünde tutulacağına,  yaşadığı yerden uzak kalacağına ve özlem çekeceğine,  bereket ve zenginliğe kavuşacağına,  kendi işini kurar" />
<meta name="keywords" content="rüyada,a,görmek">
<script type="application/ld+json">
{"description":"Rüyada a görmek   toplum tarafından el üstünde tutulacağına,  yaşadığı yerden uzak kalacağına ve özlem çekeceğine,  bereket ve zenginliğe kavuşacağına,  kendi işini kurar","url":"https://ruya-tabiri.github.io/ruyada-a-gormek.html","@type":"WebSite","headline":"Rüyada a görmek tabiri, yorumu","name":"Rüyada a görmek","@context":"https://schema.org"}</script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#157878">
    <link rel="stylesheet" href="/assets/css/style.css">
	
	</head>
  <body>
    <section class="page-header">
      <h1 class="project-name">Rüyada a görmek</h1>
      <h2 class="project-tagline">Rüya tabiri Rüya yorumu</h2> 
 <a href="https://ruya-tabiri.github.io" rel="dofollow" class="btn">Anasayfa - Duyurular</a> 
 <a href="https://ruya-tabiri.github.io/dizin.html" class="btn" rel="dofollow">Rüya Tabiri Dizin</a>      
    </section>
    <section class="main-content">
      <h2>Rüyada a görmek tabiri</h2>
<p>Rüyada a görmek   toplum tarafından el üstünde tutulacağına,  yaşadığı yerden uzak kalacağına ve özlem çekeceğine,  bereket ve zenginliğe kavuşacağına,  kendi işini kurarak yönetici koltuğuna oturacağına ve rahat bir şekilde gelir elde ederek hayatını idame ettireceğine,  kişi hasta ise ölümün vaki olduğuna,  yakalandığı ağır bir hastalığı yeneceğine ve yapılan işlerin sonunda helal para ve mal kazanılacağına,  gönül işlerinden yana hayır bulacağına,  tabir olur.</p>
<p>Ayrıca rüyada a görmek   zor ve sorunlu bir döneme gireceğine,  geçim için verdiği savaşın kızışacağına,  gönül işlerinden yana hep şanslı olacağı gibi son kararını da isabetli vereceğine ve kendisi için doğru kişiyi bulacağına,  uzun zamandan beri çok istediği şeylere kısa sürede kavuşacağına,  hayatın keyifli bir hale geleceğine,  birbirlerinin sıkıntılarına koşulacağına,  yorumlanır.</p> 
<h2>Dini olarak rüyada a görmek tabiri</h2>
<p>Dini olarak rüyada a görmek   rakiplerin yenilgiye uğratılacağına ve zorlukların kısa süre içinde sona ereceğine,  cebine giren paranın gittikçe azalacağına,  hiçbir hevesinin yarım kalmayacağına,  bu sayede büyük bir özgüven kazanacağına,  iş hayatında büyük bir terfi alınacağına,  işlerle ilgili doğru karar vermek için detaylı bir düşünme yolu seçildiğine,  kendisini insan içine çıkamayacak kadar güçsüz hissedeceğine,  her anlamda neredeyse dört dörtlük sayılacak bir kişi ile yollarının kesişeceğine,  delalet eder.</p>
<h2>Psikolojik olarak rüyada a görmek yorumu</h2>
<p>Psikolojik olarak rüyada a görmek   büyük zarar edeceği bir döneme gireceğine,  tüyü bitmemiş yetimin rızkına göz dikeceğine,  tatmin olacağı oranda gelire kavuşacağına,  hasta olan kişi ile irtibata geçeceğine hatta yanına gidip kendisine her konuda destek olmaya çalışacağına,  atılan bazı adımların çok büyük sorunlara sebep olacağına,  resmi işlemlerinde büyük kolaylıklar yaşayacağına,  sağlıkla ilgili olarak yaşanan sorunların bitirileceğine,  yorumlanır.</p>

<h3 id="support-or-contact">Arama</h3>
<p>Rüya tabiri arayabilirsiniz.</p>
<p><script async src="https://cse.google.com/cse.js?cx=f06af576ee2079108"></script>
<div class="gcse-search"></div></p>
      <footer class="site-footer">        
        <span class="site-footer-credits">Sitemizde yer alan rüya tabirleri size sadece fikir sunmak içindir. Rüya Tabiri © 2021</span>
      </footer>
    </section>    
  </body>
</html>
```

Herhangi bir rüya tabiri için nasıl görünmesini istiyorsanız bu sayfanızı o şekilde düzenleyebilirsiniz. Daha sonra bu şablonu programlama içinde kullanacağız. 

## Rüya tabiri veritabanı hazırlama

Rüya tabiri için sqlite veritabanı yapısı kullandım. Bunu kendiniz hazırlamalısınız veya satın almak isterseniz 200.000 civarında derlediğim özgün rüya tabirleri için iletişime geçebilirsiniz. 

## Rüya tabiri sitesi kod hazırlığı

Rüya tabiri sitesi yapmak için kod hazırlığına başlayabiliriz. Kodumuza başlamadan önce veritabanı hazır ve sqlite3 modülü kullanılabilir durumda olmalıdır. Bunları pip ile kurabilirsiniz. Python3 programlama dili elbette bilgisayarınıza kurulu olmalı.

## Rüya tabiri sayfası ekleme

[sayfaekle.py](https://github.com/ruya-tabiri/ruya-tabiri-sitesi/blob/main/sayfaekle.py) dosyasında paylaştığım kodu kendi ihtiyaçlarınıza göre değiştirerek veritabanından gelen bilgilerle yeni tabirler üretmeye başlayacaksınız. Veritabanında 3 içerik bölümünü kendi ihtiyacınız doğrultusunda genişletebilir veya azaltabilirsiniz. Sayfa eklemekle ilgili sorunlarınızı [issues](https://github.com/ruya-tabiri/ruya-tabiri-sitesi/issues) bölümünde sorabilirsiniz. Bu kod elbette stabil sayfalar üretiyor. Aslında bu da oldukça hızlı web siteleri yapmanıza sebep olur. Dilerseniz kullanacağınız javascript kodlarının adreslerini de sayfa temasına ekleyebilirsiniz. 

