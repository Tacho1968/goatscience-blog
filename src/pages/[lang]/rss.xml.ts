import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import MarkdownIt from 'markdown-it';
import sanitizeHtml from 'sanitize-html';
import { LANGS, SITE, LICENSE, type Lang } from '../../config';
import { t } from '../../i18n';
import { postsFor, urlOf } from '../../lib/posts';

const md = new MarkdownIt();
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function getStaticPaths() {
  return LANGS.map((lang) => ({ params: { lang } }));
}

export async function GET(context: APIContext) {
  const lang = context.params.lang as Lang;
  const s = t[lang];
  const posts = await postsFor(lang);
  return rss({
    title: `${SITE.title} (${s.langName})`,
    description: s.description,
    site: context.site!,
    xmlns: { dc: 'http://purl.org/dc/elements/1.1/' },
    customData: `<language>${lang}</language><copyright>${esc(s.licenseFeed)}</copyright>`,
    items: posts.map((p) => {
      const a = p.data.articulo;
      const link = a.doi ? `https://doi.org/${a.doi}` : a.url;
      // Texto completo: referencia del artículo original + resumen + licencia.
      const ref = `<p><strong>${s.paper}:</strong> ${esc(a.autores)} (${a.anio}). ${esc(a.titulo)}. <em>${esc(a.revista)}</em>.${
        link ? ` <a href="${link}">${esc(a.doi ? `https://doi.org/${a.doi}` : link)}</a>` : ''
      }</p>`;
      const body = md.render(p.body ?? '');
      const lic = `<p>${esc(s.licenseText)} <a href="${LICENSE.url}">${LICENSE.name}</a>.</p>`;
      return {
        title: `${s.issue} ${p.data.numero}: ${p.data.titulo}`,
        pubDate: p.data.fecha,
        description: p.data.idea,
        content: sanitizeHtml(ref + body + lic, {
          allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
        }),
        link: urlOf(p),
        categories: p.data.etiquetas,
        customData: `<dc:creator>${esc(SITE.author)}</dc:creator>`,
      };
    }),
  });
}
