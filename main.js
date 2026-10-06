(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- mandala generator (layered lotus petals) ---------- */
  const mandala = () => {
    let s = '';
    const ring = (n, rx, ry, cy, rot = 0) => {
      for (let i = 0; i < n; i++) {
        s += `<ellipse cx="0" cy="${cy}" rx="${rx}" ry="${ry}" transform="rotate(${(360 / n) * i + rot})"/>`;
      }
    };
    s += '<circle r="48"/><circle r="46"/>';
    ring(24, 2.2, 6, -41);
    ring(16, 4, 10, -32, 0);
    ring(12, 5, 14, -22, 15);
    ring(8, 6, 14, -12, 0);
    s += '<circle r="5"/><circle r="2"/>';
    return s;
  };
  const m = mandala();
  $$('svg.mandala').forEach(el => (el.innerHTML = m));

  /* ---------- nav ---------- */
  const nav = $('#nav');
  const links = $('#links');
  const burger = $('#burger');
  const heroTitle = document.body.dataset.page === 'home' ? $('.hero h1') : null;
  const onScroll = () => {
    nav.classList.toggle('stuck', scrollY > 40);
    if (heroTitle) {
      const gone = heroTitle.getBoundingClientRect().bottom < nav.offsetHeight;
      nav.classList.toggle('brand-hidden', !gone && !links.classList.contains('open'));
    }
    document.documentElement.style.setProperty('--sy', Math.min(scrollY * 0.25, 160));
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  burger.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    nav.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
    onScroll();
  });
  links.addEventListener('click', e => {
    if (e.target.closest('a')) {
      links.classList.remove('open');
      nav.classList.remove('menu-open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      onScroll();
    }
  });

  /* ---------- countdown ---------- */
  const target = new Date('2027-07-09T09:00:00+01:00').getTime();
  const tick = () => {
    if (!$('#cd')) return;
    let d = Math.max(0, target - Date.now());
    const days = Math.floor(d / 864e5);
    const hrs = Math.floor((d % 864e5) / 36e5);
    const min = Math.floor((d % 36e5) / 6e4);
    $('#cd').textContent = String(days).padStart(3, '0');
    $('#ch').textContent = String(hrs).padStart(2, '0');
    $('#cm').textContent = String(min).padStart(2, '0');
  };
  tick();
  setInterval(tick, 30000);

  /* ---------- scroll reveals ---------- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
  $$('.reveal').forEach(el => io.observe(el));

  /* ---------- count-up stats ---------- */
  const cio = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      cio.unobserve(e.target);
      const el = e.target;
      const end = +el.dataset.count;
      const plus = el.hasAttribute('data-plus') ? '+' : '';
      if (reduce) return;
      const t0 = performance.now();
      const run = t => {
        const p = Math.min((t - t0) / 1400, 1);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + (p === 1 ? plus : '');
        if (p < 1) requestAnimationFrame(run);
      };
      requestAnimationFrame(run);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* ---------- word-by-word welcome text ---------- */
  const words = $('.words');
  if (words) {
    const text = words.textContent.trim();
    words.setAttribute('aria-label', text);
    words.innerHTML = text.split(/\s+/).map(w => `<span aria-hidden="true">${w}</span>`).join(' ');
    const spans = $$('span', words);
    const paint = () => {
      const r = words.getBoundingClientRect();
      const vh = innerHeight;
      const p = Math.min(Math.max((vh * 0.85 - r.top) / (r.height + vh * 0.25), 0), 1);
      const n = Math.round(p * spans.length);
      spans.forEach((s, i) => s.classList.toggle('on', i < n));
    };
    addEventListener('scroll', paint, { passive: true });
    paint();
  }

  /* ---------- floating image on practice list ---------- */
  const imgs = {
    yoga: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/45d5bbdd-bc6c-4c8b-8fc5-5c20a2684203/Oh+Shala+Festival-172.jpg?format=750w',
    listen: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/111fd282-fece-4027-9a52-1b7f96aff927/EC_Oshala24_5381.jpg?format=750w',
    circle: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/b245a310-5546-4ab8-9150-2fd1ee958c6d/Oh+Shala+Festival-153.jpg?format=750w',
    tipi: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/09b43347-a860-4c6e-9571-46ac5133df69/EC_Oshala24_4396.jpg?format=750w',
    craft: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/6356cd82-fae0-41bd-bb6e-2b6c3af04a2d/Oh+Shala+Festival-232.jpg?format=750w',
    circus: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/764842e3-514e-4e44-8fb4-fdff9f4be217/Oh+Shala+Festival-98.jpg?format=750w',
    music: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/6d4582ed-9423-49ef-b465-0a27feba8632/EC_Oshala24_4075.jpg?format=750w',
    bell: 'https://images.squarespace-cdn.com/content/v1/63e22743b32cb51561aa4698/f2cd9c4d-43a1-4227-9acb-5aa18354f577/Oh+Shala+Festival-89.jpg?format=750w'
  };
  const preload = () => Object.values(imgs).forEach(u => { new Image().src = u; });
  const fi = $('#floatimg');
  const list = $('#plist');
  if (fi && list && matchMedia('(hover:hover)').matches && !reduce) {
    let x = 0, y = 0, tx = 0, ty = 0, raf = null;
    const loop = () => {
      x += (tx - x) * 0.14;
      y += (ty - y) * 0.14;
      fi.style.transform = `translate(${x + 40}px,${y - 150}px) rotate(${(tx - x) * 0.05}deg)`;
      raf = requestAnimationFrame(loop);
    };
    list.addEventListener('mouseenter', preload, { once: true });
    list.addEventListener('mousemove', e => { tx = e.clientX; ty = e.clientY; });
    $$('li', list).forEach(li => {
      li.addEventListener('mouseenter', e => {
        fi.style.backgroundImage = `url(${imgs[li.dataset.img]})`;
        if (!raf) { x = tx = e.clientX; y = ty = e.clientY; loop(); }
        fi.classList.add('show');
      });
    });
    list.addEventListener('mouseleave', () => {
      fi.classList.remove('show');
      cancelAnimationFrame(raf);
      raf = null;
    });
  }

  /* ---------- gentle parallax on photo breaks + collage ---------- */
  if (!reduce) {
    const px = $$('.pb-img img, .collage figure');
    let tick2 = false;
    const move = () => {
      tick2 = false;
      const vh = innerHeight;
      px.forEach(el => {
        const host = el.closest('.pb, .collage') || el;
        const r = host.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        const off = (r.top + r.height / 2 - vh / 2);
        const speed = el.tagName === 'IMG' ? -0.12 : parseFloat(el.dataset.speed || 0);
        el.style.setProperty('--py', (off * speed).toFixed(1) + 'px');
      });
    };
    addEventListener('scroll', () => { if (!tick2) { tick2 = true; requestAnimationFrame(move); } }, { passive: true });
    addEventListener('resize', move);
    move();
  }

  /* ---------- newsletter (front-end only: wire to your mailing platform) ---------- */
  const form = $('#signup');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const v = $('#email').value.trim();
    const msg = $('#msg');
    if (!/^\S+@\S+\.\S+$/.test(v)) {
      msg.textContent = 'Please enter a valid email address.';
      return;
    }
    msg.textContent = 'Thank you, you’re on the list. See you in the woods.';
    form.reset();
  });
})();

/* ---------- contact form: composes an email in the visitor's mail app ---------- */
(() => {
  const f = document.getElementById('cform');
  if (!f) return;
  f.addEventListener('submit', e => {
    e.preventDefault();
    const msg = document.getElementById('cmsg');
    const d = new FormData(f);
    const name = (d.get('name') || '').toString().trim();
    const email = (d.get('email') || '').toString().trim();
    const text = (d.get('message') || '').toString().trim();
    if (!name || !/^\S+@\S+\.\S+$/.test(email) || !text) {
      msg.textContent = 'Please fill in your name, a valid email and a message.';
      return;
    }
    const [to, subject] = d.get('topic').toString().split('|');
    const body = `${text}\n\n— ${name} (${email})`;
    location.href = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    msg.textContent = 'Opening your email app…';
  });
})();

/* ---------- hero film (Squarespace-hosted HLS stream from the current site) ---------- */
(() => {
  const hero = document.getElementById('heroVideo');
  if (!hero) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const attach = (video) => {
    const src = video.dataset.hls;
    if (window.Hls && Hls.isSupported()) {
      const hls = new Hls({ capLevelToPlayerSize: true, maxBufferLength: 15, maxMaxBufferLength: 30, abrEwmaDefaultEstimate: 6000000 });
      hls.on(Hls.Events.ERROR, (_, d) => {
        if (!d.fatal) return;
        if (d.type === Hls.ErrorTypes.NETWORK_ERROR) hls.startLoad();
        else if (d.type === Hls.ErrorTypes.MEDIA_ERROR) hls.recoverMediaError();
      });
      hls.loadSource(src);
      hls.attachMedia(video);
      return () => hls.destroy();
    }
    if (video.canPlayType('application/vnd.apple.mpegurl')) {
      video.src = src;
      return () => { video.removeAttribute('src'); video.load(); };
    }
    return () => {};
  };

  /* ambient background loop: poster shows instantly, video takes over as soon as it can play */
  hero.muted = true;
  hero.defaultMuted = true;
  hero.setAttribute('muted', '');
  const tryPlay = () => { if (!reduce) hero.play().catch(() => {}); };
  if (!reduce) {
    attach(hero);
    ['loadeddata', 'canplay'].forEach(ev => hero.addEventListener(ev, tryPlay));
    // if the browser blocked autoplay, start on the first interaction
    ['pointerdown', 'touchstart', 'keydown', 'scroll'].forEach(ev =>
      addEventListener(ev, () => { if (hero.paused) tryPlay(); }, { once: true, passive: true }));
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') tryPlay(); });
    // save bandwidth only when the hero is genuinely scrolled out of view
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) tryPlay();
      else if (document.visibilityState === 'visible') hero.pause();
    }).observe(hero.closest('.hero'));
  }

  /* full film in a dialog, with sound */
  const dlg = document.getElementById('film');
  const fv = document.getElementById('filmVideo');
  const open = document.getElementById('playFilm');
  let detach = null;
  const close = () => { if (dlg.open) dlg.close(); };
  open.addEventListener('click', () => {
    dlg.showModal();
    hero.pause();
    detach = attach(fv);
    fv.play().catch(() => {});
  });
  dlg.addEventListener('close', () => {
    fv.pause();
    if (detach) detach();
    detach = null;
    tryPlay();
  });
  document.getElementById('filmClose').addEventListener('click', close);
  dlg.addEventListener('click', e => { if (e.target === dlg) close(); });
})();
