# Privacy policies

Privacy policy pages for apps and games published by Reimagined Bits, served with GitHub Pages.

| Page | URL |
|---|---|
| Index of all apps | https://igorzhelezarski.github.io/apps-privacy-policy/ |
| Whack It World | https://igorzhelezarski.github.io/apps-privacy-policy/whack-it-world/ |

Plain HTML with one shared stylesheet (`assets/style.css`) and self-hosted fonts (Nunito and Lilita One,
SIL Open Font License, in `assets/fonts/`). No build step.

## Adding a new app

1. Copy `_template/` to a new folder named after the app, for example `my-new-game/`.
2. Add the app's images to `my-new-game/img/`: `icon.png` (256×256), `icon-64.png`, `feature.jpg`
   (the 1024×500 Play feature graphic) and a few phone screenshots as `shot-*.jpg`, resized to
   540 px wide.
3. Fill in every `[BRACKETED]` value, delete the sections the app does not need, and remove the
   `noindex` line.
4. Add a game card to `index.html`: copy the `<article class="game-card">` block and change it.
5. Merge to `main`. The page is live at `https://igorzhelezarski.github.io/apps-privacy-policy/my-new-game/`
   within a minute or two. Give that URL to Google Play and the App Store.

Each store needs a policy that describes that app's own data practices, so every app gets its own
page rather than sharing one general policy.

## Updating a policy

Edit the app's `index.html`, change the "Last updated" date, and merge. The URL stays the same, so
nothing needs to change in the store listings.
