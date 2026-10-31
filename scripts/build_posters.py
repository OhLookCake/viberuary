# /// script
# requires-python = ">=3.10"
# dependencies = ["reportlab"]
# ///
"""Regenerate both A4 posters: uv run scripts/build_posters.py."""
from pathlib import Path
import re
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
for name, file in [('Arial', 'Arial.ttf'), ('Bold', 'Arial Bold.ttf'), ('Black', 'Arial Black.ttf'), ('Italic', 'Georgia Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
prompts = re.findall(r'^\d{2} (.+)$', (ROOT / 'prompts.txt').read_text(), re.M)
assert len(prompts) == 28
W, H = A4
INK, ACCENT, MUTED, LINE = map(HexColor, ['#252820', '#e9502e', '#66695e', '#c9c8bb'])
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)

def poster(white=False):
    path = OUT / ('viberuary-a4-poster-white-background.pdf' if white else 'viberuary-a4-poster.pdf')
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle('Viberuary - 28 days of making things - February 2027')
    c.setAuthor('Viberuary')
    paper = HexColor('#ffffff' if white else '#f3f0e6')
    c.setFillColor(paper); c.rect(0, 0, W, H, fill=1, stroke=0)
    def text(x, y, s, size=12, font='Arial', color=INK):
        c.setFillColor(color); c.setFont(font, size); c.drawString(x, H-y, s)
    def rule(y):
        c.setStrokeColor(LINE); c.setLineWidth(.7); c.line(38, H-y, W-38, H-y)
    c.saveState(); c.translate(39, H-51); c.rotate(5)
    c.setFillColor(ACCENT); c.rect(0,0,25,25,fill=1,stroke=0)
    c.setFillColor(paper); c.setFont('Bold',20); c.drawString(2,5,'V.'); c.restoreState()
    text(73,45,'viberuary',12,'Bold')
    text(368,44,'01-28 FEBRUARY 2027',8,'Courier',MUTED)
    rule(62)
    text(38,88,'*  A CREATIVE VIBE CODING CHALLENGE',8,'Courier',ACCENT)
    # Fit the longer name within the same headline area.
    title_size = min(96, 519 / pdfmetrics.stringWidth('Viberuary.', 'Black', 1))
    text(31,184,'Viberuary',title_size,'Black')
    dot_x = 31 + pdfmetrics.stringWidth('Viberuary','Black',title_size)
    text(dot_x,184,'.',title_size,'Black',ACCENT)
    for y, s in [(225,'A month of vibe-coding.'),(252,'Real creativity.'),(279,'Artificial intelligence.')]: text(38,y,s,21)
    text(38,306,'Make something new each day.',11,color=MUTED)
    text(38,323,'Follow a prompt. Or follow your own idea.',11,color=MUTED)
    c.saveState(); c.translate(395,H-204); c.rotate(-2)
    c.setFillColor(HexColor('#ffffff' if white else '#eae7dc')); c.setStrokeColor(MUTED)
    c.rect(0,-120,157,120,fill=1,stroke=1)
    c.setFillColor(MUTED); c.setFont('Courier',6.5); c.drawString(11,-16,'YOUR FEBRUARY,'); c.drawString(11,-27,'LOOSELY PLANNED')
    c.setFillColor(INK); c.setFont('Bold',61); c.drawString(9,-83,'28'); c.setFont('Italic',21); c.drawString(84,-83,'days')
    c.line(11,-94,145,-94); c.setFont('Courier',6); c.drawString(11,-109,'* Unfinished projects count'); c.restoreState()
    rule(345)
    for x, s in zip([38,166,319,441],['TRY AN IDEA.','LEARN SOMETHING.','SHARE IT.','DO IT AGAIN.']): text(x,364,'* '+s,7,'Courier',MUTED)
    rule(377)
    text(38,401,'28 STARTING POINTS. ZERO BINDING COMMITMENTS.',8,'Courier',MUTED)
    # February 2027 starts on Monday: four full rows of seven days.
    gx, gy, cw, ch = 38, 418, (W-76)/7, 67
    c.setStrokeColor(LINE); c.setLineWidth(.6)
    for i, prompt in enumerate(prompts):
        x, y = gx+(i%7)*cw, gy+(i//7)*ch
        c.rect(x,H-y-ch,cw,ch,fill=0,stroke=1)
        text(x+8,y+15,f'{i+1:02}',8,'Courier',ACCENT)
        text(x+cw-22,y+15,'FEB',5.5,'Courier',MUTED)
        text(x+8,y+43,prompt,10,'Bold')
    text(38,706,'One word for each day. Interpret very loosely.',7,'Courier',MUTED)
    text(38,741,"That idea isn't going to",23,'Bold')
    text(38,769,'build itself.',27,'Italic',ACCENT)
    rule(789)
    text(38,811,'viberuary.pages.dev',11,'Bold')
    text(438,811,'#viberuary',10,'Courier')
    c.linkURL('https://viberuary.pages.dev/',(38,H-817,175,H-798),relative=0)
    c.showPage(); c.save()
    print(path)

poster()
poster(white=True)
