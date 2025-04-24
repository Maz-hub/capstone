document.addEventListener("DOMContentLoaded", function () {
  const section = document.querySelector(".trail-section");

  // Only scroll if URL has a difficulty filter
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("difficulty") && section) {
    section.scrollIntoView({ behavior: "smooth" });
  }
});
