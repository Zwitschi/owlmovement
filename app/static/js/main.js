/**
 * Main JavaScript for Corey Pellizzi Website
 */

document.addEventListener("DOMContentLoaded", function () {
  initializePortfolioFilters();
  initializeFormValidation();
});

/**
 * Portfolio filter functionality (multi-select)
 */
function initializePortfolioFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  const portfolioItems = document.querySelectorAll(".portfolio-item");

  if (filterBtns.length === 0) return;

  let activeFilters = new Set();

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const filter = this.getAttribute("data-filter");

      if (filter === "all") {
        // Reset: clear all selections
        activeFilters.clear();
        filterBtns.forEach((b) => b.classList.remove("active"));
        this.classList.add("active");
      } else {
        // Remove 'all' button active state
        const allBtn = document.querySelector('.filter-btn[data-filter="all"]');
        if (allBtn) allBtn.classList.remove("active");

        // Toggle this filter
        if (activeFilters.has(filter)) {
          activeFilters.delete(filter);
          this.classList.remove("active");
        } else {
          activeFilters.add(filter);
          this.classList.add("active");
        }

        // If nothing selected, fall back to 'all'
        if (activeFilters.size === 0) {
          if (allBtn) allBtn.classList.add("active");
        }
      }

      // Apply filter
      portfolioItems.forEach((item) => {
        const itemCategories = (item.getAttribute("data-category") || "").split(
          " ",
        );
        const show =
          activeFilters.size === 0 ||
          itemCategories.some((cat) => activeFilters.has(cat));
        if (show) {
          item.style.display = "block";
          setTimeout(() => (item.style.opacity = "1"), 10);
        } else {
          item.style.opacity = "0";
          setTimeout(() => (item.style.display = "none"), 300);
        }
      });
    });
  });
}

/**
 * Contact form validation
 */
function initializeFormValidation() {
  const contactForm = document.querySelector(".contact-form");
  if (!contactForm) return;

  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const subject = document.getElementById("subject").value.trim();
    const message = document.getElementById("message").value.trim();

    // Basic validation
    if (!name || !email || !subject || !message) {
      alert("Please fill in all required fields");
      return;
    }

    if (!isValidEmail(email)) {
      alert("Please enter a valid email address");
      return;
    }

    // Submit form (would be handled by Flask backend)
    console.log("Form submitted:", { name, email, subject, message });
    alert("Thank you for your message! I will get back to you soon.");
    contactForm.reset();
  });
}

/**
 * Email validation helper
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Smooth scroll for navigation links
 */
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});
