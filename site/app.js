const grid = document.querySelector('#style-grid');
const dialog = document.querySelector('#style-modal');
const modalTitle = document.querySelector('#modal-title');
const modalGrid = document.querySelector('#modal-grid');
const modalRecipe = document.querySelector('#modal-recipe');
const modalStatus = document.querySelector('#modal-status');
let styles = [];
let activeStyle = null;
let activeStep = 0;
let workflowTimer;

function imageMarkup(reference, alt = '') {
  return `<img loading="lazy" src="${reference}" alt="${alt}">`;
}

function renderStyles() {
  grid.innerHTML = styles.map(style => {
    const previews = style.references.slice(0, 4);
    const single = previews.length === 1 ? ' single' : '';
    return `<li class="style-card"><button class="style-button" type="button" data-style="${style.slug}" aria-label="Open ${style.name} style preview"><figure class="style-figure"><span class="style-thumbs${single}" aria-hidden="true">${previews.map((src, index) => `<span class="style-thumb">${imageMarkup(src, `${style.name} reference ${index + 1}`)}</span>`).join('')}</span><figcaption class="style-label">${style.name}</figcaption></figure></button></li>`;
  }).join('');
  grid.querySelectorAll('[data-style]').forEach(button => button.addEventListener('click', () => openStyle(button.dataset.style, button)));
}

function openStyle(slug, trigger) {
  activeStyle = styles.find(style => style.slug === slug);
  if (!activeStyle) return;
  dialog.dataset.returnFocus = trigger ? 'yes' : 'no';
  dialog.dataset.style = slug;
  modalTitle.textContent = `${activeStyle.name} Skill`;
  modalGrid.innerHTML = activeStyle.references.slice(0, 12).map((src, index) => `<div class="modal-item">${imageMarkup(src, `${activeStyle.name} visual reference ${index + 1}`)}</div>`).join('');
  modalRecipe.innerHTML = `<div class="recipe-part"><strong>Shape</strong>${activeStyle.form}</div><div class="recipe-part"><strong>Surface</strong>${activeStyle.finish}</div><div class="recipe-part"><strong>Palette</strong>${activeStyle.palette}</div>`;
  modalStatus.textContent = '';
  dialog.showModal();
  document.querySelector('#modal-close').focus();
}

function closeModal() {
  if (dialog.open) dialog.close();
}
document.querySelector('#modal-close').addEventListener('click', closeModal);
dialog.addEventListener('click', event => { if (event.target === dialog) closeModal(); });
dialog.addEventListener('close', () => {
  if (activeStyle && dialog.dataset.returnFocus === 'yes') grid.querySelector(`[data-style="${activeStyle.slug}"]`)?.focus();
});

document.querySelector('#copy-style').addEventListener('click', async event => {
  if (!activeStyle) return;
  const command = `Use the ${activeStyle.slug}-icon skill. If I attach an illustration, use it as the subject reference and redraw it in this style.`;
  try {
    await navigator.clipboard.writeText(command);
    modalStatus.textContent = `Copied: ${command}`;
  } catch {
    modalStatus.textContent = command;
  }
  const button = event.currentTarget;
  button.innerHTML = 'Copied <span aria-hidden="true">✓</span>';
  window.setTimeout(() => { if (activeStyle) button.innerHTML = 'Use in Codex <span aria-hidden="true">↗</span>'; }, 1700);
});

document.querySelector('#copy-prompt').addEventListener('click', async event => {
  const prompt = 'Use the illustration-icon-wizard skill. Ask me one question at a time and wait for my answer before asking the next. At the subject step, let me describe an idea or attach an illustration to redraw in my chosen style.';
  const button = event.currentTarget;
  try {
    await navigator.clipboard.writeText(prompt);
    button.textContent = 'Prompt copied';
    document.querySelector('#prompt-copy-status').textContent = 'Wizard prompt copied to clipboard.';
  } catch {
    button.textContent = prompt;
    document.querySelector('#prompt-copy-status').textContent = prompt;
  }
  window.setTimeout(() => { button.textContent = 'Copy wizard prompt'; }, 1800);
});

const steps = [...document.querySelectorAll('[data-step]')];
const workflowImage = document.querySelector('#workflow-image');
function showStep(index) {
  activeStep = (index + steps.length) % steps.length;
  steps.forEach((step, i) => {
    const active = i === activeStep;
    step.classList.toggle('is-active', active);
    if (active) step.setAttribute('aria-current', 'step'); else step.removeAttribute('aria-current');
  });
  const source = styles[activeStep]?.references[0];
  if (source) {
    const updateImage = () => {
      workflowImage.src = source;
    };
    workflowImage.classList.add('is-changing');
    window.setTimeout(() => { updateImage(); workflowImage.classList.remove('is-changing'); }, 160);
  }
  window.clearTimeout(workflowTimer);
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) workflowTimer = window.setTimeout(() => showStep(activeStep + 1), 4500);
}
steps.forEach((step, index) => step.addEventListener('click', () => showStep(index)));
showStep(0);

document.querySelectorAll('.faq-item').forEach(item => item.addEventListener('toggle', () => {
  if (item.open) document.querySelectorAll('.faq-item').forEach(other => { if (other !== item) other.open = false; });
}));

fetch('styles.json').then(response => {
  if (!response.ok) throw new Error('Style catalog unavailable');
  return response.json();
}).then(data => { styles = data; renderStyles(); showStep(activeStep); }).catch(() => {
  grid.innerHTML = '<li class="style-empty">The style collection could not be loaded.</li>';
});
