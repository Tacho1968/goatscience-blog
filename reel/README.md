# Vídeos semanales (Instagram y WeChat)

Plantillas para los vídeos verticales (1080×1920, 30 fps) de cada resumen:

- `make_reel.py`: reel en español para Instagram.
- `make_reel_zh.py`: vídeo en chino simplificado para WeChat Canales (视频号).

Cada semana se copian, se cambian los textos y tiempos de las escenas y se renderizan.

Requisitos (no se guardan en el repositorio):

- `ffmpeg`, Python con Pillow y `fonttools` + `brotli`.
- Fuentes: Bricolage Grotesque y Literata convertidas a TTF desde `node_modules/@fontsource-variable` (carpeta `fonts/`); Noto Sans/Serif CJK SC para el chino.
- Voz en off gratuita: `pip install piper-tts` y las voces de https://github.com/rhasspy/piper/releases/tag/v0.0.2
  (`voice-es-carlfm-x-low` y `voice-zh-cn-huayan-x-low`).

El vídeo sale sin música: se añade en la propia app para evitar problemas de derechos.
