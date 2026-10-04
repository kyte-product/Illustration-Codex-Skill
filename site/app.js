const grid = document.querySelector('#style-grid');
const search = document.querySelector('#style-search');
const count = document.querySelector('#result-count');
const dialog = document.querySelector('#style-modal');
const modalContent = document.querySelector('#modal-content');
let styles = [];

function renderStyles(query = '') {
  const term = query.trim().toLowerCase();
  const visible = styles.filter(style => `${style.name} ${style.description} ${style.palette} ${style.form}`.toLowerCase().includes(term));
  count.textContent = `${visible.length} ${visible.length === 1 ? 'style' : 'styles'}`;
  grid.innerHTML = visible.length ? visible.map(style => `
    <button class="style-card" type="button" data-style="${style.slug}" aria-label="View ${style.name} style details">
      <span class="style-image"><img loading="lazy" src="${style.reference}" alt="${style.name} style reference illustration" onerror="this.onerror=null;this.src='https://sohna.dev/waterlemon/src/image/min/skill/${style.slug}/${style.slug}_4.png'"></span>
      <span class="style-meta"><span class="style-title-row"><strong>${style.name}</strong><span class="style-arrow" aria-hidden="true">↗</span></span><span class="style-subtitle">${style.description}</span></span>
    </button>`).join('') : '<p class="empty-state">No styles match that search. Try another name or visual material.</p>';
  grid.querySelectorAll('[data-style]').forEach(card => card.addEventListener('click', () => openStyle(card.dataset.style)));
}
function openStyle(slug) {
  const style = styles.find(item => item.slug === slug);
  if (!style) return;
  modalContent.innerHTML = `
    <div class="modal-title-row"><div><span class="section-kicker">Style recipe · ${style.slug}-icon</span><h2 id="modal-title">${style.name}</h2><p>${style.description}. The skill includes a repeatable visual direction to help keep icons in this family consistent.</p></div></div>
    <div class="modal-images">${style.references.map((src, i) => `<img loading="lazy" src="${src}" alt="${style.name} style reference ${i + 1}" onerror="this.style.display='none'">`).join('')}</div>
    <div class="modal-facts"><div class="modal-fact"><span>Shape language</span><p>${style.form}</p></div><div class="modal-fact"><span>Surface & light</span><p>${style.finish}</p></div><div class="modal-fact"><span>Palette direction</span><p>${style.palette}</p></div><div class="modal-fact"><span>Use in Codex</span><p>Call <code>${style.slug}-icon</code> directly, or select ${style.name} in the wizard.</p></div></div>
    <div class="modal-bottom"><small>Reference examples from the public Waterlemon gallery.</small><button type="button" data-copy-style="${style.slug}">Copy “Use ${style.slug}-icon”</button></div>`;
  modalContent.querySelector('[data-copy-style]').addEventListener('click', async event => {
    const phrase = `Use the ${style.slug}-icon skill.`;
    try { await navigator.clipboard.writeText(phrase); event.currentTarget.textContent = 'Copied'; }
    catch { event.currentTarget.textContent = phrase; }
  });
  dialog.showModal();
}
search.addEventListener('input', () => renderStyles(search.value));
dialog.querySelector('.modal-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
const prompt = document.querySelector('#starter-prompt').textContent.trim();
document.querySelector('#copy-prompt').addEventListener('click', async event => {
  try { await navigator.clipboard.writeText(prompt); event.currentTarget.innerHTML = 'Copied <span>✓</span>'; }
  catch { event.currentTarget.textContent = prompt; }
});
fetch('styles.json').then(response => { if (!response.ok) throw new Error('Could not load style catalog'); return response.json(); }).then(data => { styles = data; renderStyles(); }).catch(() => { grid.innerHTML = '<p class="empty-state">The gallery could not load its style catalog. Serve this folder over HTTP, for example with <code>python3 -m http.server 8000</code>.</p>'; });
