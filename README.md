# petit-chaton.com

猫モチーフのジュエリーブランド「Petit Chaton（プチシャトン）」の公式サイト。
**Astro（SSG）による完全静的サイト**で、GitHub Pages にホスティングしています。

公開URL: https://petit-chaton.com

## 技術スタック

- **Astro 6**（静的サイト生成 / SSG）
- 素のCSS（フレームワーク不使用 — 依存最小・保守容易）
- `@astrojs/sitemap`（sitemap 自動生成）
- 画像は `<picture>` で **avif → webp → jpg** を出し分け

## 開発

```bash
npm install
npm run dev       # http://localhost:4321 で確認
npm run build     # dist/ に静的出力
npm run preview   # ビルド結果をローカル配信
```

## 主なファイル

| パス | 役割 |
|---|---|
| `src/pages/index.astro` | 本文（ヘッダー / COLLECTION / CONCEPT / フッター） |
| `src/layouts/Layout.astro` | `<head>`（title・description・OGP・JSON-LD・canonical・favicon） |
| `src/styles/global.css` | 配色・タイポグラフィ（`--olive-ink: #6f7038` はアクセシブルな文字色） |
| `public/images/` | 画像。**すべて width/height を指定**（CLS=0 を維持） |
| `public/CNAME` | カスタムドメイン設定。**削除しない** |
| `astro.config.mjs` | `base` は `/`（apexドメイン配信） |

## デプロイ

`main` ブランチへ push すると、GitHub Actions（`.github/workflows/deploy.yml`）が
自動でビルド・デプロイします。

- `withastro/action@v3`（**`node-version: 22` 必須** — 20以下はビルド失敗）
- → `actions/deploy-pages@v4`
- Settings → Pages：Source = GitHub Actions / Custom domain = petit-chaton.com / Enforce HTTPS = ON

## ドメイン / DNS 運用メモ

- DNSは外部で管理。apex の A レコードは GitHub Pages IP（`185.199.108`〜`111.153`）、
  `www` は CNAME → `hayaboosan.github.io`。
- ⚠️ **Web向けの A / CNAME は必ず「DNS only（プロキシ無効）」にする。**
  CDNプロキシ経由にすると GitHub の HTTPS 証明書発行が失敗する。
- ⚠️ **メールの MX / SPF(TXT) レコードは変更・削除しない。**
- 証明書が発行されない場合：Settings → Pages の Custom domain を **Remove → 再入力**して
  発行を再トリガーする。

---

旧サイト（Vue/Vite SPA）からの移行記録・診断・計測結果は、制作側の引き継ぎ資料を参照。
