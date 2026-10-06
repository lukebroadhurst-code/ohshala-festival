#!/usr/bin/env python3
"""Generates the sub-pages and keeps nav/footer identical across the site.
Run:  python3 build.py   (index.html is hand-authored; only its nav/footer are refreshed)
Output is plain static HTML. No build step is needed to *serve* the site.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
CDN = 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/'

def img(path, w=1500):
    return f'{CDN}{path}?format={w}w'

# ---- brand assets (hot-linked from the current site; save locally before launch) ----
LOGO = img('8ddbb9a4-abd6-44d9-be26-56d0668473a6/Untitled+design.png', 2500)

P = {
    'yoga':     '45d5bbdd-bc6c-4c8b-8fc5-5c20a2684203/Oh+Shala+Festival-172.jpg',
    'bell':     'f2cd9c4d-43a1-4227-9acb-5aa18354f577/Oh+Shala+Festival-89.jpg',
    'market':   '0fa587c2-a53c-4c97-8df1-7f6e25580998/Oh+Shala+Festival-184.jpg',
    'food':     'd124d439-8d36-404d-912e-55c81bec9d6e/Oh+Shala+Festival-369.jpg',
    'stretch':  'be30a4bb-caa9-4460-8450-868abaabab4e/Oh+Shala+Festival-362.jpg',
    'craft':    '6356cd82-fae0-41bd-bb6e-2b6c3af04a2d/Oh+Shala+Festival-232.jpg',
    'circle':   'b245a310-5546-4ab8-9150-2fd1ee958c6d/Oh+Shala+Festival-153.jpg',
    'sign':     'b75bb614-dba8-41e0-a897-baad587699f5/Oh+Shala+Festival-377.jpg',
    'move':     'd3d6b355-e9d3-4746-9723-5ddf8762d491/EC_Oshala24_4238.jpg',
    'explore':  'd21446d1-853a-4b97-a0b0-4841afa9b6ad/EC_Oshala24_4395.jpg',
    'listen':   '111fd282-fece-4027-9a52-1b7f96aff927/EC_Oshala24_5381.jpg',
    'tipi':     '09b43347-a860-4c6e-9571-46ac5133df69/EC_Oshala24_4396.jpg',
    'wood':     '8d8e03d7-dfd3-4780-b507-61f0af25f302/EC_Oshala24_4299.jpg',
    'family':   '0b75f55b-25d9-4cf1-ab77-fabf9ddbcd4c/EC_Oshala24_4120.jpg',
    'talk':     '7c3e77f2-68d6-4c45-b41e-5832cf6213da/EC_Oshala24_3457.jpg',
    'meadow':   'a86ef75b-eea2-4fbf-b7f1-9b72c8649343/EC_Oshala24_5326.jpg',
    'joy':      '9121cb11-c5dd-4a9c-a1bc-7812ea471d6b/EC_Oshala24_5743.jpg',
    'music':    '6d4582ed-9423-49ef-b465-0a27feba8632/EC_Oshala24_4075.jpg',
    'circus':   '764842e3-514e-4e44-8fb4-fdff9f4be217/Oh+Shala+Festival-98.jpg',
    'fri':      'd372a0d9-6edb-4c01-9a1d-5c81620f25e5/FRIDAY+WEBSITE.png',
    'sat':      '4ce36b51-2153-464e-920a-279f2eb498f7/SATURDAY+WEBSITE.png',
    'sun':      'c580165f-b096-4cdc-8eb4-3331bfc7ed19/SUNDAY+WEBSITE.png',
}
def I(k, w=1500):
    return img(P[k], w)

OLD = 'https://www.ohshalafestival.com'
TICKETS_URL = OLD + '/tickets'   # hosts the Ticket Tailor embed today

# ---------------------------------------------------------------- shared chrome
def logo(cls=''):
    return (f'<span class="logo {cls}"><img src="{LOGO}" alt="Oh Shala Bhakti Festival" '
            f'width="400" height="400"></span>')

def nav(active=''):
    items = [('story.html', 'Our story'), ('programme.html', 'Programme'), ('tickets.html', 'Tickets'),
             ('gatherings.html', 'Gatherings'), ('team.html', 'The team'), ('faqs.html', 'FAQs')]
    cur = ' aria-current="page"'
    links = ''.join(
        '<a href="%s"%s>%s</a>' % (h, cur if h == active else '', t) for h, t in items)
    return f'''<header class="nav" id="nav">
  <a class="brand" href="index.html" aria-label="Oh Shala Festival, home">{logo()}</a>
  <nav class="links" id="links" aria-label="Main">
    {links}
    <a class="cta" href="tickets.html">Golden Tickets</a>
  </nav>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="links"><i></i><i></i></button>
</header>'''

FOOTER = f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a href="index.html" aria-label="Oh Shala Festival, home">{logo('logo-lg')}</a>
      <p>Embracing community · Supporting local · Celebrating wellness &amp; nature.</p>
      <p class="when">9 – 11 July 2027<br>Penn House Estate, Buckinghamshire</p>
    </div>
    <nav aria-label="Festival">
      <h4>Festival</h4>
      <a href="story.html">Our story</a>
      <a href="programme.html">Programme</a>
      <a href="tickets.html">Tickets</a>
      <a href="family.html">Family</a>
      <a href="food.html">Food, stalls &amp; treatments</a>
    </nav>
    <nav aria-label="More">
      <h4>More</h4>
      <a href="gatherings.html">Upcoming gatherings</a>
      <a href="team.html">The team</a>
      <a href="faqs.html">FAQs</a>
      <a href="contact.html">Contact</a>
      <a href="terms.html">Terms &amp; conditions</a>
    </nav>
    <div class="social">
      <h4>Say hello</h4>
      <a href="https://instagram.com/ohshalafest" rel="noopener">Instagram</a>
      <a href="https://facebook.com/ohshalafest" rel="noopener">Facebook</a>
      <a href="mailto:hello@ohshalafestival.com">hello@ohshalafestival.com</a>
    </div>
  </div>
  <p class="copy">© 2027 Oh Shala Festival</p>
</footer>'''

BAR = ('<div class="bar" role="note"><a href="tickets.html"><span class="dot"></span> '
       'Limited Golden Tickets for 2027 are live <span aria-hidden="true">→</span></a></div>')

KIT = '''<!-- FONTS: the old site uses Adobe Fonts "orpheus-pro" + "adobe-garamond-pro". Once an Adobe Fonts web project exists for the new domain,
     uncomment and paste its kit URL here; styles.css already asks for those families first (EB Garamond / Cormorant are close stand-ins).
<link rel="stylesheet" href="https://use.typekit.net/YOURKIT.css"> -->
'''

def head(title, desc, og=None):
    og = og or I('yoga')
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#2a0f27">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<link rel="icon" href="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..700;1,400..700&family=Cormorant:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
{KIT}<link rel="stylesheet" href="styles.css?v=11">
<script>document.documentElement.classList.add('js')</script>
</head>'''

def phero(eyebrow, h1, lede, extra=''):
    return f'''<section class="phero">
  <div class="sky" aria-hidden="true"><div class="sun"></div><svg class="mandala halo" viewBox="-50 -50 100 100"></svg></div>
  <div class="wrap">
    <p class="eyebrow reveal">{eyebrow}</p>
    <h1 class="reveal" style="--d:.08s">{h1}</h1>
    <p class="lede reveal" style="--d:.16s">{lede}</p>
    {extra}
  </div>
</section>'''

JOIN = '''<section class="join" id="join">
  <div class="wrap">
    <svg class="mandala join-mandala spin" viewBox="-50 -50 100 100" aria-hidden="true"></svg>
    <h2 class="sec-title">Join our growing <em>community</em></h2>
    <p class="lede">Line-up news, ticket releases and the occasional kirtan. Nothing else.</p>
    <form class="signup" id="signup" novalidate>
      <label class="sr" for="email">Email address</label>
      <input id="email" type="email" placeholder="you@email.com" autocomplete="email" required>
      <button class="btn btn-gold" type="submit">Sign me up</button>
      <p class="msg" id="msg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>'''

def page(fname, title, desc, body, active='', join=True, og=None):
    html = (head(title, desc, og) + '\n<body>\n<a class="skip" href="#main">Skip to content</a>\n'
            '<div class="grain" aria-hidden="true"></div>\n' + BAR + '\n' + nav(active) +
            '\n<main id="main">\n' + body + ('\n' + JOIN if join else '') +
            '\n</main>\n' + FOOTER + '\n<script src="main.js?v=9"></script>\n</body>\n</html>\n')
    key = PHERO_BG.get(fname)
    if key:
        html = re.sub(r'(<section class="phero[^"]*">)',
                      lambda m: m.group(1) + '\n  <div class="phero-bg" aria-hidden="true"><img src="%s" alt=""></div>' % I(key, 2000),
                      html, count=1)
    (ROOT / fname).write_text(html)
    print('wrote', fname)


PHERO_BG = {'story.html': 'circle', 'programme.html': 'move', 'tickets.html': 'stretch', 'gatherings.html': 'listen',
            'team.html': 'joy', 'family.html': 'circus', 'food.html': 'food', 'faqs.html': 'talk',
            'contact.html': 'sign', '404.html': 'wood'}

def pb(key, quote, alt='', short=False):
    return f'''<section class="pb{' pb-short' if short else ''}">
  <div class="pb-img"><img src="{I(key, 2000)}" alt="{alt}" loading="lazy"></div>
  <div class="pb-veil"></div>
  <div class="wrap"><p class="pb-quote reveal">{quote}</p></div>
</section>'''

def cta_band(h, p, label, href, ext=False):
    rel = ' rel="noopener"' if ext else ''
    return f'''<section class="band">
  <div class="wrap band-in">
    <h2 class="sec-title reveal">{h}</h2>
    <div class="reveal"><p class="lede">{p}</p><a class="btn btn-plum" href="{href}"{rel}>{label}</a></div>
  </div>
</section>'''

# ---------------------------------------------------------------- STORY
def story():
    body = phero('Our story', 'A gathering,<br><em>not a festival.</em>',
                 'How a group of people who wanted more community around Marlow ended up building a wellbeing festival in the Buckinghamshire woods.')
    body += f'''
<section class="sec plum">
  <div class="wrap story-grid">
    <figure class="story-photo reveal">
      <img src="{I('joy')}" alt="Two festival-goers laughing together" loading="lazy">
      <svg class="mandala spin" viewBox="-50 -50 100 100" aria-hidden="true"></svg>
    </figure>
    <div class="story-copy">
      <p class="eyebrow reveal">2019</p>
      <h2 class="sec-title reveal">We had a vision: the first wellbeing festival in <em>Buckinghamshire.</em></h2>
      <div class="prose reveal">
        <p>Oh Shala came together through a group of people who wanted to bring more of a sense of community to the Marlow area. We realised quickly that the surrounding areas of Buckinghamshire and Berkshire had hidden treasures of wellbeing that we wanted to share far and wide.</p>
        <p>We would consider the festival more of a &lsquo;gathering&rsquo;, keeping it grassroots, local and about connection.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec cream">
  <div class="wrap">
    <h2 class="sec-title reveal">What we hold <em>dear</em></h2>
    <ul class="values">
      <li class="reveal"><b>Safe &amp; non-judgmental</b><span>A new way to look at wellbeing, in a space that lets you express however you need to.</span></li>
      <li class="reveal" style="--d:.07s"><b>Family-oriented</b><span>Little ones are part of the gathering, not an afterthought. Under-fives to grandparents.</span></li>
      <li class="reveal" style="--d:.14s"><b>Sober &amp; vegan</b><span>No alcohol, no drugs, and every plate plant-based, so the whole field can relax into it.</span></li>
      <li class="reveal" style="--d:.21s"><b>Grassroots &amp; local</b><span>Local facilitators, local businesses and local land. Our wellbeing treasures are close to home.</span></li>
    </ul>
  </div>
</section>

{pb("meadow", "Grassroots.<br><em>Local.</em> Connected.")}

<section class="sec night">
  <div class="wrap two">
    <div>
      <p class="eyebrow reveal">Giving back</p>
      <h2 class="sec-title reveal">Every year, we back <em>local charities.</em></h2>
      <p class="lede reveal">We highlight the work of organisations doing good close to home and further afield.</p>
    </div>
    <ul class="charities">
      <li class="reveal"><b>Marlow Refugee Action</b></li>
      <li class="reveal" style="--d:.06s"><b>One Can Trust</b><span>Buckinghamshire&rsquo;s food bank</span></li>
      <li class="reveal" style="--d:.12s"><b>War Child UK</b></li>
      <li class="reveal" style="--d:.18s"><b>Dash Charity</b></li>
    </ul>
  </div>
</section>

<section class="sec blush letter">
  <div class="wrap narrow">
    <p class="eyebrow reveal">A note from Emily</p>
    <blockquote class="reveal">
      <p>The weekend takes a team of incredible people: volunteers, facilitators, local businesses and the land we are lucky to have our festival on, Penn House Estate.</p>
      <p>We welcome you all with open arms to embrace community and celebrate nature.</p>
      <footer>Emily x <span>Founder &amp; Director</span></footer>
    </blockquote>
  </div>
</section>
''' + cta_band('Come and be part of it.', 'Three days, 6 tents and a field full of kindred spirits.', 'See the tickets →', 'tickets.html')
    page('story.html', 'Our story · Oh Shala Festival',
         'In 2019 we had a vision: the first wellbeing festival in Buckinghamshire. A grassroots gathering about community, nature and connection.',
         body, 'story.html', og=I('joy'))

# ---------------------------------------------------------------- PROGRAMME
AREAS = [
    ('move', 'Move tent', 'Move', 'Get in your body.',
     'Yoga, Qi Gong, Tai Chi, capoeira, handstands and dance. Roll out your mat and move, however moves you.',
     ['Yoga', 'Qi Gong', 'Tai Chi', 'Capoeira', 'Handstands', 'Dance']),
    ('explore', 'Explore tent', 'Explore', 'Follow your curiosity.',
     'Wellbeing talks, meditation and crafts. A tent for learning something new about yourself and your community.',
     ['Wellbeing talks', 'Meditation', 'Crafts']),
    ('listen', 'Listen tent', 'Listen', 'Let the sound carry you.',
     'Kirtan, chanting, African drumming and live artists. Call-and-response singing that needs no experience, only a voice.',
     ['Kirtan', 'Chanting', 'African drumming', 'Live artists']),
    ('heal', 'Heal tent', 'Heal', 'Rest, restore, receive.',
     'Crystal healing, feminine health and sacred ceremony, held gently by local holistic practitioners.',
     ['Crystal healing', 'Feminine health', 'Sacred ceremony']),
    ('woodland', 'Woodland &amp; sauna', 'Woodland', 'Slip into the trees.',
     'A quiet corner of woodland, plus sauna, for when the field gets lively and you need to be among the trees.',
     ['Woodland', 'Sauna']),
    ('family', 'Family area', 'Family', 'Play together.',
     'Children&rsquo;s yoga, circus, crafts and plenty of space to run. See the full family page for the details.',
     ["Children's yoga", 'Circus', 'Crafts']),
    ('think-gita', 'Think Gita', 'Think Gita', 'Conversation &amp; philosophy.',
     'A space to sit with big questions and the wisdom of the bhakti tradition.',
     ['Philosophy', 'Bhakti']),
    ('temple', 'Temple of the Feminine Flame', 'Temple', 'Sacred feminine.',
     'Feminine health and sacred ceremony, in a space held for women&rsquo;s wellbeing.',
     ['Ceremony', "Women's healing"]),
    ('wiseheart', 'Wiseheart Project', 'Wiseheart', 'More to be announced.',
     'The Wiseheart Project joins the programme this year. Details are on their way.',
     []),
    ('live-music', 'Live music', 'Music', 'Evenings under the trees.',
     'Live artists and music through the weekend, from kirtan circles to evening sets.',
     ['Live artists', 'Kirtan', 'Drumming']),
]
AREA_IMG = {'move': 'move', 'explore': 'explore', 'listen': 'listen', 'heal': 'tipi', 'woodland': 'wood',
            'family': 'family', 'think-gita': 'talk', 'temple': 'bell', 'wiseheart': 'meadow', 'live-music': 'music'}

def programme():
    areas = ''
    for i, (slug, name, short, tag, desc, chips) in enumerate(AREAS, 1):
        chip_html = ''.join(f'<li>{c}</li>' for c in chips)
        extra = ' <a class="more" href="family.html">The family page →</a>' if slug == 'family' else ''
        areas += f'''
    <article class="area reveal" id="{slug}">
      <div class="area-img"><img src="{I(AREA_IMG[slug], 1000)}" alt="{name} at a previous Oh Shala" loading="lazy"></div>
      <div class="area-copy">
        <span class="n">{i:02d}</span>
        <h3>{name}</h3>
        <p class="tagline">{tag}</p>
        <p>{desc}{extra}</p>
        {f'<ul class="chips dark">{chip_html}</ul>' if chips else ''}
      </div>
    </article>'''
    sched = ''
    for key, day, pdf, desc_pdf in [
        ('fri', 'Friday', 'FRIDAY-FINAL-FOR-PRINT.pdf', 'FRI-DESCRIP-FINAL.pdf'),
        ('sat', 'Saturday', 'SATURDAY-FINAL-FOR-PRINT.pdf', 'SATURDAY-DESCRIPTIONS.pdf'),
        ('sun', 'Sunday', 'SUNDAY-FINAL-PRINT.pdf', 'SUNDAY-DESCRIPTIONS-dd9f.pdf')]:
        sched += f'''
      <article class="sched reveal">
        <a class="sched-img" href="{OLD}/s/{pdf}" target="_blank" rel="noopener"><img src="{I(key, 750)}" alt="{day} schedule, 2026" loading="lazy"></a>
        <h3>{day}</h3>
        <a class="btn btn-ghost-dark" href="{OLD}/s/{pdf}" target="_blank" rel="noopener">Schedule (PDF) ↓</a>
        <a class="tlink" href="{OLD}/s/{desc_pdf}" target="_blank" rel="noopener">Workshop descriptions (PDF) ↓</a>
      </article>'''
    body = phero('Programme', 'Six tents.<br><em>Three days.</em>',
                 'Over 40 workshops and over 50 practitioners, all included in your ticket. Here&rsquo;s the lay of the land.')
    body += f'''
<section class="sec night soon">
  <div class="wrap two">
    <div>
      <p class="eyebrow reveal">2027 line-up</p>
      <h2 class="sec-title reveal">Announced <em>soon.</em></h2>
    </div>
    <div class="reveal">
      <p class="lede">We&rsquo;re putting the final touches to the 2027 programme. Join the mailing list to be first to know, or tell us what you&rsquo;d love to offer.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="#join">Get line-up news</a>
        <a class="btn btn-ghost" href="contact.html#facilitators">Apply to facilitate</a>
      </div>
      <p class="small">Schedule timings and practices may change, as they do at festivals.</p>
    </div>
  </div>
</section>

<section class="sec plum">
  <div class="wrap">
    <p class="eyebrow">Around the field</p>
    <h2 class="sec-title">Ten places to <em>wander.</em></h2>
    <div class="areas">{areas}
    </div>
  </div>
</section>

<section class="sec cream" id="schedule">
  <div class="wrap">
    <p class="eyebrow">See what a day looks like</p>
    <h2 class="sec-title">The 2026 <em>schedule</em></h2>
    <p class="lede">Last year&rsquo;s programme, for a taste of how the weekend flows. The 2027 schedule will follow.</p>
    <div class="scheds">{sched}
    </div>
  </div>
</section>
''' + cta_band('Everything here is in your ticket.', 'Every scheduled workshop, plus camping on site.', 'Get your Golden Ticket →', 'tickets.html')
    page('programme.html', 'Programme · Oh Shala Festival',
         'Six tents, over 40 workshops and 50 practitioners: yoga, kirtan, Qi Gong, circus, crystal healing, live music and more. 9–11 July 2027.',
         body, 'programme.html', og=I('move'))

# ---------------------------------------------------------------- TICKETS
def tickets():
    body = phero('Tickets', 'One ticket.<br><em>The whole weekend.</em>',
                 'Your Golden Ticket covers every scheduled workshop and camping on site, from Friday to Sunday.')
    body += f'''
<section class="sec night">
  <div class="wrap tix-grid">
    <div>
      <h2 class="sec-title reveal" style="font-size:clamp(34px,4.6vw,64px)">What&rsquo;s <em>in</em>, what&rsquo;s <em>extra</em></h2>
      <ul class="tick-list reveal">
        <li class="yes">All scheduled workshops &amp; classes</li>
        <li class="yes">Camping on site, free</li>
        <li class="yes">Free parking (please car-share)</li>
        <li class="yes">Showers, toilets and free water taps</li>
        <li class="no">Food from our vegan vendors</li>
        <li class="no">Treatments</li>
        <li class="no">Glamping &amp; vehicle camping</li>
      </ul>
      <p class="small reveal">Food and treatments are paid for directly with vendors and practitioners on site.</p>
    </div>
    <div class="ticket reveal" aria-label="Golden Ticket">
      <div class="ticket-main">
        <svg class="mandala t-mandala" viewBox="-50 -50 100 100" aria-hidden="true"></svg>
        <span class="t-label">Admit one</span>
        <h3>Golden<br><em>Ticket</em></h3>
        <p>9 – 11 July 2027<br>Penn House Estate</p>
        <a class="btn btn-plum" href="{TICKETS_URL}">Book on Ticket Tailor →</a>
      </div>
      <div class="ticket-stub" aria-hidden="true"><span>Oh Shala · 2027 · Oh Shala · 2027 · Oh Shala</span></div>
    </div>
  </div>
</section>

{pb("circle", "Come as<br><em>you are.</em>", short=True)}

<section class="sec cream">
  <div class="wrap">
    <h2 class="sec-title reveal">Good to <em>know</em></h2>
    <div class="cards">
      <article class="card reveal"><h3>Instalments</h3><p>Instalment payment plans are available. Email <a href="mailto:hello@ohshalafestival.com">hello@ohshalafestival.com</a> and we&rsquo;ll set one up.</p></article>
      <article class="card reveal" style="--d:.06s"><h3>Carer tickets</h3><p>Complimentary carer tickets are available for people with disabilities or medical conditions. Get in touch to arrange one.</p></article>
      <article class="card reveal" style="--d:.12s"><h3>Children</h3><p>Children go free, with limited availability, and need adult supervision at all times. See the <a href="family.html">family page</a>.</p></article>
      <article class="card reveal" style="--d:.18s"><h3>Transfers &amp; refunds</h3><p>Tickets are non-refundable, but you can transfer yours to someone else by contacting us with their details. See our <a href="terms.html">terms</a>.</p></article>
      <article class="card reveal" style="--d:.24s"><h3>Wristbands</h3><p>Your wristband lets you leave and re-enter the site throughout the weekend. Keep it on.</p></article>
      <article class="card reveal" style="--d:.3s"><h3>Glamping &amp; treatments</h3><p>Glamping and treatments are booked separately. Find the links on our <a href="{TICKETS_URL}">ticket booking page</a>.</p></article>
    </div>
  </div>
</section>
''' + cta_band('Ready to join us?', 'Limited Golden Tickets for 2027 are live.', 'Book your ticket →', TICKETS_URL, True)
    page('tickets.html', 'Tickets · Oh Shala Festival',
         'Golden Tickets for Oh Shala Festival, 9–11 July 2027. Includes all scheduled workshops and camping. Instalment plans available.',
         body, 'tickets.html', join=False, og=I('stretch'))

# ---------------------------------------------------------------- GATHERINGS
def gatherings():
    body = phero('Upcoming gatherings', 'Between festivals,<br><em>we gather.</em>',
                 'Kirtan evenings, ceremonies and retreats through the year, held in and around Marlow and beyond.')
    body += f'''
<section class="sec night">
  <div class="wrap">
    <p class="eyebrow">Coming up</p>
    <h2 class="sec-title">Next on the <em>calendar</em></h2>
    <div class="events">
      <article class="event reveal">
        <div class="date"><b>17</b><span>Oct 2026</span><i>Saturday</i></div>
        <div class="info">
          <h3>An Evening of Kirtan: Navaratri Special</h3>
          <p>18:00 – 20:00 · PILA Yoga, Marlow</p>
        </div>
        <a class="btn btn-gold" href="https://bookwhen.com/openshala" target="_blank" rel="noopener">Book on Bookwhen ↗</a>
      </article>
      <article class="event reveal" style="--d:.08s">
        <div class="date"><b>14</b><span>Nov 2026</span><i>Saturday</i></div>
        <div class="info">
          <h3>Oh Shala Post Party</h3>
          <p>16:00 – 20:30 · Lopemede Farm</p>
        </div>
        <a class="btn btn-gold" href="https://bookwhen.com/openshala" target="_blank" rel="noopener">Book on Bookwhen ↗</a>
      </article>
    </div>
  </div>
</section>

{pb("music", "Voices rising,<br><em>together.</em>")}

<section class="sec blush">
  <div class="wrap two">
    <div>
      <p class="eyebrow reveal">Regular rhythm</p>
      <h2 class="sec-title reveal">An evening of <em>kirtan</em></h2>
      <p class="lede reveal">Our kirtan evenings are call-and-response chanting practice, born and raised in India&rsquo;s bhakti traditions. No experience needed. Just come and sing.</p>
    </div>
    <ul class="facts reveal">
      <li><b>When</b><span>Regular Saturday evenings, around 6:30 – 8:30pm</span></li>
      <li><b>Where</b><span>Venues around Marlow, including PILA Yoga and The Wellness Barn</span></li>
      <li><b>What&rsquo;s included</b><span>Complimentary tea and prasad (blessed food)</span></li>
      <li><b>Cost</b><span>Suggested donation, from around £12 – £15 in advance</span></li>
    </ul>
  </div>
</section>

<section class="sec cream">
  <div class="wrap">
    <h2 class="sec-title reveal">And <em>also&hellip;</em></h2>
    <div class="cards">
      <article class="card reveal"><h3>Bhakti retreats</h3><p>Immersive weekends and longer residential retreats with yoga, kirtan, philosophy sessions and nourishing meals. Email Emily to hear about the next one.</p></article>
      <article class="card reveal" style="--d:.06s"><h3>Cacao &amp; kirtan</h3><p>Cacao ceremonies paired with devotional singing, for an evening of slowing right down.</p></article>
      <article class="card reveal" style="--d:.12s"><h3>Charity kirtan</h3><p>Evenings of song in support of the charities we champion every year.</p></article>
      <article class="card reveal" style="--d:.18s"><h3>Woodland walks</h3><p>Foraging walks ending in woodland meditation.</p></article>
      <article class="card reveal" style="--d:.24s"><h3>Creative workshops</h3><p>Things like pottery-and-kirtan fusion evenings, with guest teachers and artists dropping in.</p></article>
      <article class="card reveal" style="--d:.3s"><h3>Guest artists</h3><p>Visiting teachers have included Balaram Das, Vraj Mohan, Tarini and Hannah Lunar Rose.</p></article>
    </div>
  </div>
</section>
''' + cta_band('Booking &amp; retreat enquiries', 'Events are booked via Bookwhen. For retreat details, email Emily at <a href="mailto:emily@theopenshala.com?subject=Bhakti%20Retreat%20Information">emily@theopenshala.com</a> or call 07917 644369.', 'See all events ↗', 'https://bookwhen.com/openshala', True)
    page('gatherings.html', 'Upcoming gatherings · Oh Shala Festival',
         'Kirtan evenings, cacao ceremonies and bhakti retreats with The Open Shala around Marlow, Buckinghamshire.',
         body, 'gatherings.html', og=I('listen'))

# ---------------------------------------------------------------- TEAM
TEAM = [
    ('Emily Cobie', 'Director', 'EC',
     'Emily began to dream up the Oh Shala Festival in 2019. As a local community yoga teacher, she had been bringing new offerings and facilitators to her community to understand new and different tools to add to the wellbeing toolbox.',
     'hello@ohshalafestival.com'),
    ('Benny Chandler', 'Logistics', 'BC',
     'Benny has been working with The Open Shala for the last four years as a coach and caterer for retreats and workshops. He looks after the technical and structural side of the festival.',
     'admin@ohshalafestival.com'),
    ('Amber Valentine', 'Site Manager &amp; Access Ambassador', 'AV',
     'Ten years ago Amber unintentionally opened a yoga studio with 30 mats, a small experiment that grew into a thriving community. She created HHJC, an online wellness hub, and is our Access Ambassador.',
     None),
    ('Siobhan Emin-Prentice', 'Diversity Ambassador', 'SE',
     'Siobhan is a wellness facilitator who has supported community around the world through events, retreats and festivals. She specialises in womb and women&rsquo;s healing and brings embodied movement and ceremony.',
     None),
    ('Fizz Yasin', 'Family Facilitator Curator', 'FY',
     'A radiant force of joy, healing and heart-led connection, Fizz is a yoga instructor, health coach, facialist and children&rsquo;s entertainer, and curates our family offering.',
     None),
]
def team():
    cards = ''
    for i, (n, role, ini, bio, mail) in enumerate(TEAM):
        m = f'<a class="tlink" href="mailto:{mail}">{mail}</a>' if mail else ''
        cards += f'''
      <article class="person reveal" style="--d:{i*0.06:.2f}s">
        <div class="mono" aria-hidden="true"><span>{ini}</span></div>
        <h3>{n}</h3>
        <p class="role">{role}</p>
        <p>{bio}</p>
        {m}
      </article>'''
    body = phero('The team', 'The people<br><em>behind it.</em>',
                 'Oh Shala is built by a small team, a lot of volunteers, and the local community that shows up every year.')
    body += f'''
<section class="sec cream">
  <div class="wrap">
    <div class="people">{cards}
    </div>
  </div>
</section>

{pb("circle", "Built by a community,<br><em>held by the land.</em>", short=True)}

<section class="sec plum">
  <div class="wrap two">
    <div>
      <p class="eyebrow reveal">Join in</p>
      <h2 class="sec-title reveal">Volunteers, facilitators, <em>traders.</em></h2>
    </div>
    <div class="reveal">
      <p class="lede">The weekend takes a team of incredible people. If you&rsquo;d like to be one of them, we&rsquo;d love to hear from you.</p>
      <a class="btn btn-gold" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
'''
    page('team.html', 'The team · Oh Shala Festival',
         'Meet Emily, Benny, Amber, Siobhan and Fizz, the team behind Oh Shala Festival.',
         body, 'team.html', og=I('joy'))

# ---------------------------------------------------------------- FAMILY
def family():
    body = phero('Family area', 'Bring the<br><em>little ones.</em>',
                 'Oh Shala is family-oriented, sober and vegan. Children are part of the gathering, with a space of their own to play.')
    body += f'''
<section class="sec night">
  <div class="wrap story-grid">
    <figure class="story-photo reveal">
      <img src="{I('family')}" alt="A woman playing with two small children" loading="lazy">
      <svg class="mandala spin" viewBox="-50 -50 100 100" aria-hidden="true"></svg>
    </figure>
    <div class="story-copy">
      <p class="eyebrow reveal">Children go free</p>
      <h2 class="sec-title reveal">A festival where kids <em>belong.</em></h2>
      <div class="prose reveal">
        <p>From children&rsquo;s yoga to circus skills and crafts, there&rsquo;s plenty for young festival-goers, and plenty of space for them to run.</p>
        <p>Our family offering is curated by <b>Fizz Yasin</b>, yoga instructor, health coach and children&rsquo;s entertainer.</p>
        <p>Children go free, with limited availability. Please <a href="tickets.html">check the tickets page</a> for current age bands.</p>
      </div>
    </div>
  </div>
</section>

{pb("wood", "Room to <em>roam.</em>", short=True)}

<section class="sec cream">
  <div class="wrap">
    <h2 class="sec-title reveal">What&rsquo;s <em>there</em></h2>
    <ul class="chips reveal">
      <li>Children&rsquo;s yoga</li><li>Circus</li><li>Crafts</li><li>Woodland play</li><li>Family area</li><li>Free camping</li><li>Showers &amp; toilets</li><li>Free water taps</li>
    </ul>
    <h2 class="sec-title reveal" style="margin-top:1.2em">Looking <em>after</em> everyone</h2>
    <div class="cards">
      <article class="card reveal"><h3>Supervision</h3><p>Children under 12 need constant supervision during workshops and classes. Adult supervision is needed at all times across the site.</p></article>
      <article class="card reveal" style="--d:.06s"><h3>Wristbands</h3><p>Our child welfare procedures include recording a parent or guardian&rsquo;s contact details on children&rsquo;s wristbands.</p></article>
      <article class="card reveal" style="--d:.12s"><h3>Help on hand</h3><p>Staff are on site to answer questions, and there&rsquo;s a staffed support van for anything extra.</p></article>
      <article class="card reveal" style="--d:.18s"><h3>Dogs</h3><p>Dogs aren&rsquo;t permitted in the festival arena, so little ones can roam freely.</p></article>
    </div>
  </div>
</section>
''' + cta_band('Grown-ups, we&rsquo;ve got you too.', 'Every workshop in the main tents is included in your ticket.', 'See the programme →', 'programme.html')
    page('family.html', 'Family · Oh Shala Festival',
         'A family-oriented, sober and vegan wellbeing festival in Buckinghamshire. Children go free. Children’s yoga, circus, crafts and more.',
         body, 'family.html', og=I('family'))

# ---------------------------------------------------------------- FOOD / STALLS / TREATMENTS
def food():
    body = phero('Food, stalls &amp; treatments', 'Local, plant-based,<br><em>plastic free.</em>',
                 'Everything on site is vegan and follows our zero-waste policy. Vendors and practitioners are paid directly, so you always know where your money goes.')
    body += f'''
<section class="sec cream">
  <div class="wrap trio">
    <article class="tri reveal">
      <div class="tri-img"><img src="{I('food', 1000)}" alt="People queueing at a vintage food van" loading="lazy"></div>
      <h3>Food</h3>
      <p>Local vendors serve completely vegan meals all weekend. Food isn&rsquo;t included in your ticket, and you&rsquo;re welcome to bring your own too. Please bring reusable cutlery.</p>
    </article>
    <article class="tri reveal" style="--d:.08s">
      <div class="tri-img"><img src="{I('market', 1000)}" alt="Festival-goers browsing a market stall" loading="lazy"></div>
      <h3>Market stalls</h3>
      <p>Local business stalls selling clothes, crafts and wellbeing goods from independent makers and small businesses.</p>
    </article>
    <article class="tri reveal" style="--d:.16s">
      <div class="tri-img"><img src="{I('bell', 1000)}" alt="A practitioner outside a bell tent" loading="lazy"></div>
      <h3>Treatments</h3>
      <p>Local holistic practitioners offer treatments on site. Treatments are booked and paid for separately from your ticket.</p>
    </article>
  </div>
</section>

<section class="sec leaf">
  <div class="wrap pledge-grid">
    <h2 class="sec-title reveal">The <em>zero-waste</em> promise</h2>
    <ul class="pledges">
      <li class="reveal"><b>All vendors plastic free</b><span>Every trader follows our zero-waste policy.</span></li>
      <li class="reveal" style="--d:.06s"><b>No bottled water</b><span>Free drinking water taps across site. Bring a reusable bottle.</span></li>
      <li class="reveal" style="--d:.12s"><b>Bring your own</b><span>A mug, bottle and cutlery will see you through the weekend.</span></li>
      <li class="reveal" style="--d:.18s"><b>Completely vegan</b><span>Plant-based plates, everywhere.</span></li>
    </ul>
  </div>
</section>

<section class="sec night" id="apply">
  <div class="wrap">
    <p class="eyebrow">Want to be here?</p>
    <h2 class="sec-title">Traders, vendors &amp; <em>practitioners</em></h2>
    <p class="lede">We&rsquo;d love to hear from local businesses, food vendors and holistic practitioners who share our values. All vendors must be plastic free.</p>
    <div class="cards dark">
      <article class="card reveal"><h3>Traders &amp; food vendors</h3><p>Applications and logistics, with Benny.</p><a class="tlink" href="mailto:admin@ohshalafestival.com?subject=Trader%20application">admin@ohshalafestival.com</a></article>
      <article class="card reveal" style="--d:.06s"><h3>Facilitators &amp; therapists</h3><p>Offer a workshop or treatment.</p><a class="tlink" href="mailto:admin@ohshalafestival.com?subject=Facilitator%20or%20therapist%20application">admin@ohshalafestival.com</a></article>
      <article class="card reveal" style="--d:.12s"><h3>Anything else</h3><p>General enquiries, with Emily.</p><a class="tlink" href="mailto:hello@ohshalafestival.com">hello@ohshalafestival.com</a></article>
    </div>
  </div>
</section>
'''
    page('food.html', 'Food, stalls & treatments · Oh Shala Festival',
         'Vegan food, local market stalls and holistic treatments, all plastic free. Apply to be a trader, vendor or practitioner at Oh Shala 2027.',
         body, 'food.html', og=I('food'))

# ---------------------------------------------------------------- FAQS
FAQ = [
    ('Tickets', [
        ('What is included in my ticket?', 'Your ticket price includes all workshops and classes shown on the schedule throughout the day, plus free camping on site. Vendors charge separately for food and treatments.'),
        ('Will I be able to get a refund if I am unable to attend?', 'All tickets are non-refundable and non-transferable unless we are in a lockdown due to COVID-19. You may transfer your ticket to someone else by contacting us with their details.'),
        ('Can I leave the site and re-enter?', 'You can leave and re-enter the site only with your valid wristband.'),
        ('Do you offer free tickets for carers?', 'Yes. Complimentary carer tickets are available for people with disabilities or medical conditions. Contact hello@ohshalafestival.com to enquire.'),
        ('Can I bring my children?', 'Yes! Anyone can come to the festival and children go free, with limited availability. Children must have adult supervision.'),
        ('Can we camp onsite?', 'Yes, and your festival ticket allows you to camp on site for free! Glamping and vehicle camping require separate purchases.'),
    ]),
    ('When you arrive', [
        ('How do I get there?', 'The Big Park, Penn House Estate, Penn Street, Beaconsfield, Amersham, HP7 0PS. Buses 1B and 1C stop nearby, and the closest train stations are High Wycombe, Beaconsfield and Amersham.'),
        ('Is there parking?', 'Yes, there will be parking, however we encourage everyone to car share as much as possible.'),
        ('Will there be disabled access?', 'We provide assistance for attendees with disabilities. Please email hello@ohshalafestival.com in advance so we can help.'),
    ]),
    ('Your weekend', [
        ('What facilities are available?', 'We will have toilets and showers on site and free water taps.'),
        ('What food and drink will be available?', 'Local vendors provide meals. You may bring your own food, and we ask that you bring reusable cutlery to minimise waste.'),
        ('Can I bring alcohol?', 'We have a strict no alcohol or drugs policy. Prohibited substances will be confiscated and may result in removal from site.'),
        ('What do I need to bring?', 'Your yoga mat, warm clothing and personal cutlery. You are welcome to bring your own food and drinks too.'),
        ('Where can I get help on the day?', 'We will have a number of staff on site to answer your questions, and a van staffed for additional support.'),
    ]),
]
def faqs():
    groups = ''
    for g, qs in FAQ:
        items = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qs)
        groups += f'<div class="faq-group reveal"><h3>{g}</h3><div class="qa">{items}</div></div>'
    body = phero('FAQs', 'Questions,<br><em>answered.</em>',
                 'Everything you need to know before you come. If we&rsquo;ve missed something, drop us a line.')
    body += f'''
<section class="sec plum">
  <div class="wrap">
    <div class="faq-page">{groups}</div>
  </div>
</section>
''' + cta_band('Still wondering?', 'Write to us and we&rsquo;ll get back to you.', 'Contact us →', 'contact.html')
    page('faqs.html', 'FAQs · Oh Shala Festival',
         'Tickets, camping, children, parking, what to bring and more: answers to common questions about Oh Shala Festival.',
         body, 'faqs.html', join=False, og=I('circle'))

# ---------------------------------------------------------------- CONTACT
def contact():
    body = phero('Contact', 'Say<br><em>hello.</em>',
                 'Questions, ideas, stall applications or just a nice note: we read everything.')
    body += f'''
<section class="sec cream">
  <div class="wrap contact-grid">
    <div class="who">
      <article class="reveal"><h3>General enquiries</h3><p>With Emily</p><a class="tlink" href="mailto:hello@ohshalafestival.com">hello@ohshalafestival.com</a></article>
      <article class="reveal" style="--d:.06s" id="traders"><h3>Trader applications &amp; logistics</h3><p>With Benny</p><a class="tlink" href="mailto:admin@ohshalafestival.com">admin@ohshalafestival.com</a></article>
      <article class="reveal" style="--d:.12s" id="facilitators"><h3>Facilitator &amp; therapist applications</h3><p>With Sarah</p><a class="tlink" href="mailto:admin@ohshalafestival.com">admin@ohshalafestival.com</a></article>
      <article class="reveal" style="--d:.18s"><h3>Follow along</h3><p><a class="tlink" href="https://instagram.com/ohshalafest" rel="noopener">@ohshalafest on Instagram</a><br><a class="tlink" href="https://facebook.com/ohshalafest" rel="noopener">@ohshalafest on Facebook</a></p></article>
    </div>
    <form class="cform reveal" id="cform" novalidate>
      <h2>Send us a message</h2>
      <label>Your name<input name="name" type="text" autocomplete="name" required></label>
      <label>Email<input name="email" type="email" autocomplete="email" required></label>
      <label>What&rsquo;s it about?
        <select name="topic">
          <option value="hello@ohshalafestival.com|General enquiry">General enquiry</option>
          <option value="admin@ohshalafestival.com|Trader or food vendor application">Trader or food vendor application</option>
          <option value="admin@ohshalafestival.com|Facilitator or therapist application">Facilitator or therapist application</option>
          <option value="hello@ohshalafestival.com|Access or carer ticket">Access or carer ticket</option>
        </select>
      </label>
      <label>Message<textarea name="message" rows="5" required></textarea></label>
      <button class="btn btn-plum" type="submit">Open in my email app →</button>
      <p class="msg" id="cmsg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>

<section class="sec night visit-band">
  <div class="wrap two">
    <div>
      <p class="eyebrow reveal">Find us</p>
      <h2 class="sec-title reveal">The Big Park, <em>Penn House Estate</em></h2>
    </div>
    <div class="reveal">
      <address>Penn Street, Beaconsfield<br>Amersham HP7 0PS</address>
      <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&query=Penn+House+Estate+Penn+Street+HP7+0PS" target="_blank" rel="noopener">Open in Maps ↗</a>
      <p class="small">Trains: High Wycombe, Beaconsfield or Amersham. Buses: 1B &amp; 1C. Please car-share.</p>
    </div>
  </div>
</section>
'''
    page('contact.html', 'Contact · Oh Shala Festival',
         'Get in touch with the Oh Shala team about tickets, trader applications, facilitator applications and access.',
         body, 'contact.html', join=False, og=I('sign'))

# ---------------------------------------------------------------- TERMS
def terms():
    body = phero('Terms &amp; conditions', 'The small<br><em>print.</em>', 'Please read before you buy a ticket. By purchasing, you agree to these terms.')
    body += '''
<section class="sec cream">
  <div class="wrap narrow legal">
    <!-- TODO: confirm wording against the original T&Cs. Note the original names "Parmoor Park" rather than Penn House Estate. -->
    <h2>1. Admissions policy</h2>
    <p>All admissions are strictly through pre-bought tickets through the official Oh Shala website or official ticketing officials.</p>
    <p>The festival retains discretion to deny entry or remove attendees found with alcohol, drugs, or showing signs of intoxication.</p>
    <p>Dogs are prohibited within Parmoor Park Field and the festival arena.</p>
    <h2>2. On site</h2>
    <p>Attendees younger than 12 require constant supervision during workshops and classes. We implement child welfare procedures where parent or guardian contact information is recorded on wristbands.</p>
    <p>Smoking is forbidden within the festival arena.</p>
    <p>We have zero tolerance toward abusive or inappropriate conduct toward attendees or staff.</p>
    <p>Open fires are strictly prohibited by festival attendees in Parmoor Park Farm and the arena.</p>
    <h2>3. Refund policy</h2>
    <p>Refunds are not permitted for any and all purchases under any grounds, including cancellations for medical reasons.</p>
    <p>Ticket transfers are available by contacting <a href="mailto:hello@ohshalafestival.com">hello@ohshalafestival.com</a> with the new participant&rsquo;s details.</p>
    <p>Force majeure circumstances, including pandemics, natural disasters or supplier failures, permit cancellation without liability.</p>
    <h2>4. Release and waiver</h2>
    <p>By purchasing tickets for the festival, you accept that Oh Shala Festival accepts no liability for injury or illness.</p>
    <p>Photography and videography take place during the festival for promotional purposes, and ticket purchase constitutes consent.</p>
  </div>
</section>
'''
    page('terms.html', 'Terms & conditions · Oh Shala Festival',
         'Admissions, on-site rules, refund policy and release for Oh Shala Festival.',
         body, '', join=False)

# ---------------------------------------------------------------- 404
def notfound():
    body = f'''<section class="phero nf">
  <div class="sky" aria-hidden="true"><div class="sun"></div><svg class="mandala halo" viewBox="-50 -50 100 100"></svg></div>
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>Lost in<br><em>the woods.</em></h1>
    <p class="lede">That page has wandered off. Let&rsquo;s get you back to the field.</p>
    <div class="hero-actions"><a class="btn btn-gold" href="index.html">Back to home</a><a class="btn btn-ghost" href="programme.html">See the programme</a></div>
  </div>
</section>'''
    page('404.html', 'Page not found · Oh Shala Festival', 'Page not found.', body, '', join=False)

# ---------------------------------------------------------------- refresh index chrome
def patch_index():
    p = ROOT / 'index.html'
    s = p.read_text()
    s = re.sub(r'<header class="nav".*?</header>', lambda m: nav(), s, flags=re.S)
    s = re.sub(r'<footer class="foot">.*?</footer>', lambda m: FOOTER, s, flags=re.S)
    p.write_text(s)
    print('patched index.html chrome')

if __name__ == '__main__':
    story(); programme(); tickets(); gatherings(); team(); family(); food(); faqs(); contact(); terms(); notfound()
    patch_index()
