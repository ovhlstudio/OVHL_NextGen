# 🏗️ Architecture Decisions Log (ADL)

## 📖 Purpose
Dokumen ini berfungsi sebagai catatan “kenapa sesuatu dibuat seperti itu” — bukan hanya “bagaimana cara membuatnya”.

---

## 🧠 Arsitektur Utama: OVHL_NextGen OS

| Komponen | Deskripsi | Alasan Utama | Status |
|-----------|------------|---------------|---------|
| **OVHL_NextGen Root** | Boot Engine & Kernel System | Centralized OS management | ✅ Stable |
| **OVHL_Modules Root** | Standalone Applications Folder | Clear separation from OS | ✅ Core |
| **OVHL_Shared Root** | Cross-system Communication | Centralized event system | ✅ Stable |
| **Bootstrap System** | Auto-installation Engine | Enable drag & play experience | 🔥 Active Development |
| **Visual Guide System** | Big Screen Tutorial | Eliminate user confusion | 🔥 Active Development |

---

## 🔍 Prinsip Umum
1. **Scalable Thinking** – Semua module dibuat dengan asumsi akan tumbuh.
2. **Human-AI Collaboration** – Tiap keputusan punya alasan yang bisa dipahami AI baru.
3. **Fail-Forward System** – Error bukan kegagalan, tapi bahan pembelajaran dokumentatif.
4. **Decentralized Docs** – Semua log & solusi hidup di file markdown agar mudah diakses oleh AI atau manusia.

---

## 🔄 Iterasi dan Evolusi
- Setiap perubahan besar → catat alasan dan tanggal di bawah.
- AI baru harus membaca dokumen ini dulu sebelum bekerja.

### 🏗️ Multi-Root Architecture Decision

**[2024-07-09] - Multi-Root Separation**

**Masalah / Tantangan:** Semua komponen OVHL sebelumnya berada dalam satu root folder, menyebabkan:
- Kesulitan membedakan OS engine vs user applications
- Creator confusion tentang file ownership
- Sulit maintenance dan updates

**Keputusan:** Implementasi multi-root architecture dengan clear separation:
```

ServerStorage/
├── 🖥️ OVHL\_NextGen/     ← OS Engine (100% OVHL)
├── 📦 OVHL\_Modules/     ← Applications (Creator/OVHL)
└── 🔧 OVHL\_Shared/      ← System Resources (100% OVHL)

```

**Alasan:** - **Clear Ownership** - Creator tahu mana OS, mana aplikasi
- **Independent Development** - Modules bisa develop terpisah dari OS
- **Easy Management** - Bisa delete modules tanpa sentuh OS
- **Scalable** - Bisa nambah ribuan modules tanpa ubah architecture

**Alternatif yang Dipertimbangkan:** - Single root folder (ditolak - terlalu messy)
- Plugin-based system (ditolak - terlalu complex untuk creator)

**Status:** ✅ Diterapkan

---

### 🚀 Bootstrap System Design

**[2024-07-09] - First-Mover Bootstrap Strategy**

**Masalah / Tantangan:** Standalone modules tidak bisa auto-execute di Roblox environment. Creator harus manually pindahkan scripts ke location yang benar.

**Keputusan:** Implementasi "First-Mover Bootstrap System":
- Setiap module mengandung Bootstrap Script
- Module pertama installs OVHL_Bootstrap ke ServerScriptService
- Module berikutnya auto-terkelola oleh existing bootstrap
- Zero manual setup setelah initial install

**Alasan:** - **True Drag & Play** - Creator experience seamless
- **Progressive** - System installs itself
- **Future-Proof** - Compatible dengan OS enhancement
- **User-Friendly** - No technical knowledge required

**Technical Implementation:**
```lua
-- Bootstrap auto-places components:
ModuleScripts → ServerScriptService
LocalScripts → StarterPlayerScripts  
Modules → OVHL_Modules folder
```

**Alternatif yang Dipertimbangkan:** - Manual placement (ditolak - poor user experience)

  - Workspace execution (ditolak - messy dan unprofessional)

**Status:** 🧩 Dalam Uji Coba

-----

### 🖥️ Visual Guide Integration

**[2024-07-09] - Big Screen Tutorial System**

**Masalah / Tantangan:** Creator pemula sering bingung dengan README documentation dan technical setup instructions.

**Keputusan:** Implementasi Visual Guide System:

  - Big Screen Part auto-place di workspace
  - Multi-language tutorial texts
  - Context-aware messages (new vs experienced users)
  - Self-cleanup setelah successful installation

**Alasan:** - **Visual Learning** - Lebih efektif dari text documentation

  - **Instant Expertise** - User jadi expert dalam 5 menit
  - **Professional Polish** - Enterprise-grade user experience
  - **Zero Confusion** - Eliminate setup frustration

**Implementation Details:**

  - Guide muncul saat module pertama kali di-insert
  - Different messages untuk new vs returning users
  - Auto-destroy setelah bootstrap successful
  - Multi-language support (ID/EN)

**Alternatif yang Dipertimbangkan:** - Text documentation (ditolak - sering tidak dibaca)

  - Video tutorials (ditolak - tidak integrated)

**Status:** 🧩 Dalam Uji Coba

-----

## 📅 Metadata

**Last Major Revision:** 2024-07-09 - Multi-Root Architecture & Bootstrap System  
**Key Innovations:** Drag & Play Experience, Visual Guidance, Clear Revenue Boundaries

