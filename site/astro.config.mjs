// @ts-check
import svelte from '@astrojs/svelte';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

// Standalone: https://anavaratha.intuituilabs.studio (base "/").
// Subpath mode: ANAVARATHA_BASE=/projects/anavaratha/atlas-site pnpm build
export default defineConfig({
  site: process.env.ANAVARATHA_SITE ?? 'https://anavaratha.intuituilabs.studio',
  base: process.env.ANAVARATHA_BASE ?? '/',
  trailingSlash: 'ignore',
  vite: { plugins: [tailwindcss()] },
  integrations: [svelte()],
});
