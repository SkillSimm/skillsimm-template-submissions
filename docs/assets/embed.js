(() => {
  if (new URLSearchParams(location.search).get("embed") !== "1") return;
  document.documentElement.classList.add("embedded");
  const page = location.pathname.endsWith("jobs.html") ? "jobs" : "explore";
  let parentOrigin;
  try { parentOrigin = new URL(document.referrer).origin; } catch { return; }
  let lastHeight = 0;
  function resize() {
    document.querySelectorAll("a[href]").forEach(a => {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    });
    // Measure content, not the viewport: this also lets the iframe shrink.
    const height = Math.ceil(document.body.getBoundingClientRect().height);
    if (height !== lastHeight) {
      lastHeight = height;
      parent.postMessage({ type: "skillsimm:height", page, height }, parentOrigin);
    }
  }
  addEventListener("DOMContentLoaded", () => {
    new ResizeObserver(resize).observe(document.body);
    new MutationObserver(resize).observe(document.body, {childList: true, subtree: true});
    resize();
  });
  addEventListener("message", event => {
    if (event.source !== parent || event.origin !== parentOrigin || event.data?.type !== "skillsimm:measure") return;
    lastHeight = 0;
    resize();
  });
  addEventListener("resize", resize);
})();
