# 🔁 Human–AI Sync Protocol

## 🎯 Tujuan
Menjamin kesinambungan antara manusia dan AI lintas sesi.

---

## 🧭 Siklus Kerja
1. **Manusia update ide atau progres baru.**
2. **AI membaca perubahan dan menulis reasoning ke log.**
3. **Jika ada error → catat di `05_ERROR_SOLUTIONS.md`.**
4. **Jika ada keputusan arsitektur → update `04_ARCHITECTURE_DECISIONS.md`.**
5. **AI tambahkan metadata footer.**
6. **Sistem auto-commit ke GitHub.**

---

## ⚙️ Mode Operasi
| Mode | Fungsi |
|------|--------|
| `audit` | Membaca semua dokumen & mencari inkonsistensi. |
| `build` | Menulis laporan & memperbarui progres. |
| `reflect` | Mengevaluasi ide & solusi lama. |

---

## 🧠 Protokol Komunikasi AI
- Semua AI wajib membaca `03_AI_CONTEXT.md` sebelum memulai reasoning.  
- Semua laporan baru harus mengikuti `10_AI_REPORT_TEMPLATES.md`.  
- Semua keputusan atau perubahan harus memiliki **footer metadata resmi**.  
- Tidak boleh ada laporan anonim.

---

## 🧩 Filosofi Sinkronisasi
> “Setiap commit adalah percakapan antara manusia dan AI.”  
> — OVHL Boot Philosophy

---

## 📅 Metadata
| Field | Nilai |
|--------|--------|
| **Versi** | 1.0.0 |
| **Maintainer** | Hanif |
| **AI Role** | System Maintainer |
| **Last Updated** | 2025-10-18 |
