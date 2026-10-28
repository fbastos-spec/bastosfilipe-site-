// Aiguillage de la page d'accueil selon la langue du navigateur, puis le pays (Cloudflare Pages Function).
// Seule l'adresse / est concernée. Le choix explicite (cookie « lang ») gagne. Les robots ne sont jamais redirigés.
const BOT = /bot|crawl|spider|slurp|fetch|preview|facebookexternalhit|embedly|quora|outbrain|pinterest|vkshare|whatsapp|telegram|discord|curl|wget|python-requests|gptbot|claudebot|perplexity|applebot|bingpreview|duckduck|yandex|baidu|semrush|ahrefs|mj12|lighthouse|pagespeed|headless/i;
const PT = new Set(["PT", "BR", "AO", "MZ", "CV", "GW", "ST", "TL", "MO"]);
const FR = new Set(["FR", "BE", "CH", "LU", "MC", "CA", "SN", "CI", "ML", "BF", "NE", "TG", "BJ", "GA", "CG", "CD", "CM", "MG", "HT", "DZ", "MA", "TN", "RE", "GP", "MQ", "GF", "NC", "PF", "BI", "RW", "TD", "CF", "GN", "DJ", "KM", "SC", "MU", "LB"]);

function fromAcceptLanguage(h) {
  if (!h) return null;
  const tags = h.split(",").map((p, i) => { const [tag, ...rest] = p.trim().split(";"); let q = 1; for (const r of rest) { const m = /q=([\d.]+)/.exec(r); if (m) q = parseFloat(m[1]); } return { tag: tag.toLowerCase(), q, i }; }).sort((a, b) => b.q - a.q || a.i - b.i);
  for (const { tag } of tags) {
    const base = tag.split("-")[0];
    if (base === "fr") return "fr";
    if (base === "en") return "en";
    if (base === "pt") return "pt";
  }
  return null;
}

export async function onRequestGet(context) {
  const { request, next } = context;
  const url = new URL(request.url);
  if (url.pathname !== "/") return next();
  const cookie = request.headers.get("Cookie") || "";
  const m = /(?:^|;\s*)lang=(fr|en|pt)/.exec(cookie);
  if (m) {
    if (m[1] === "fr") return next();
    return Response.redirect(`${url.origin}/${m[1]}/`, 302);
  }
  const ua = request.headers.get("User-Agent") || "";
  if (BOT.test(ua)) return next();
  let lang = fromAcceptLanguage(request.headers.get("Accept-Language"));
  if (!lang) {
    const cc = (request.headers.get("CF-IPCountry") || "").toUpperCase();
    lang = PT.has(cc) ? "pt" : FR.has(cc) ? "fr" : "en";
  }
  if (lang === "fr") return next();
  // ne redirige que si la version existe (sécurité pendant la mise en ligne d'une langue)
  try {
    const probe = await context.env.ASSETS.fetch(new Request(`${url.origin}/${lang}/`, { method: "HEAD" }));
    if (probe.status !== 200) return next();
  } catch (e) {}
  const res = Response.redirect(`${url.origin}/${lang}/`, 302);
  const h = new Headers(res.headers); h.append("Vary", "Accept-Language, Cookie");
  return new Response(null, { status: 302, headers: h });
}
