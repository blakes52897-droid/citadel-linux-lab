function initProjectReveal() {
  const targets = document.querySelectorAll(
    "h1, h2, article, .card, .panel, .project-card, pre, .terminal"
  );

  targets.forEach((el) => {
    el.classList.add("project-reveal");
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12
  });

  targets.forEach((el) => observer.observe(el));
}

document.addEventListener("DOMContentLoaded", initProjectReveal);

function initProjectHud() {
  if (document.querySelector(".project-data-layer")) return;

  const layer = document.createElement("div");
  layer.className = "project-data-layer";
  document.body.prepend(layer);

  const leftRail = document.createElement("div");
  leftRail.className = "project-side-rail left";

  const rightRail = document.createElement("div");
  rightRail.className = "project-side-rail right";

  document.body.appendChild(leftRail);
  document.body.appendChild(rightRail);

  const banner = document.createElement("div");
  banner.className = "project-command-banner";

  const pageName = document.title
    ? document.title.replace("| The Citadel", "").trim()
    : "Citadel Project Module";

  banner.innerHTML = `<span>ARGUS PROJECT VIEW // ${pageName}</span>`;

  const header = document.querySelector("header");
  if (header && header.insertAdjacentElement) {
    header.insertAdjacentElement("afterend", banner);
  } else {
    document.body.prepend(banner);
  }

  for (let i = 0; i < 18; i++) {
    const particle = document.createElement("div");
    particle.className = "project-particle";

    particle.style.left = `${8 + Math.random() * 84}%`;
    particle.style.top = `${18 + Math.random() * 72}%`;
    particle.style.animationDelay = `${Math.random() * 5}s`;
    particle.style.animationDuration = `${4.5 + Math.random() * 4}s`;

    document.body.appendChild(particle);
  }
}

document.addEventListener("DOMContentLoaded", initProjectHud);
