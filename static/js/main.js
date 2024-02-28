$(document).ready(function () {
    (function () {
        "use strict";
        /* Product slider active */
        $(".product-list").owlCarousel({
            loop: false,
            nav: false,
            dots: true,
            autoplay: true,
            autoplayTimeout: 5000,
            animateOut: "fadeOut",
            animateIn: "fadeIn",
            item: 4,
            margin: 24,
            responsive: {
                0: {
                    items: 2,
                    margin: 8,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 3,
                },
                992: {
                    items: 5,
                },
                1200: {
                    items: 5.6,
                },
            },
        });

        $(".product-slider-active").owlCarousel({
            loop: true,
            nav: false,
            autoplay: true,
            autoplayTimeout: 5000,
            animateOut: "fadeOut",
            animateIn: "fadeIn",
            item: 4,
            margin: 30,
            responsive: {
                0: {
                    items: 2,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 3,
                },
                992: {
                    items: 4,
                },
                1200: {
                    items: 4,
                },
            },
        });

        $(".expert-list").owlCarousel({
            loop: false,
            nav: false,
            dots: true,
            autoplay: true,
            autoplayTimeout: 5000,
            animateOut: "fadeOut",
            animateIn: "fadeIn",
            item: 4,
            margin: 24,
            responsive: {
                0: {
                    items: 1.5,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 2.5,
                },
                992: {
                    items: 3,
                },
                1200: {
                    items: 4,
                },
            },
        });

        // preloader
        $.fakeLoader({
            spinner: "spinner5",
            bgColor: "#fff",
        });

        // smooth scroll
        $("a").on("click", function (event) {
            if (this.hash !== "") {
                event.preventDefault();

                var hash = this.hash;

                $("html, body").animate(
                    {
                        scrollTop: $(hash).offset().top - 50,
                    },
                    850
                );
            }
        });

        // navbar on scroll
        $(window).on("scroll", function () {
            var onScroll = $(this).scrollTop();

            if (onScroll > 50) {
                $(".navbar").addClass("navbar-fixed");
            } else {
                $(".navbar").removeClass("navbar-fixed");
            }
        });

        // hide navbar on click
        $(".navbar-nav>li>a").on("click", function () {
            $(".navbar-collapse").collapse("hide");
        });

        // counter
        $(".number-counter").each(function () {
            $(this)
                .prop("Counter", 0)
                .animate(
                    {
                        Counter: $(this).text(),
                    },
                    {
                        duration: 5000,
                        easing: "swing",
                        step: function (now) {
                            $(this).text(Math.ceil(now));
                        },
                    }
                );
        });
    })();

    /* AUTHOR LINK */
    $(".about-me-img").hover(
        function () {
            $(".authorWindowWrapper").stop().fadeIn("fast").find("p").addClass("trans");
        },
        function () {
            $(".authorWindowWrapper")
                .stop()
                .fadeOut("fast")
                .find("p")
                .removeClass("trans");
        }
    );


    /*=====================
        Video Popup JS
    =======================*/
    $('.video-popup').magnificPopup({
        type: 'video',
    });


    const productWrapper = document.querySelectorAll(".product-list .item");

    productWrapper.forEach((item) => {
        const images = item.querySelectorAll('.card__images a');
        const trigger = item.querySelector('.card__image');
        const popupItems = [];
        images.forEach((anchor) => {
            const src = anchor.getAttribute("href");
            popupItems.push({src});
        });

        $(trigger).magnificPopup({
            type: 'image',
            removalDelay: 300,
            mainClass: 'mfp-fade',
            gallery: {
                enabled: true
            },
            items: popupItems
        });
    });


// form
    document.getElementById("application").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission
        const btn = document.getElementById('application_btn');
        // Create FormData object
        const formData = new FormData(this);

        // Send form data to backend using Fetch API
        btn.setAttribute("disabled", "true");
        fetch("/create/", {
            method: "POST",
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.status) {
                    Swal.fire({
                        title: data.message,
                        icon: 'success',
                        position: 'center',
                        timer: 2000,
                        showConfirmButton: false,
                    });
                    this.reset();
                } else {
                    Swal.fire({
                        title: `${data.message}`,
                        icon: 'error',
                        position: 'center',
                        timer: 3000,
                    });
                }


            })
            .catch(error => {
                Swal.fire({
                    title: `${error}`,
                    icon: 'info',
                    position: 'center',
                    timer: 3000,
                });
            })
            .finally(() => {
                btn.removeAttribute("disabled")
            });
    });

});

