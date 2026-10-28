<div align="center">
<img src="assets/app-icon.png" width="96" height="96" alt="Custa">
<h1>Custa</h1>
<p>Kopyaladıkların ve yakaladıkların, elinin altında.</p>
<p>macOS için pano geçmişi, ekran görüntüleri, OCR, Base64, diff ve görsel düzenleme.</p>
</div>

## İndir

**[Mac uygulamasını indir → Releases](https://github.com/aliyasirusta/custa-releases/releases)**

macOS 14+ · Intel ve Apple Silicon için tek Universal paket.

ZIP'i açıp Custa.app dosyasını çalıştırın. 0.4.2 ve üstünde ilk açılıştaki **Uygulamalar’a taşı ve aç** düğmesi kurulumu ve doğru konumdan yeniden açılmayı tamamlar. Uygulama kapatılmadan önce açık görsel düzenlemelerinizi kaydedin. Elle kurmak isterseniz Custa.app dosyasını Uygulamalar klasörüne taşıyabilirsiniz. Uygulama menü çubuğunda çalışır; ⌥⌘V kısayoluyla açılır.

## Uygulama içinden güncelleme

0.4.0 ve üstünde **Ayarlar → Güncellemeleri denetle…** düğmesini kullanın. Yeni sürüm bulunduğunda Sparkle, paketi doğrular ve onayınızla yükleyip uygulamayı yeniden başlatır. Otomatik kontrol isteğe bağlıdır; otomatik yükleme kapalıdır.

0.3.0 ve önceki sürümlerden geçerken ilk kez 0.4.0'ı elle kurmanız gerekir. Yerel Custa geçmişiniz korunur.

## Dağıtım ve gizlilik

Bu repo yalnızca derlenmiş uygulama paketleri, imzalı güncelleme listesi, sürüm notları ve dağıtım otomasyonunu içerir. Uygulamanın Swift kaynak kodu, pano içeriği, ekran görüntüsü geçmişi ve özel anahtarlar bulunmaz.

Güncellemeler Ed25519 ile, güncelleme listesi de Sparkle tarafından imzalanır. Doğrulama için yalnızca açık anahtar yayınlanır. Otomatik kontrol açıldığında veya siz denetleme düğmesine bastığınızda GitHub'a bağlanılır; pano verileri gönderilmez.

**Ön sürüm:** Apple Developer ID ve noter onayı henüz yoktur. macOS ilk açılışta güvenlik uyarısı gösterebilir. Kaynağa güveniyorsanız Sistem Ayarları → Gizlilik ve Güvenlik bölümündeki “Yine de Aç” seçeneği kullanılabilir. Sistem genelinde güvenlik ayarlarını kapatmayın.

Uygulama ücretsiz indirilebilir; bu dağıtım reposu kaynak kod lisansı sağlamaz.
