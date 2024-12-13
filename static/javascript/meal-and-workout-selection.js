document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.meal-card, .workout-card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            const checkbox = card.querySelector('input[type="checkbox"]');
            checkbox.checked = !checkbox.checked;

            card.classList.toggle('selected', checkbox.checked);
        });
    });
});
