import { getCollection, type CollectionEntry } from 'astro:content';
import type { Lang } from '../config';

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

export async function translationOf(p: Post) {
  const other: Lang = langOf(p) === 'es' ? 'en' : 'es';
  const list = await postsFor(other);
  return list.find((x) => slugOf(x) === slugOf(p));
}
