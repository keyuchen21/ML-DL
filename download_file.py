from jupyter_server.serverapp import list_running_servers
import os

# List running servers
servers = list(list_running_servers())
if not servers:
    raise RuntimeError("No running Jupyter server found.")

# Use the first server found
server = servers[0]
jupyter_root = server['root_dir']
print("✅ Jupyter root directory:", jupyter_root)


import os
import pandas as pd
import urllib.parse

# === USER INPUT ===
folder = '/Users/keyu/Library/Mobile Documents/com~apple~CloudDocs/Coding/医药'
token = "2f2bc50c12568f9e45e253646618dc4fdb8dcf394f8baf26"     # paste your Jupyter token here
jupyter_root = "/Users/keyu/Library/Mobile Documents/com~apple~CloudDocs/Coding"  # Jupyter notebook root
base_url = "http://localhost:8888"

# === Generate links ===
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

rows = []
for filename in files:
    full_path = os.path.join(folder, filename)
    
    # Get relative path to Jupyter root
    rel_path = os.path.relpath(full_path, jupyter_root)
    
    # URL-encode the relative path
    encoded_path = urllib.parse.quote(rel_path)
    
    # Build download URL
    download_url = f"{base_url}/files/{encoded_path}?token={token}"
    
    # Build Excel-style HYPERLINK formula
    hyperlink_formula = f'=HYPERLINK("{download_url}", "Download link")'
    
    rows.append({
        "Filename": filename,
        "Download": hyperlink_formula
    })

# === Export to CSV ===
df = pd.DataFrame(rows)
df.to_csv("download_links_with_token.csv", index=False)

print("✅ download_links_with_token.csv created with Excel-friendly links.")
