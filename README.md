# Viberuary

**A month of vibe coding. Real creativity. Artificial intelligence.**

**1–28 February 2027 · 28 days · 28 optional prompts · #viberuary**

Viberuary is a creative challenge to make something with AI every day of February 2027. Twenty-eight days to try ideas, learn something, and bring things into the world that didn't exist in January.

Make a website, an app, a game, a useful tool, or a strange little experiment. Whether you use AI coding tools every day or you're just getting started, you're welcome to join.

Visit [viberuary.pages.dev](https://viberuary.pages.dev) for the guidelines, daily prompts, and FAQs. The source lives at [OhLookCake/viberuary](https://github.com/OhLookCake/viberuary).

## How to take part

1. **Make something.** Use AI to help you code each day from February 1–28, 2027. Choose whichever tools, languages, and frameworks you like.
2. **Try a prompt, if you want.** There are 28 optional prompts, one for each day. Take them literally, interpret them loosely, or follow your own idea.
3. **Share what you make.** Post a link, screenshot, video, or story about the process wherever you already share things. Use **#viberuary** so others can find your work. A private demo to a friend counts too.
4. **Keep going at your own pace.** Aim for all 28 days, join once a week, or start late. Miss a day? Carry on.

You can start a new project each day, add a feature to something bigger, or remix an earlier experiment. Unfinished projects count. The point is to make progress and flex your creative muscles.

There are no formal submissions or prizes. Pick an idea and start making.

## Find your next idea

Browse the [daily prompts](https://viberuary.pages.dev/#prompts), use the site's “Choose one randomly for me” button, or download the [plain-text prompt list](prompts.txt).

Want the challenge on your wall? Grab the A4 poster with a [cream background](output/pdf/viberuary-a4-poster.pdf) or a [white background](output/pdf/viberuary-a4-poster-white-background.pdf).

## Local preview and posters

Run `uv run --no-project python -m http.server 8000 --bind 127.0.0.1` and open <http://127.0.0.1:8000/>.

Regenerate both A4 posters with `uv run scripts/build_posters.py` (uses macOS Arial and Georgia fonts). The script reads the 28 themes from `prompts.txt`; keep that list and the cards in `index.html` in sync.
