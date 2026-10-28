// Sélecteur de langue : versions FR / EN / PT de la page courante, traduction automatique pour les autres langues,
// mémorisation du choix (cookie « lang », un an).
(function () {
  function set(l) { document.cookie = "lang=" + l + "; Max-Age=31536000; Path=/; SameSite=Lax"; }
  var cur = document.documentElement.lang || "fr";
  var alt = {};
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (k) {
    try { alt[k.getAttribute("hreflang")] = new URL(k.href).pathname; } catch (e) {}
  });
  document.querySelectorAll("details.lang").forEach(function (d) {
    d.querySelectorAll("a[data-l]").forEach(function (a) {
      var l = a.getAttribute("data-l");
      if (alt[l]) a.setAttribute("href", alt[l]);
      if (l === cur) a.setAttribute("aria-current", "true");
      a.addEventListener("click", function () { set(l); });
    });
    d.querySelectorAll("a[data-tl]").forEach(function (a) {
      var t = a.getAttribute("data-tl");
      a.href = "https://bastosfilipe-com.translate.goog" + location.pathname + "?_x_tr_sl=" + cur + "&_x_tr_tl=" + t + "&_x_tr_hl=" + t + "&_x_tr_pto=wapp";
      a.rel = "noopener";
    });
  });
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details.lang[open]").forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute("open"); });
  });
  document.querySelectorAll('header.top a[href="/"], header.top a[href="/en/"], header.top a[href="/pt/"]').forEach(function (a) {
    if (a.closest("details.lang")) return;
    a.addEventListener("click", function () { set(cur); });
  });
})();
