"""Versión en chino simplificado del reel nº 4 (WeChat Channels)."""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont
import make_reel as m

NOTO = '/usr/share/fonts/opentype/noto/'
_c = {}


def zf(kind, size):
    path = {'black': 'NotoSansCJK-Black.ttc', 'bold': 'NotoSansCJK-Bold.ttc',
            'med': 'NotoSansCJK-Medium.ttc', 'serif': 'NotoSerifCJK-Medium.ttc'}[kind]
    k = (kind, size)
    if k not in _c:
        _c[k] = ImageFont.truetype(NOTO + path, size, index=2)  # índice 2 = SC
    return _c[k]


def wrap_cjk(draw, text, f, maxw):
    """Corta por caracteres, sin dejar puntuación al principio de línea."""
    lines, cur = [], ''
    for ch in text:
        if draw.textlength(cur + ch, font=f) <= maxw or ch in '，。？！：；、）':
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    lines.append(cur)
    return lines


def block(draw, x, y, text, f, color, bg, a, maxw=m.W - 2 * 96, lh=1.35, rise=40):
    lines = wrap_cjk(draw, text, f, maxw)
    oy = int((1 - a) * rise)
    col = m.blend(color, bg, a)
    for i, ln in enumerate(lines):
        draw.text((x, y + oy + i * f.size * lh), ln, font=f, fill=col)
    return y + len(lines) * f.size * lh


def label(d, bg, fg):
    d.text((96, 250), 'Goat Science  第 4 期', font=zf('bold', 40), fill=fg)


P, G, O, INK, MUTED, ON = m.PAPER, m.GREEN, m.OCHRE, m.INK, m.MUTED, m.ON_GREEN
pr = m.prog


def s1(t):
    img = Image.new('RGB', (m.W, m.H), G); d = ImageDraw.Draw(img); label(d, G, O)
    n = int(round(7000 * pr(t, 0.2, 1.6) / 10) * 10)
    d.text((80, 620), str(n), font=m.font(m.HEAD, 300, 800), fill=O)
    block(d, 96, 930, '年', zf('black', 120), ON, G, pr(t, 1.3, 0.6))
    block(d, 96, 1200, '这块山羊皮革，出土于西班牙格拉纳达的一处洞穴。', zf('serif', 58), ON, G, pr(t, 2.0, 0.7), lh=1.5)
    return img


def s2(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, P, G)
    y = block(d, 96, 640, '蝙蝠洞', zf('black', 120), G, P, pr(t, 0.1, 0.6), lh=1.2)
    y = block(d, 96, y + 10, 'Cueva de los Murciélagos', m.font(m.HEAD, 60, 700), MUTED, P, pr(t, 0.4, 0.6))
    y = block(d, 96, y, '西班牙 阿尔武尼奥尔（格拉纳达）', zf('med', 52), MUTED, P, pr(t, 0.6, 0.6))
    d.rectangle((96, y + 50, 96 + int(160 * pr(t, 0.9, 0.6)), y + 58), fill=O)
    block(d, 96, y + 110, '经过鞣制，边缘有人工穿孔，属于新石器时代早期，很可能是随葬品。',
          zf('serif', 56), INK, P, pr(t, 1.2, 0.7), lh=1.55)
    return img


def s3(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, P, G)
    y = block(d, 96, 620, '家养山羊，还是野山羊？', zf('bold', 88), MUTED, P, pr(t, 0.1, 0.6), lh=1.3)
    y = block(d, 96, y + 100, '家养山羊。', zf('black', 150), G, P, pr(t, 2.6, 0.5), lh=1.2)
    block(d, 96, y + 40, 'DNA 显示，它源自欧洲。', zf('serif', 62), INK, P, pr(t, 4.3, 0.6), lh=1.5)
    return img


def s4(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, P, G)
    y = block(d, 96, 560, '与它亲缘最近的现代品种：', zf('bold', 72), MUTED, P, pr(t, 0.1, 0.6))
    y = m.text_block(d, 88, y + 60, 'Bermeya', m.font(m.HEAD, 190, 800), G, P, pr(t, 0.8, 0.7), rise=60, lh=1.05)
    y = block(d, 96, y + 20, '贝尔梅亚山羊，西班牙阿斯图里亚斯地方品种', zf('med', 56), INK, P, pr(t, 1.4, 0.6))
    d.rectangle((96, y + 50, 96 + int(160 * pr(t, 2.0, 0.5)), y + 58), fill=O)
    block(d, 96, y + 110, '西班牙南部和海岛的山羊品种，后来才受到非洲血统的影响。',
          zf('serif', 54), INK, P, pr(t, 2.3, 0.7), lh=1.55)
    return img


def s5(t):
    img = Image.new('RGB', (m.W, m.H), G); d = ImageDraw.Draw(img); label(d, G, O)
    block(d, 96, 600, '每周一篇山羊科研论文，通俗解读。', zf('black', 80), ON, G, pr(t, 0.1, 0.6), lh=1.3)
    block(d, 96, 1060, '完整解读（英文）：', zf('serif', 56), ON, G, pr(t, 1.0, 0.6))
    m.text_block(d, 96, 1160, 'goatscience.ulpgc.es', m.font(m.HEAD, 80, 800), O, G, pr(t, 1.4, 0.6))
    return img


SCENES = [('z1', s1, 4.0), ('z2', s2, 4.5), ('z3', s3, 6.0), ('z4', s4, 5.5), ('z5', s5, 4.5)]

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'frames':
        for name, fn, dur in SCENES:
            fn(dur - 0.05).save(f'frame_{name}.png')
    else:
        for name, fn, dur in SCENES:
            m.render_scene(name, fn, dur)
        with open('list_zh.txt', 'w') as fh:
            for name, _, _ in SCENES:
                fh.write(f"file '{name}.mp4'\n")
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', 'list_zh.txt',
                        '-c', 'copy', 'goatscience-reel-n4-zh.mp4'], check=True)
        print('ok')
