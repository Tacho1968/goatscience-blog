import { getCollection, type CollectionEntry } from 'astro:content';
import { LANGS, type Lang } from '../config';

export type Post = CollectionEntry<'resumenes'>;

export const langOf = (p: Post) => p.id.split('/')[0] as Lang;
export const slugOf = (p: Post) => p.id.split('/').slice(1).join('/');
export const urlOf = (p: Post) => `/${langOf(p)}/${slugOf(p)}/`;

export async function postsFor(lang: Lang) {
  const all = await getCollection(
    'resumenes',
    (p) => langOf(p) === lang && (import.meta.env.DEV || !p.data.borrador),
  );
  return all.sort((a, b) => b.data.fecha.valueOf() - a.data.fecha.valueOf());
}

/** Versiones del mismo resumen en los otros idiomas (solo las que existen). */
export async function translationsOf(p: Post) {
  const out: Partial<Record<Lang, Post>> = {};
  for (const l of LANGS) {
    if (l === langOf(p)) continue;
    const found = (await postsFor(l)).find((x) => slugOf(x) === slugOf(p));
    if (found) out[l] = found;
  }
  return out;
}
