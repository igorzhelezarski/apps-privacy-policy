# Privacy policies

Privacy policy pages for apps and games published by Reimagined Bits, served with GitHub Pages.

| Page | URL |
|---|---|
| Index of all apps | https://igorzhelezarski.github.io/apps-privacy-policy/ |
| Whack It World | https://igorzhelezarski.github.io/apps-privacy-policy/whack-it-world/ |
| Fading Tic-Tac-Toe | https://igorzhelezarski.github.io/apps-privacy-policy/fading-tic-tac-toe/ |
| Cat Tower | https://igorzhelezarski.github.io/apps-privacy-policy/cat-tower/ |
| Bloomgrid | https://igorzhelezarski.github.io/apps-privacy-policy/bloomgrid/ |
| Arrows Escape | https://igorzhelezarski.github.io/apps-privacy-policy/arrows-escape/ |

Plain HTML with one shared stylesheet (`assets/style.css`) and self-hosted fonts (Nunito and Lilita One,
SIL Open Font License, in `assets/fonts/`). No build step.

## Adding a new game or app

1. Copy `_template/` to a new folder named after the game or app, for example `my-new-game/`.
2. Add the app's images to `my-new-game/img/`: `icon.png` (256×256), `icon-64.png`, `feature.jpg`
   (the 1024×500 Play feature graphic) and a few phone screenshots as `shot-*.jpg`, resized to
   540 px wide.
3. Fill in every `[BRACKETED]` value, delete the sections the app does not need, and remove the
   `noindex` line.
4. In `index.html`, copy an `<article class="product-card">` block into the `catalog` under
   **Our games** or **Our apps** and change it (set `<span class="kind">` to "Board game",
   "Productivity app" and so on). Then add a line to the **Privacy policies** list and a footer link.
   Remove the "Apps are on the way" placeholder when the first app is added.
   Optional: give the policy page's `<body>` a color theme such as `theme-blue`
   (themes live at the end of the catalog styles in `assets/style.css`).
5. Merge to `main`. The page is live at `https://igorzhelezarski.github.io/apps-privacy-policy/my-new-game/`
   within a minute or two. Give that URL to Google Play and the App Store.

Each store needs a policy that describes that app's own data practices, so every app gets its own
page rather than sharing one general policy.

## Updating a policy

Edit the app's `index.html`, change the "Last updated" date, and merge. The URL stays the same, so
nothing needs to change in the store listings.

## Firebase Hosting

The same pages are also published on Firebase Hosting (project `reimagined-bits`): the index at
https://reimagined-bits.web.app and each policy on its own site, for example https://cat-tower-site.web.app.
Every site gets `app-ads.txt`.

1. For a new app, create its Hosting site once (`firebase hosting:sites:create my-new-game-site`) and add
   it to `firebase/sites.json`.
2. Run `python3 firebase/build.py`. It writes `firebase/dist/` with the links between pages pointing at
   the Firebase addresses, plus `firebase/firebase.json` and `firebase/.firebaserc`.
3. From `firebase/`, run `firebase deploy --only hosting`.
