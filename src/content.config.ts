import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Cada resumen vive en src/content/resumenes/es/ y src/content/resumenes/en/.
// Usa el MISMO nombre de archivo en las dos carpetas para que queden enlazados.
const resumenes = defineCollection({
  loader: glob({ pattern: '{es,en}/*.md', base: './src/content/resumenes' }),
  schema: z.object({
    numero: z.number().int().positive(),
    fecha: z.coerce.date(),
    titulo: z.string(),
    idea: z.string(),
    etiquetas: z.array(z.string()).default([]),
    borrador: z.boolean().default(false),
    doi: z.string().optional(), // DOI de este resumen (lo asigna Rogue Scholar)
    articulo: z.object({
      titulo: z.string(),
      autores: z.string(),
      revista: z.string(),
      anio: z.number().int(),
      doi: z.string().optional(),
      url: z.string().url().optional(),
      accesoAbierto: z.boolean().default(false),
    }),
  }),
});

export const collections = { resumenes };
