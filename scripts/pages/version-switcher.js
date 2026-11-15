/* Version switcher of the robarm documentation on GitHub Pages (D55, research/zdocs.md §8).
 *
 * scripts/pages/site.py copies this file to the site root and adds to every page
 *   <script id="xdmod-version-switcher" src="<root>/version-switcher.js" data-site-root="<root>" defer>
 * where <root> is the relative path from the page to the site root. The first path segment below
 * the root is the version (latest, v0.1.0, ...). The switcher reads <root>/versions.json and links
 * each version to the same page; if that page does not exist there, to the version's start page.
 * Old versions get a banner that points to latest.
 */
(function () {
  "use strict";
  var me = document.getElementById("xdmod-version-switcher");
  if (!me || !window.fetch) return;
  var root = new URL((me.getAttribute("data-site-root") || ".").replace(/\/?$/, "/"), location.href);
  var here = location.href.split("#")[0].split("?")[0];
  if (here.indexOf(root.href) !== 0) return;
  var rest = here.slice(root.href.length);           // e.g. "v0.1.0/se-req/index.html"
  var cut = rest.indexOf("/");
  var current = cut < 0 ? rest : rest.slice(0, cut);
  var page = cut < 0 ? "" : rest.slice(cut + 1);

  function go(version) {
    var target = new URL(version + "/" + page, root).href + location.hash;
    var start = new URL(version + "/", root).href;
    fetch(target, { method: "HEAD" })
      .then(function (r) { location.href = r.ok ? target : start; })
      .catch(function () { location.href = start; });
  }

  function label(v) {
    return v.name === "latest" ? "latest (main)" : "baseline " + v.name;
  }

  function render(versions) {
    var box = document.createElement("div");
    box.className = "xdmod-versions";
    box.style.cssText = "font-size:90%;margin:6px 0 0;";
    var sel = document.createElement("select");
    sel.setAttribute("aria-label", "Documentation version");
    sel.style.cssText = "font-size:inherit;max-width:100%;";
    versions.forEach(function (v) {
      var o = document.createElement("option");
      o.value = v.name;
      o.textContent = label(v);
      o.title = (v.ref || "") + (v.sha ? " @ " + v.sha.slice(0, 12) : "");
      if (v.name === current) o.selected = true;
      sel.appendChild(o);
    });
    sel.addEventListener("change", function () { go(sel.value); });
    box.appendChild(document.createTextNode("Version: "));
    box.appendChild(sel);

    var slot = document.querySelector(".wy-side-nav-search");   // sphinx_rtd_theme (zdocs)
    if (slot) {
      slot.appendChild(box);
    } else {                                                   // Doxygen and other pages
      box.style.cssText = "position:fixed;right:12px;bottom:12px;z-index:1000;padding:6px 8px;" +
        "background:#fff;border:1px solid #bbb;border-radius:4px;font:13px sans-serif;";
      document.body.appendChild(box);
    }

    if (current !== "latest" && versions.some(function (v) { return v.name === "latest"; })) {
      var bar = document.createElement("div");
      bar.style.cssText = "background:#fff3cd;color:#664d03;border-bottom:1px solid #e6c96b;" +
        "padding:6px 12px;font:14px sans-serif;text-align:center;";
      var a = document.createElement("a");
      a.href = "#";
      a.textContent = "the latest version";
      a.addEventListener("click", function (e) { e.preventDefault(); go("latest"); });
      bar.appendChild(document.createTextNode("You are reading baseline " + current + ". See "));
      bar.appendChild(a);
      bar.appendChild(document.createTextNode(" for the state of main."));
      document.body.insertBefore(bar, document.body.firstChild);
    }
  }

  fetch(new URL("versions.json", root).href, { cache: "no-cache" })
    .then(function (r) { return r.ok ? r.json() : { versions: [] }; })
    .then(function (d) { if (d.versions && d.versions.length) render(d.versions); })
    .catch(function () { /* opened from disk or offline: no switcher */ });
})();
