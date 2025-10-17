# ⚙️ Error & Solution Logbook

## 🎯 Tujuan
Mencatat setiap masalah penting selama pengembangan agar AI baru tidak mengulang kesalahan yang sama.

---

## 📚 Template Pencatatan
| Tanggal | Modul | Masalah | Penyebab | Solusi | Status |
|----------|--------|----------|-----------|---------|---------|

---

## 🧩 Contoh Kasus
| 2025-10-17 | Rojo Setup | Plugin tidak terbaca di Roblox Studio | Path Plugin salah & versi mismatch | Update ke Rojo 7.6.0, gunakan koneksi otomatis (tanpa URL) | ✅ Solved |
| 2025-10-17 | Git Sync | Push ditolak (`fetch first`) | Repo GitHub sudah punya commit default | Gunakan `git pull origin main --allow-unrelated-histories` | ✅ Solved |
| 2025-10-17 | AI Context Reset | Context hilang setiap sesi baru | Tidak ada penyimpanan reasoning antar sesi | Buat file `03_AI_CONTEXT.md` sebagai persistent context | 🧩 Permanent Fix |

---

## 🧠 Catatan Tambahan
- Semua solusi di sini bisa di-*upgrade*.  
- AI boleh melakukan refactor jika menemukan solusi lebih efisien.  
- Gunakan format ini setiap kali error baru ditemukan.

🕓 **Last Updated:** _2025-10-17_
