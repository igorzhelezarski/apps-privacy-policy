"""Builds the Firebase Hosting copy of the site into firebase/dist/.

The index becomes its own Hosting site (reimagined-bits.web.app) and every app policy gets its
own site (for example cat-tower-site.web.app), as listed in sites.json. Links between the pages
are rewritten to those addresses, and app-ads.txt goes into every site.
Also writes firebase.json and .firebaserc next to dist/, so `firebase deploy --only hosting`
can run from this folder. Standard library only: `python3 firebase/build.py`.
"""
import json, re, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DIST = HERE / "dist"
cfg = json.loads((HERE / "sites.json").read_text())
url = lambda site: f"https://{site}.web.app/"
HUB = url(cfg["hub"]["site"])
apps = cfg["apps"]

shutil.rmtree(DIST, ignore_errors=True)

def common(dest):
    shutil.copytree(ROOT / "assets", dest / "assets")
    shutil.copy(ROOT / "app-ads.txt", dest / "app-ads.txt")

# Index site
hub = DIST / "hub"
common(hub)
html = (ROOT / "index.html").read_text(encoding="utf-8")
for slug, a in apps.items():
    shutil.copytree(ROOT / slug / "img", hub / slug / "img")
    html = html.replace(f'href="{slug}/"', f'href="{url(a["site"])}"')
(hub / "index.html").write_text(html, encoding="utf-8")

# One site per app
targets = [{"target": "hub", "public": "dist/hub", "cleanUrls": True}]
for slug, a in apps.items():
    d = DIST / a["target"]
    common(d)
    shutil.copytree(ROOT / slug / "img", d / "img")
    page = (ROOT / slug / "index.html").read_text(encoding="utf-8")
    page = page.replace('"../assets/', '"assets/').replace('href="../#', f'href="{HUB}#').replace('href="../"', f'href="{HUB}"')
    left = re.findall(r'(?:href|src)="\.\./[^"]*"', page)
    assert not left, f"{slug}: unrewritten links {left}"
    (d / "index.html").write_text(page, encoding="utf-8")
    targets.append({"target": a["target"], "public": f"dist/{a['target']}", "cleanUrls": True})

(HERE / "firebase.json").write_text(json.dumps({"hosting": targets}, indent=2) + "\n")
(HERE / ".firebaserc").write_text(json.dumps({
    "projects": {"default": "reimagined-bits"},
    "targets": {"reimagined-bits": {"hosting": {"hub": [cfg["hub"]["site"]], **{a["target"]: [a["site"]] for a in apps.values()}}}},
}, indent=2) + "\n")
print("Built", ", ".join(["hub"] + [a["target"] for a in apps.values()]), "in", DIST)
