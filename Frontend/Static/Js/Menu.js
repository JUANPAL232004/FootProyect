const buttons = document.querySelectorAll('.cat-btn');
    const items = document.querySelectorAll('.menu-item');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // 1. Cambiar el botón activo visualmente
            buttons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            // 2. Obtener la categoría a filtrar
            // Convertimos a minúsculas y tomamos la primera palabra para evitar fallos con espacios
            const filter = button.textContent.toLowerCase().split(' ')[0];

            // 3. Mostrar u Ocultar
            items.forEach(item => {
                const category = item.getAttribute('data-category');
                
                // Si el producto coincide con el botón, se muestra, si no, se oculta
                if (category.includes(filter)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });