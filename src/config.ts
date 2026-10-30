// Ajustes generales del blog. Cambia aquí los textos y la suscripción.

export const LANGS = ['es', 'en'] as const;
export type Lang = (typeof LANGS)[number];

export const SITE = {
  title: 'Goat Science',
  author: 'Anastasio Argüello',
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
