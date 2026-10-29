import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { LANGS, SITE, type Lang } from '../../config';
import { t } from '../../i18n';
import { postsFor, urlOf } from '../../lib/posts';

export function getStaticPaths() {
  return LANGS.map((lang) => ({ params: { lang } }));
}

export async function GET(context: APIContext) {
  const lang = context.params.lang as Lang;
  const posts = await postsFor(lang);
  return rss({
    title: `${SITE.title} (${t[lang].langName})`,
    description: t[lang].description,
    site: context.site!,
    customData: `<language>${lang}</language>`,
    items: posts.map((p) => ({
      title: `${t[lang].issue} ${p.data.numero}: ${p.data.titulo}`,
      pubDate: p.data.fecha,
      description: p.data.idea,
      link: urlOf(p),
      categories: p.data.etiquetas,
    })),
  });
}
