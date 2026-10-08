import base64, re

# Read your photo
with open("mona.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

# Read the HTML
with open("samarth_art_studio.html") as f:
    html = f.read()

# Replace the avatar
new_img = f'<img src="data:image/jpeg;base64,{b64}" alt="Mona" style="width:100%; height:100%; object-fit:cover; object-position:center top;">'
html = re.sub(r'<img src="data:image/svg\+xml;base64,[^"]*" alt="Illustrated portrait of Mona, the artist"[^>]*>', new_img, html)

# Save
with open("samarth_art_studio_new.html", "w") as f:
    f.write(html)

print("Done! Open samarth_art_studio_new.html to see your updated site.")
