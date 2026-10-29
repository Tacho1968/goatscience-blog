# Goat Science

Blog bilingüe (español e inglés) de resúmenes semanales de artículos científicos sobre cabras.
Web: https://goatscience.ulpgc.es

Está hecho con [Astro](https://astro.build) y genera una web estática: solo HTML, CSS y archivos
finales, sin base de datos ni nada que mantener en el servidor.

## Cómo publicar el resumen de la semana

1. Copia `PLANTILLA-es.md` en `src/content/resumenes/es/` y `PLANTILLA-en.md` en
   `src/content/resumenes/en/`.
2. Ponles **el mismo nombre** a los dos archivos, en minúsculas y con guiones, por ejemplo
   `calostro-cabras-majoreras.md`. Ese nombre será la dirección de la página y es lo que enlaza
   la versión en español con la inglesa.
3. Rellena la cabecera (número, fecha, título, idea clave, datos del artículo) y las cinco secciones.
4. Sube los dos archivos a la rama `main` de GitHub. En uno o dos minutos la web está actualizada.

Si quieres preparar un resumen sin publicarlo todavía, pon `borrador: true` en la cabecera.

Cuando publiques el primer resumen real, borra los dos archivos `ejemplo.md`.

### Campos de la cabecera

| Campo | Qué es |
| --- | --- |
| `numero` | Número de la entrega (1, 2, 3...) |
| `fecha` | Fecha de publicación, formato `AAAA-MM-DD` |
| `titulo` | Título del resumen, en lenguaje llano |
| `idea` | La idea clave en una o dos frases. Sale en la portada, en el RSS y en el correo |
| `etiquetas` | Temas, entre corchetes y comillas |
| `borrador` | `true` para ocultarlo, `false` para publicarlo |
| `articulo.titulo` | Título original del artículo |
| `articulo.autores` | Autores del artículo |
| `articulo.revista` | Revista |
| `articulo.anio` | Año |
| `articulo.doi` | DOI sin `https://doi.org/` (opcional) |
| `articulo.url` | Enlace si no hay DOI (opcional) |
| `articulo.accesoAbierto` | `true` si es de acceso abierto |

## Puesta en marcha (una sola vez)

### 1. GitHub

1. Crea un repositorio en tu cuenta (por ejemplo `Tacho1968/goatscience-blog`). Puede ser privado.
2. Sube el contenido de esta carpeta a la rama `main`.
3. Al subirlo, GitHub ejecuta automáticamente `.github/workflows/deploy.yml`: construye la web y
   crea una rama llamada `deploy` con la web ya lista. Puedes verlo en la pestaña **Actions**.

### 2. Plesk

1. En el dominio `goatscience.ulpgc.es`, entra en **Desplegar mediante Git**.
2. Elige repositorio remoto e introduce la dirección de tu repositorio de GitHub.
   Si es privado, Plesk te mostrará una clave SSH pública: añádela en GitHub en
   *Settings > Deploy keys* del repositorio (basta con permiso de lectura).
3. Rama: **`deploy`** (no `main`).
4. Ruta de despliegue: la carpeta pública del dominio, normalmente `httpdocs`.
5. Modo de despliegue: automático.

Para que Plesk descargue los cambios en cuanto GitHub termina, busca en la ficha del repositorio
en Plesk la URL de *webhook* y añádela en GitHub en *Settings > Webhooks*. Si no aparece o
prefieres no configurarlo, usa en Plesk el botón para extraer los cambios cada vez que publiques.

## Suscripción por correo

Una web estática no puede guardar correos por sí misma, así que la suscripción la gestiona un
servicio de boletines externo. Lo práctico es usar uno con **envío automático desde RSS**: cada vez
que publicas un resumen, el servicio lee el RSS del blog y manda el correo solo.

El blog ya publica un RSS por idioma:

- https://goatscience.ulpgc.es/es/rss.xml
- https://goatscience.ulpgc.es/en/rss.xml

Dos servicios con esa función son MailerLite y Buttondown (hay más). Compara precios y
condiciones en sus webs, que cambian.

Cuando tengas el servicio:

1. Crea una lista por idioma (o una sola con un campo de idioma).
2. Configura la campaña automática desde el RSS de cada idioma.
3. Copia la dirección `action` del formulario de alta que te da el servicio y el nombre de su campo
   de correo, y pégalos en `src/config.ts`, en `SUBSCRIBE`.
4. Hasta que `formAction` tenga valor, la web muestra que la suscripción llegará pronto y ofrece el RSS.

**Antes de activarla**, completa la política de privacidad (`src/pages/es/privacidad.astro` y
`src/pages/en/privacy.astro`) con el servicio de protección de datos de la ULPGC: vas a tratar
correos electrónicos de personas y el dominio es institucional.

## Trabajar en tu ordenador (opcional)

Necesitas Node.js 22 o superior.

```bash
npm install
npm run dev      # vista previa en http://localhost:4321 (muestra también los borradores)
npm run build    # genera la web final en dist/
```

## Dónde está cada cosa

- `src/content/resumenes/es/` y `src/content/resumenes/en/`: los resúmenes
- `src/config.ts`: nombre del blog, suscripción y direcciones de las páginas
- `src/i18n.ts`: todos los textos de la interfaz en los dos idiomas
- `src/styles/global.css`: colores y tipografía
- `src/pages/es/` y `src/pages/en/`: páginas fijas (acerca de, privacidad)

Las fuentes (Bricolage Grotesque y Literata, ambas con licencia libre SIL OFL) se sirven desde tu
propio dominio, sin llamadas a Google.
