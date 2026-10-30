// Ajustes generales del blog. Cambia aquí los textos y la suscripción.

export const LANGS = ['es', 'en'] as const;
export type Lang = (typeof LANGS)[number];

export const SITE = {
  title: 'Goat Science',
  author: 'Anastasio Argüello',
  orcid: 'https://orcid.org/0000-0002-4426-0678',
};

// Licencia de los resúmenes (necesaria para Rogue Scholar).
export const LICENSE = {
  name: 'CC BY 4.0',
  url: 'https://creativecommons.org/licenses/by/4.0/',
};

// SUSCRIPCIÓN POR CORREO
// Por ahora la suscripción es manual: los lectores escriben a esta dirección
// y el boletín se envía a mano cada semana, siempre en copia oculta (CCO).
export const SUBSCRIBE_EMAIL = 'tacho@ulpgc.es';

// Direcciones de las páginas fijas en cada idioma.
export const ROUTES: Record<'archive' | 'about' | 'privacy', Record<Lang, string>> = {
  archive: { es: '/es/archivo/', en: '/en/archive/' },
  about: { es: '/es/acerca/', en: '/en/about/' },
  privacy: { es: '/es/privacidad/', en: '/en/privacy/' },
};
