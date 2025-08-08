 document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("btn-calculer");

  btn.addEventListener("click", function () {
    // Apply animated transformation
    btn.style.transition = "transform 0.4s ease, background-color 0.4s ease";
    btn.style.transform = "scale(1.1) rotate(5deg)";
    btn.style.backgroundColor = "#ffc107"; // flash yellow

    // Reset after short delay
    setTimeout(() => {
      btn.style.transform = "scale(1) rotate(0deg)";
      btn.style.backgroundColor = "#28a745"; // original green
    }, 400);
  });
});
