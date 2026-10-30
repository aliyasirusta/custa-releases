# Custa · Kullanım rehberi

[← Custa ana sayfası](../README.md)

## Kurulum

1. Releases sayfasındaki **Assets** bölümünden `Custa-X.Y.Z-macos-universal.zip` dosyasını indir. `Source code` ve `.sha256` dosyaları uygulama değildir.
2. ZIP’i aç. **Custa.app**, ZIP’in açıldığı klasöre (genellikle İndirilenler) çıkar. Otomatik taşıma veya kurulum ekranı yoktur.
3. Kalıcı kurulum ve uygulama içi güncellemeler için Custa kapalıyken Finder’da **Custa.app’i Uygulamalar klasörüne elle taşı**, ardından oradan aç. `~/Applications` da desteklenir.
4. İlk kullanımda **Başla**ya bas. Sonrasında menü çubuğu simgesi veya **⌥⌘V** ile aç.

İndirilenler’den de çalıştırabilirsin; uygulama içi güncellemeler için önce Uygulamalar’a taşıyıp oradan yeniden açman gerekir. Taşıma geçmişini ve şifrelerini silmez. ZIP arşivini daha sonra kaldırabilirsin.

**Ön sürüm / Apple güvenlik uyarısı:** Paket ad-hoc imzalıdır; Apple Developer ID imzası ve noter onayı henüz yoktur. macOS ilk açılışı engellerse, yalnızca bu resmi repodan indirdiğine güveniyorsan, açmayı denedikten sonra **Sistem Ayarları → Gizlilik ve Güvenlik → Yine de Aç** yolunu kullan. Mac oturum parolan veya Touch ID istenebilir. Sistem genelinde güvenliği kapatmak gerekmez. Uygulamayı elle taşımak macOS güvenlik denetimini atlamaz.

## Güncelleme

**Custa ayarları → Güncellemeleri denetle…** yeni sürümü bulur. Sparkle imzalı paketi doğrular, onayınla yükler ve Custa’yı yeniden açar. Her sürümde ZIP indirmen gerekmez. Otomatik denetleme isteğe bağlıdır; otomatik yükleme kapalıdır. Liste kısa süre önbellekte kalabilir; yeni yayın görünmüyorsa birkaç dakika sonra yeniden dene.

## Günlük kullanım

- Metin veya görsel satırına tıkla ya da seçip **Enter**a bas: panoya kopyalanır. Hedef uygulamada **⌘V** ile yapıştır; otomatik yapıştırma yapılmaz.
- Arama metin ve tamamlanan OCR sonuçlarında çalışır. Filtreler: **Tümü, Metinler, Görseller, Sabitlenenler, Şifreler**.
- Kaydın üzerinde bekle veya klavyeyle seçip **Space**e bas: büyük önizleme açılır. Görsel düzenlemek için **… → Düzenle** kullan.
- Başlıktaki pencere düğmesi taşınabilir serbest pencereyi açar. Alt köşelerden oranı korunarak boyutlandır; iğne düğmesiyle üstte tut.
- Menü paneli imlecin bulunduğu ekranın sağ üstünde açılır. Ayarlarda **Saydam** (varsayılan) veya **Koyu** seçebilirsin.
- Alttaki duraklat düğmesi pano ve ekran görüntüsü takibini durdurur.

## Varsayılan kısayollar

| İşlem | Kısayol | Kapsam |
|---|---|---|
| Aç / kapat | ⌥⌘V | Her uygulamada |
| Şifre üretici | ⌥⌘P | Her uygulamada |
| Serbest pencere | ⌥⇧⌘D | Her uygulamada |
| Ara | ⌘F | Custa içinde |
| Ayarlar | ⌘, | Custa içinde |
| Pencereyi üstte tut / bırak | ⇧⌘P | Serbest pencerede |
| Seçili kaydı sabitle / bırak | ⇧⌘S | Geçmiş listesinde |
| Seçili kaydı sil | ⌥⌘⌫ | Geçmiş listesinde |
| İlk dokuz kaydı kopyala | ⌘1–9 | Geçmiş listesinde |
| Gezin / kopyala / önizle | ↑↓ / Enter / Space | Geçmiş listesinde |

İlk sekiz kısayol **Ayarlar → Klavye kısayolları** bölümünden değiştirilebilir. Arama yazarken Space normal boşluk girer; ↑↓ ile kayıt seçtikten sonra önizleme açar. Editörde ⌘Z geri alır, ⇧⌘Z yineler, Delete seçili şekli siler.

## İzinler ve gizlilik

- Ekran görüntülerine ulaşmak için macOS dosya/klasör erişimi isteyebilir. Custa ekranı sürekli kaydetmez; dosyaya veya panoya ulaşan görüntüleri algılar. Ekran Kaydı izni bu akış için gerekli değildir.
- Algılama macOS ekran görüntüsü işaretleri, Spotlight ve sistem kayıt konumuna dayanır. İzin verilmeyen veya indekslenmeyen konumlar ve bazı üçüncü taraf yakalamaları eksik kalabilir. **Eski görüntüleri içe aktar** en yeni 300 eski görüntüyü isteğinle alır.
- Açılışta başlatma isteğe bağlıdır; macOS giriş öğesi onayı isteyebilir.
- Şifreler ve açıklamaları **macOS Anahtar Zinciri**nde saklanır. macOS erişim onayı/oturum parolası isteyebilir; imza değişikliklerinde onay tekrar çıkabilir.
- Pano geçmişi, görseller ve editör taslakları yerelde **şifrelenmeden** saklanır. Hariç tutulan uygulama filtresi kesin bir güvenlik sınırı değildir; hassas içeriği gerektiğinde ayrıca sil.
- OCR, Base64 ve diff cihaz üzerinde çalışır. Güncelleme denetimi GitHub’a bağlanır; pano verileri gönderilmez. Telemetri yoktur.

## Veriler nerede, nasıl silinir?

| Veri | Konum / silme |
|---|---|
| Geçmiş, görseller, yakalama durumu, taslaklar | `~/Library/Application Support/Custa` |
| Şifreler ve açıklamalar | Anahtar Zinciri: **Custa · Şifreler** |
| Görünüm ve kısayol tercihleri | macOS uygulama tercihleri: `local.custa.clipboard` |

- **Tek kayıt:** kaydın **… → Sil** menüsü. Şifre silmek için **Şifreler → … → Sil** kullan. Pano geçmişindeki ayrı kopyası varsa o ayrıca silinmelidir.
- **Geçmişi temizle:** **Ayarlar → Sabitlenmeyen geçmişi temizle…**. Sabitlenenler, şifreler ve taslaklar korunur; bunları ayrıca sil.
- **Taslaklar:** **Ayarlar → Taslakları aç…**; açık editörü kapattıktan sonra ilgili taslağı Çöp Sepeti’ne taşı.
- **Tüm yerel geçmişi sıfırla:** önce Custa’dan çık. Finder’da **Git → Klasöre Git…** ile yukarıdaki Application Support yolunu açıp Custa klasörünü Çöp Sepeti’ne taşı. Bu işlem geçmişi, Custa’nın görsel kopyalarını ve taslaklarını kaldırır; orijinal ekran görüntüsü dosyalarını ve Anahtar Zinciri şifrelerini silmez. Yeniden açmadan önce geri alırsan klasörü geri koyabilirsin.
- **Tüm şifreleri sil:** Custa’dan çık, **Anahtar Zinciri Erişimi**nde `Custa · Şifreler` kaydını bulup yalnızca bu kaydı sil. Bu Custa şifre kitaplığının tamamını siler; onay istenebilir. Diğer Anahtar Zinciri kayıtlarına dokunma.
- **Uygulamayı kaldır:** önce açılışta başlatmayı ayarlardan kapat, Custa’dan çık ve kurulu Custa.app’i Çöp Sepeti’ne taşı. Uygulamayı kaldırmak verileri kendiliğinden silmez.

Kayıt silmek macOS’un o anki panosunu boşaltmaz. Panoda hassas içerik kaldıysa zararsız başka bir metin kopyala. Çöp Sepeti, yedekler ve diğer pano uygulamalarındaki kopyalar ayrıca kalabilir.

## Araçlar ve bilinen sınırlar

**Metin:** … menüsünden Base64 dönüştür/çöz ve iki kayıt arasında karşılaştırma. Diff penceresindeki iki alan düzenlenebilir; ⌘Enter ile karşılaştırılır. Sınır: metin başına 5.000 satır, toplam 1 MB.

**Görsel:** seç/taşı/boyutlandır, kalem, çizgi, ok, dikdörtgen, daire, metin, kırp ve opak kapatma. Renk paleti editör içinde açılır. PNG kaydet, kopyala veya geçmişe ekle; orijinal dosya değişmez. Taslaklar düzenlenebilir şekilleri korur. PNG’ye gömülmüş eski çizimler ayrı nesne değildir.

**Şifre:** anahtar düğmesi üreticiyi aynı panelde açar. Uzunluk 8–128; Yeni şifre üret yalnızca önizler, **Kopyala** kaydeder. Metin kaydından Şifrelere ekle açıklama ister; orijinal pano kaydını kaldırmaz.

**Kapasite:** en fazla 300 sabitlenmemiş kayıt; sabitlenenler ayrıca korunur. Metin saklama süresi ve görsel disk sınırı ayarlanabilir. OCR her yazıyı doğru tanımayabilir. Arka plan görsel işleme ve küçük önizleme önbelleği kullanılır; bunlar toplam RAM sınırı veya kesintisiz performans garantisi değildir.

**Açılış sorunu:** macOS güvenlik uyarısını yukarıdaki adımlarla kontrol et. Güncelleme kullanılamıyorsa Custa’dan çık, Uygulamalar’a elle taşı ve oradan yeniden aç.
