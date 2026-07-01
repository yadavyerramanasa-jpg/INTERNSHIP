// ==========================
// AuraStyle JavaScript
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    console.log("AuraStyle Loaded Successfully");

    // ==========================
    // Navbar Scroll Effect
    // ==========================

    const navbar = document.querySelector("nav");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.background = "#0f172a";
            navbar.style.boxShadow = "0 10px 25px rgba(0,0,0,.4)";

        } else {

            navbar.style.background = "#111827";
            navbar.style.boxShadow = "none";

        }

    });


    // ==========================
    // Reveal Animation
    // ==========================

    const cards = document.querySelectorAll(".card");

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0px)";

            }

        });

    });

    cards.forEach(card => {

        card.style.opacity = "0";
        card.style.transform = "translateY(60px)";
        card.style.transition = ".8s";

        observer.observe(card);

    });


    // ==========================
    // Product Hover Effect
    // ==========================

    const productCards = document.querySelectorAll(".product-card");

    productCards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-12px) scale(1.02)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });


    // ==========================
    // Search Validation
    // ==========================

    const searchForm = document.querySelector(".search-section form");

    if (searchForm) {

        searchForm.addEventListener("submit", (e) => {

            const input = searchForm.querySelector("input");

            if (input.value.trim() === "") {

                alert("Please enter a search keyword.");

                e.preventDefault();

            }

        });

    }


    // ==========================
    // Image Upload Preview
    // ==========================

    const imageInput = document.querySelector('input[type="file"]');

    if (imageInput) {

        imageInput.addEventListener("change", function () {

            const file = this.files[0];

            if (!file) return;

            const reader = new FileReader();

            reader.onload = function (e) {

                let preview = document.getElementById("preview");

                if (!preview) {

                    preview = document.createElement("img");

                    preview.id = "preview";

                    preview.style.width = "250px";
                    preview.style.marginTop = "25px";
                    preview.style.borderRadius = "15px";
                    preview.style.boxShadow = "0 15px 30px rgba(0,0,0,.4)";

                    imageInput.parentElement.appendChild(preview);

                }

                preview.src = e.target.result;

            }

            reader.readAsDataURL(file);

        });

    }


    // ==========================
    // Button Ripple Effect
    // ==========================

    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {

        button.addEventListener("click", function () {

            this.style.transform = "scale(.95)";

            setTimeout(() => {

                this.style.transform = "scale(1)";

            }, 150);

        });

    });


    // ==========================
    // Smooth Page Fade
    // ==========================

    document.body.style.opacity = "0";

    setTimeout(() => {

        document.body.style.transition = ".6s";
        document.body.style.opacity = "1";

    }, 100);

});