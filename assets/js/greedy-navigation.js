/* Priority navigation: keep the current section and switches visible as links move. */
const siteNav = document.querySelector('#site-nav');
const navButton = siteNav.querySelector('.nav-toggle');
const visibleLinks = siteNav.querySelector('.visible-links');
const hiddenLinks = siteNav.querySelector('.hidden-links');
const navBreaks = [];

function closeNavigation(restoreFocus = false) {
  hiddenLinks.classList.add('hidden');
  navButton.classList.remove('close');
  navButton.setAttribute('aria-expanded', 'false');
  if (restoreFocus) navButton.focus();
}

function updateNav() {
  const availableWidth = () => siteNav.clientWidth - (navButton.classList.contains('hidden') ? 0 : navButton.getBoundingClientRect().width + 30);
  if (visibleLinks.getBoundingClientRect().width > availableWidth()) {
    while (visibleLinks.getBoundingClientRect().width > availableWidth()) {
      const movable = [...visibleLinks.children].filter(item => !item.classList.contains('persist')).pop();
      if (!movable) break;
      navBreaks.push(visibleLinks.getBoundingClientRect().width);
      hiddenLinks.prepend(movable);
      navButton.classList.remove('hidden');
    }
  } else {
    while (navBreaks.length && availableWidth() > navBreaks[navBreaks.length - 1]) {
      const firstHidden = hiddenLinks.firstElementChild;
      if (!firstHidden) break;
      visibleLinks.insertBefore(firstHidden, visibleLinks.querySelector('.persist.tail'));
      navBreaks.pop();
    }
    if (!navBreaks.length) {
      navButton.classList.add('hidden');
      closeNavigation();
    }
  }
  navButton.setAttribute('aria-expanded', !navButton.classList.contains('hidden') && !hiddenLinks.classList.contains('hidden'));
  navButton.setAttribute('count', navBreaks.length);
  const height = document.querySelector('.masthead').getBoundingClientRect().height;
  document.body.style.paddingTop = `${height}px`;
  const sidebar = document.querySelector('.sidebar');
  if (sidebar) sidebar.style.paddingTop = window.innerWidth >= 925 ? `${height}px` : '';
}

navButton.addEventListener('click', () => {
  hiddenLinks.classList.toggle('hidden');
  navButton.classList.toggle('close');
  navButton.setAttribute('aria-expanded', !hiddenLinks.classList.contains('hidden'));
});
siteNav.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !hiddenLinks.classList.contains('hidden')) {
    closeNavigation(true);
    event.preventDefault();
  }
});
window.addEventListener('resize', updateNav);
screen.orientation?.addEventListener('change', updateNav);
updateNav();
