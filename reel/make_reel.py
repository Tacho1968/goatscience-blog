"""Reel vertical (1080x1920, 30 fps) para Goat Science nº 4.

Uso: python3 make_reel.py [frames]   -> con 'frames' solo dibuja fotogramas clave en PNG.
"""
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
GREEN = (30, 58, 43)
OCHRE = (217, 173, 74)
PAPER = (241, 243, 238)
INK = (23, 33, 28)
MUTED = (93, 102, 95)
ON_GREEN = (238, 241, 234)

HEAD = 'fonts/bricolage.ttf'
BODY = 'fonts/literata.ttf'
_cache = {}


def font(path, size, weight):
    key = (path, size, weight)
    if key not in _cache:
        f = ImageFont.truetype(path, size)
        f.set_variation_by_axes([weight])
        _cache[key] = f
    return _cache[key]


def ease(t):  # easeOutCubic
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def prog(t, start, dur):
    return ease((t - start) / dur)


def wrap(draw, text, f, maxw):
    lines = []
    for para in text.split('\n'):
        words, cur = para.split(' '), ''
        for w in words:
            test = (cur + ' ' + w).strip()
            if draw.textlength(test, font=f) <= maxw:
                cur = test
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def blend(c, bg, a):
    return tuple(int(bg[i] + (c[i] - bg[i]) * a) for i in range(3))


def text_block(draw, x, y, text, f, color, bg, a, maxw=W - 2 * 96, lh=1.18, rise=40):
    """Dibuja un bloque que aparece subiendo y fundiéndose. Devuelve la y final."""
    lines = wrap(draw, text, f, maxw)
    size = f.size
    oy = int((1 - a) * rise)
    col = blend(color, bg, a)
    for i, ln in enumerate(lines):
        draw.text((x, y + oy + i * size * lh), ln, font=f, fill=col)
    return y + len(lines) * size * lh


def label(draw, bg, fg, a=1.0):
    f = font(HEAD, 40, 700)
    draw.text((96, 250), 'Goat Science  nº 4', font=f, fill=blend(fg, bg, a))


# ---------- escenas ----------

def s1(t):  # 4.0 s : el número
    img = Image.new('RGB', (W, H), GREEN)
    d = ImageDraw.Draw(img)
    label(d, GREEN, OCHRE)
    n = int(round(7000 * prog(t, 0.2, 1.6) / 10) * 10)
    num = f'{n:,}'.replace(',', '.')
    fbig = font(HEAD, 300, 800)
    d.text((80, 620), num, font=fbig, fill=OCHRE)
    a = prog(t, 1.3, 0.6)
    text_block(d, 96, 960, 'años', font(HEAD, 120, 700), ON_GREEN, GREEN, a)
    a2 = prog(t, 2.0, 0.7)
    text_block(d, 96, 1180, 'tiene esta piel de cabra hallada en una cueva de Granada.',
               font(BODY, 58, 400), ON_GREEN, GREEN, a2, lh=1.35)
    return img


def s2(t):  # 4.5 s : el lugar
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    label(d, PAPER, GREEN)
    y = text_block(d, 96, 640, 'Cueva de los Murciélagos', font(HEAD, 104, 800), GREEN, PAPER, prog(t, 0.1, 0.6))
    y = text_block(d, 96, y + 10, 'Albuñol (Granada)', font(HEAD, 64, 500), MUTED, PAPER, prog(t, 0.5, 0.6))
    d.rectangle((96, y + 60, 96 + int(160 * prog(t, 0.9, 0.6)), y + 68), fill=OCHRE)
    text_block(d, 96, y + 130, 'Piel curtida y perforada a mano, del Neolítico antiguo. Seguramente parte de un ajuar funerario.',
               font(BODY, 56, 400), INK, PAPER, prog(t, 1.2, 0.7), lh=1.4)
    return img


def s3(t):  # 5.0 s : doméstica y europea
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    label(d, PAPER, GREEN)
    y = text_block(d, 96, 620, '¿Cabra doméstica o cabra montés?', font(HEAD, 96, 700), MUTED, PAPER, prog(t, 0.1, 0.6))
    y = text_block(d, 90, y + 110, 'Doméstica.', font(HEAD, 150, 800), GREEN, PAPER, prog(t, 2.9, 0.5))
    text_block(d, 96, y + 50, 'Y de origen europeo, según su ADN.', font(BODY, 62, 400), INK, PAPER, prog(t, 4.2, 0.6), lh=1.35)
    return img


def s4(t):  # 5.5 s : la Bermeya
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)
    label(d, PAPER, GREEN)
    y = text_block(d, 96, 560, 'Su pariente más cercana hoy:', font(HEAD, 72, 700), MUTED, PAPER, prog(t, 0.1, 0.6))
    y = text_block(d, 88, y + 60, 'Bermeya', font(HEAD, 190, 800), GREEN, PAPER, prog(t, 0.8, 0.7), rise=60, lh=1.05)
    y = text_block(d, 96, y + 20, 'raza autóctona de Asturias', font(HEAD, 64, 500), INK, PAPER, prog(t, 1.4, 0.6))
    d.rectangle((96, y + 60, 96 + int(160 * prog(t, 2.0, 0.5)), y + 68), fill=OCHRE)
    text_block(d, 96, y + 130, 'Las razas del sur y de las islas recibieron influencia africana más tarde.',
               font(BODY, 54, 400), INK, PAPER, prog(t, 2.3, 0.7), lh=1.4)
    return img


def s5(t):  # 4.5 s : llamada a la acción
    img = Image.new('RGB', (W, H), GREEN)
    d = ImageDraw.Draw(img)
    label(d, GREEN, OCHRE)
    text_block(d, 96, 600, 'Un artículo científico sobre cabras, cada semana, explicado en claro.',
               font(HEAD, 84, 700), ON_GREEN, GREEN, prog(t, 0.1, 0.6), lh=1.15)
    text_block(d, 96, 1120, 'Resumen completo en', font(BODY, 56, 400), ON_GREEN, GREEN, prog(t, 1.0, 0.6))
    text_block(d, 96, 1200, 'goatscience.ulpgc.es', font(HEAD, 80, 800), OCHRE, GREEN, prog(t, 1.4, 0.6))
    return img


SCENES = [('s1', s1, 4.0), ('s2', s2, 4.5), ('s3', s3, 5.6), ('s4', s4, 5.5), ('s5', s5, 4.5)]


def render_scene(name, fn, dur):
    tmp, out = f'{name}.tmp.mp4', f'{name}.mp4'
    n = int(round(dur * FPS))
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                          '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '18',
                          '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp],
                         stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(fn(i / FPS).tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, out)
    else:
        sys.exit(f'falló {name}')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'frames':
        for name, fn, dur in SCENES:
            fn(dur - 0.05).save(f'frame_{name}.png')
    else:
        for name, fn, dur in SCENES:
            render_scene(name, fn, dur)
        with open('list.txt', 'w') as fh:
            for name, _, _ in SCENES:
                fh.write(f"file '{name}.mp4'\n")
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', 'list.txt',
                        '-c', 'copy', 'goatscience-reel-n4.mp4'], check=True)
        print('ok')
