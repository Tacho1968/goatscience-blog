import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://goatscience.ulpgc.es',
  integrations: [sitemap()],
  build: { format: 'directory' },
});
