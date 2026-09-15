const darkModeBtn = document.getElementById("darkModeBtn");

darkModeBtn.addEventListener("click", function () {

    document.body.classList.toggle("dark-mode");

});
function filterNews(category) {

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        if (category === "all") {
            card.style.display = "block";
        }
        else if (card.dataset.category === category) {
            card.style.display = "block";
        }
        else {
            card.style.display = "none";
        }

    });

}
function searchNews() {

    const searchInput =
        document.getElementById("searchBox").value.toLowerCase();

    const cards =
        document.querySelectorAll(".card");

    cards.forEach(card => {

        const title =
            card.querySelector("h3").textContent.toLowerCase();

        if (title.includes(searchInput)) {
            card.style.display = "block";
        }
        else {
            card.style.display = "none";
        }

    });

}