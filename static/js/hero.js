(function(){
  // Simple parallax: move background position slightly on scroll
  var hero = document.querySelector('.hero-mockup');
  if(!hero) return;
  var maxShift = 40;
  function onScroll(){
    var rect = hero.getBoundingClientRect();
    var h = window.innerHeight;
    var visible = Math.max(0, Math.min(rect.bottom, h) - Math.max(rect.top, 0));
    var pct = visible / rect.height;
    pct = Math.min(1, Math.max(0, pct));
    var shift = (pct - 0.5) * maxShift; // range -20..20
    hero.style.backgroundPosition = 'center calc(50% + '+shift+'px)';
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  window.addEventListener('resize', onScroll);
  onScroll();
})();
