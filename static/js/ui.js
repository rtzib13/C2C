// UI micro-interactions: button ripple, logo subtle animation
document.addEventListener('DOMContentLoaded', function () {
  // ripple effect for any element with .ripple
  document.querySelectorAll('.ripple').forEach(function (el) {
    el.addEventListener('pointerdown', function (ev) {
      const rect = el.getBoundingClientRect();
      const wave = document.createElement('span');
      wave.className = 'ripple-wave';
      const size = Math.max(rect.width, rect.height) * 0.8;
      wave.style.width = wave.style.height = size + 'px';
      wave.style.left = (ev.clientX - rect.left - size / 2) + 'px';
      wave.style.top = (ev.clientY - rect.top - size / 2) + 'px';
      el.appendChild(wave);
      wave.addEventListener('animationend', function () { wave.remove(); });
    });
  });

  // gentle logo wiggle on focus (keyboard) for accessibility
  const brand = document.querySelector('.brand-tile');
  if (brand) {
    brand.addEventListener('focus', function () { brand.classList.add('focused'); });
    brand.addEventListener('blur', function () { brand.classList.remove('focused'); });
  }

  // optional: small parallax for hero background when user has reduced-motion disabled
  try {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!prefersReduced) {
      const hero = document.querySelector('.hero-mockup');
      if (hero) {
        window.addEventListener('scroll', function () {
          const scrolled = window.scrollY;
          hero.style.backgroundPosition = `center ${Math.max( -20, -scrolled * 0.08 )}px`;
        }, { passive: true });
      }
    }
  } catch (e) { /* ignore */ }
});
