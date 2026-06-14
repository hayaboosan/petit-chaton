import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://petit-chaton.com',
  integrations: [sitemap()],
});
