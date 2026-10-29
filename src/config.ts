// Ajustes generales del blog. Cambia aquí los textos y la suscripción.

export const LANGS = ['es', 'en'] as const;
export type Lang = (typeof LANGS)[number];

export const SITE = {
  title: 'Goat Science',
  author: 'Anastasio Argüello',
};

// SUSCRIPCIÓN POR CORREO
// La web es estática: no guarda correos por sí misma. Los guarda un servicio
// externo de boletines. Cuando lo elijas, pega aquí la dirección (action) de su
// formulario de alta y el nombre del campo de correo que espera ese servicio.
// Puedes usar una lista por idioma o la misma para los dos.
// Mientras `formAction` esté vacío, el formulario indica que está pendiente.
export const SUBSCRIBE: Record<Lang, { formAction: string; emailField: string }> = {
  es: { formAction: '', emailField: 'email' },
  en: { formAction: '', emailField: 'email' },
};

// Direcciones de las páginas fijas en cada idioma.
export const ROUTES: Record<'archive' | 'about' | 'privacy', Record<Lang, string>> = {
  archive: { es: '/es/archivo/', en: '/en/archive/' },
  about: { es: '/es/acerca/', en: '/en/about/' },
  privacy: { es: '/es/privacidad/', en: '/en/privacy/' },
};
