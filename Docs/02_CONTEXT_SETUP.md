# ⚙️ Context Setup – OVHL_NextGen
> Panduan agar AI memahami konteks proyek, gaya komunikasi, dan workflow sistem.

---

## 🧠 Tujuan
File ini menjelaskan cara AI membaca, memahami, dan beroperasi di lingkungan OVHL_NextGen.  
AI tidak boleh berjalan “buta konteks” — ia harus membaca dokumen ini **setiap kali proyek dimulai atau direboot.**

---

## 📂 File Prioritas yang Harus Dibaca AI
1. `Docs/00_README.md` → Peta navigasi dokumentasi.  
2. `Docs/01_PANDUAN_PROYEK.md` → Filosofi dan arah pengembangan.  
3. `Docs/03_AI_CONTEXT.md` → Aturan dan perilaku kerja AI.  
4. `Docs/05_ERROR_SOLUTIONS.md` → Riwayat error & pembelajaran.  
5. `Docs/07_PROGRESS_TRACKER.md` → Status terkini proyek.

---

## 🧩 Mode Kerja AI
| Mode | Deskripsi |
|------|------------|
| **Bootloader Context** | Mode inisialisasi awal, AI membaca semua dokumen inti sebelum interaksi. |
| **Memory Recall** | Mode di mana AI membaca ulang error, progres, dan ide sebelumnya sebelum bertindak. |
| **Start-From-Zero** | Mode “reboot” di mana AI membangun ulang proyek dari dokumentasi, bukan dari file lama. |

---

## ⚙️ Workflow AI ↔ Human
1. Hanif memulai sesi dengan instruksi atau topik.  
2. AI membaca konteks dari `Docs/` untuk mengetahui state terakhir.  
3. AI memberikan saran, solusi, atau dokumentasi baru.  
4. Semua pembaruan dicatat otomatis:
   - Error → `05_ERROR_SOLUTIONS.md`
   - Ide → `08_IDEAS_BACKLOG.md`
   - Update → `07_PROGRESS_TRACKER.md`

---

## 🧰 Integrasi Lingkungan
| Tool | Fungsi |
|------|---------|
| **VS Code** | IDE utama pengembangan |
| **Rojo** | Bridge VS Code ↔ Roblox Studio (port default: 34872) |
| **GitHub** | Repository utama & version control |
| **Stylua + Selene** | Formatter & linter otomatis |
| **AI Assistant** | Partner dokumentasi, ideasi, dan logika arsitektur |

---

## 💬 Gaya Komunikasi
- Gunakan Bahasa Indonesia + istilah teknis.
- Sertakan emoji untuk konteks progress:
  🔥 aktif • ⚙️ proses • ✅ selesai • ❌ error.
- Gunakan heading dan tabel untuk struktur yang jelas.
- Fokus pada kejelasan dan efisiensi, bukan panjang lebar.

---

## 🧭 Panduan Reset (Start From Zero)
Jika proyek direboot:
1. AI harus memastikan semua dokumen di `Docs/` lengkap.  
2. Gunakan dokumentasi sebagai blueprint utama, bukan file lama.  
3. Rekonstruksi struktur kerja (`src/`, `tools/`, `default.project.json`).  
4. Catat hasil inisialisasi ulang di `07_PROGRESS_TRACKER.md`.

---

## 📅 Metadata
| Field | Nilai |
|--------|--------|
| **Version** | 0.2.0 |
| **Status** | Active |
| **Maintainer** | Hanif |
| **AI Mode** | Bootloader Context + Memory Recall |
