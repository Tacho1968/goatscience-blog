"""English version of reel No. 4 (Instagram)."""
import subprocess, sys
from PIL import Image, ImageDraw
import make_reel as m

P, G, O, INK, MUTED, ON = m.PAPER, m.GREEN, m.OCHRE, m.INK, m.MUTED, m.ON_GREEN
pr, tb, F, H, B = m.prog, m.text_block, m.font, m.HEAD, m.BODY


def label(d, fg):
    d.text((96, 250), 'Goat Science  No. 4', font=F(H, 40, 700), fill=fg)


def s1(t):
    img = Image.new('RGB', (m.W, m.H), G); d = ImageDraw.Draw(img); label(d, O)
    n = int(round(7000 * pr(t, 0.2, 1.6) / 10) * 10)
    d.text((80, 620), f'{n:,}', font=F(H, 300, 800), fill=O)
    tb(d, 96, 960, 'years old', F(H, 120, 700), ON, G, pr(t, 1.1, 0.6))
    tb(d, 96, 1180, 'This goatskin was found in a cave in Granada, southern Spain.',
       F(B, 58, 400), ON, G, pr(t, 1.8, 0.7), lh=1.35)
    return img


def s2(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, G)
    y = tb(d, 96, 640, 'Cueva de los Murciélagos', F(H, 104, 800), G, P, pr(t, 0.1, 0.6))
    y = tb(d, 96, y + 10, 'The Cave of the Bats, Albuñol (Spain)', F(H, 58, 500), MUTED, P, pr(t, 0.5, 0.6))
    d.rectangle((96, y + 60, 96 + int(160 * pr(t, 0.9, 0.6)), y + 68), fill=O)
    tb(d, 96, y + 130, 'A tanned hide with hand-made holes, from the Early Neolithic. Probably part of a burial.',
       F(B, 56, 400), INK, P, pr(t, 1.2, 0.7), lh=1.4)
    return img


def s3(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, G)
    y = tb(d, 96, 620, 'Domestic goat or wild ibex?', F(H, 96, 700), MUTED, P, pr(t, 0.1, 0.6))
    y = tb(d, 90, y + 110, 'Domestic.', F(H, 160, 800), G, P, pr(t, 3.7, 0.5))
    tb(d, 96, y + 50, 'And of European origin, according to its DNA.', F(B, 62, 400), INK, P, pr(t, 5.1, 0.6), lh=1.35)
    return img


def s4(t):
    img = Image.new('RGB', (m.W, m.H), P); d = ImageDraw.Draw(img); label(d, G)
    y = tb(d, 96, 560, 'Its closest living relative:', F(H, 72, 700), MUTED, P, pr(t, 0.1, 0.6))
    y = tb(d, 88, y + 60, 'Bermeya', F(H, 190, 800), G, P, pr(t, 1.4, 0.7), rise=60, lh=1.05)
    y = tb(d, 96, y + 20, 'a local breed from Asturias, northern Spain', F(H, 58, 500), INK, P, pr(t, 2.2, 0.6))
    d.rectangle((96, y + 60, 96 + int(160 * pr(t, 2.8, 0.5)), y + 68), fill=O)
    tb(d, 96, y + 130, 'African ancestry reached the breeds of southern Spain and the islands later.',
       F(B, 54, 400), INK, P, pr(t, 3.1, 0.7), lh=1.4)
    return img


def s5(t):
    img = Image.new('RGB', (m.W, m.H), G); d = ImageDraw.Draw(img); label(d, O)
    tb(d, 96, 600, 'One goat science paper a week, explained clearly.', F(H, 84, 700), ON, G, pr(t, 0.1, 0.6), lh=1.15)
    tb(d, 96, 1120, 'Full summary at', F(B, 56, 400), ON, G, pr(t, 1.0, 0.6))
    tb(d, 96, 1200, 'goatscience.ulpgc.es', F(H, 80, 800), O, G, pr(t, 1.4, 0.6))
    return img


SCENES = [('e1', s1, 3.8), ('e2', s2, 4.3), ('e3', s3, 7.2), ('e4', s4, 5.6), ('e5', s5, 4.2)]

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'frames':
        for name, fn, dur in SCENES:
            fn(dur - 0.05).save(f'frame_{name}.png')
    else:
        for name, fn, dur in SCENES:
            m.render_scene(name, fn, dur)
        with open('list_en.txt', 'w') as fh:
            for name, _, _ in SCENES:
                fh.write(f"file '{name}.mp4'\n")
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', 'list_en.txt',
                        '-c', 'copy', 'goatscience-reel-n4-en.mp4'], check=True)
        print('ok')
