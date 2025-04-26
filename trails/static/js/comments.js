document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".comment-form form");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const response = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: {
          "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
        },
      });
      if (response.ok) {
        form.reset(); // Clear form fields
        location.reload(); // Refresh to show new comment
      }
    });
  }
});
