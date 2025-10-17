import os, re

# ===========================================
# 🧩 OVHL_NextGen Link Validator
# Deteksi link markdown rusak antar dokumen
# ===========================================

def find_md_links(path):
    md_links = re.compile(r'\[.*?\]\((.*?)\)')
    broken = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                with open(full_path, encoding="utf-8") as f:
                    content = f.read()
                    for link in md_links.findall(content):
                        if link.endswith(".md"):
                            linked_file = os.path.join("Docs", os.path.basename(link))
                            if not os.path.exists(linked_file):
                                broken.append((file, link))
    return broken

broken = find_md_links("Docs")

if broken:
    print("\n⚠️  Link rusak terdeteksi:\n")
    for src, link in broken:
        print(f"  • {src} → {link}")
else:
    print("✅ Semua link internal OK!")
