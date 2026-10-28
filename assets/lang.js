// Mémorise le choix de langue quand on clique sur Français, EN ou PT dans le menu (cookie « lang », un an).
(function () {
  function set(l) { document.cookie = "lang=" + l + "; Max-Age=31536000; Path=/; SameSite=Lax"; }
  document.querySelectorAll('a[href="/"], a[href="/index.html"], a[href="/en/"], a[href="/pt/"]').forEach(function (a) {
    if (!a.closest("header.top") && !a.closest("nav.nav")) return;
    a.addEventListener("click", function () {
      var h = a.getAttribute("href");
      set(h.indexOf("/en/") === 0 ? "en" : h.indexOf("/pt/") === 0 ? "pt" : "fr");
    });
  });
  var l = document.documentElement.lang; if (l === "en" || l === "pt" || l === "fr") { /* la visite d'une version confirme un choix seulement par clic */ }
})();
