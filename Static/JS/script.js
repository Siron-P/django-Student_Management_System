// Highlights the current page's nav link (replicates TanStack Router's activeProps/inactiveProps)
document.addEventListener("DOMContentLoaded", function () {
  var current = window.location.pathname.split("/").pop() || "index.html";

  document.querySelectorAll(".nav-link").forEach(function (link) {
    var href = link.getAttribute("href");
    if (href === current || (current === "" && href === "index.html")) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });

  // Basic client-side form handling: shows the error banner only if the
  // server-side endpoint this form posts to is unavailable/rejects it.
  // Wire this up to your real backend endpoint.
  document.querySelectorAll("form[data-auth-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      // Replace this with a real fetch() call to your auth API.
      // e.preventDefault();
      // fetch(form.action, { method: "POST", body: new FormData(form) })
      //   .then(res => { if (!res.ok) throw new Error(); window.location.href = "/dashboard.html"; })
      //   .catch(() => document.getElementById(form.dataset.authForm).classList.add("visible"));
    });
  });
});
