(function(){
  const translations = {
    es: {
      first_name_label: 'Nombre',
      last_name_label: 'Apellido',
      email_label: 'Correo electrónico',
      phone_label: 'Teléfono',
      position_label: 'Puesto al que aplica',
      previous_experience_label: 'Experiencia previa',
      motivation_label: '¿Por qué quieres unirte a nuestro equipo?',
      flexible_hours_label: 'Puedo trabajar horarios flexibles, incluidos fines de semana si es necesario.',
      submit_button: 'Enviar solicitud',
      lang_button: 'English'
    },
    en: {
      first_name_label: 'First name',
      last_name_label: 'Last name',
      email_label: 'Email',
      phone_label: 'Phone',
      position_label: 'Position applying for',
      previous_experience_label: 'Previous experience',
      motivation_label: 'Why do you want to join our team?',
      flexible_hours_label: 'I can work flexible hours, including weekends if needed.',
      submit_button: 'Submit Application',
      lang_button: 'Español'
    }
  };

  function setLanguage(lang){
    const map = translations[lang] || translations.en;
    document.querySelectorAll('[data-i18n]').forEach(el=>{
      const key = el.dataset.i18n;
      if(map[key]) el.textContent = map[key];
    });

    // translate select options for position
    const positionSelect = document.querySelector('select[name="position"]');
    if(positionSelect){
      const optionMap = {
        'residential_cleaner': {'en':'Residential Cleaner','es':'Limpiador/a residencial'},
        'commercial_cleaner': {'en':'Commercial Cleaner','es':'Limpiador/a comercial'},
        'team_lead': {'en':'Team Lead','es':'Líder de equipo'},
        'flex_position': {'en':'Flexible / Any Open Position','es':'Posición flexible / cualquier puesto disponible'}
      };
      Array.from(positionSelect.options).forEach(opt=>{
        const v = opt.value;
        if(optionMap[v]) opt.textContent = optionMap[v][lang] || optionMap[v].en;
      });
    }

    const langBtn = document.getElementById('lang-toggle');
    if(langBtn) langBtn.textContent = map.lang_button || (lang === 'en' ? 'Español' : 'English');
    localStorage.setItem('site_lang', lang);
  }

  document.addEventListener('DOMContentLoaded', function(){
    const saved = localStorage.getItem('site_lang') || 'en';
    setLanguage(saved);
    const btn = document.getElementById('lang-toggle');
    if(btn){
      btn.addEventListener('click', function(){
        const current = localStorage.getItem('site_lang') || 'en';
        const next = current === 'en' ? 'es' : 'en';
        setLanguage(next);
      });
    }
  });
})();
