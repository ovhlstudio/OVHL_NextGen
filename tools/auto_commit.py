import os, datetime

# ===========================================
# 🤖 OVHL_NextGen Auto Commit Utility
# Commit otomatis setiap perubahan terdeteksi
# ===========================================

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.system("git add .")
os.system(f'git commit -m "auto: update OVHL_NextGen docs ({now})"')
os.system("git push")

print(f"✅ Auto-commit berhasil dijalankan pada {now}")
